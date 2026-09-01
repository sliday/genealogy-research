#!/usr/bin/env python3
"""Sanity-check a GEDCOM file before and after enrichment.

Stdlib only. Works on GEDCOM 5.5, 5.5.1 and 7.0 line syntax.

Reports:
  - version, declared encoding, SHA-256, record counts by tag
  - dangling cross-references (pointers to records that do not exist)
  - individuals and families that no family or individual points to
  - events (BIRT, CHR, DEAT, BURI, MARR, ...) and names without a SOUR citation
  - possibly living people (born within the privacy window, no death event)
  - with --baseline OLD.ged: records added, removed, and changed vs. the baseline

Exit code 1 when dangling references are found, 0 otherwise.

Usage:
  python3 scripts/gedcom_check.py tree.ged
  python3 scripts/gedcom_check.py tree.enriched.ged --baseline tree.ged --json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

LINE_RE = re.compile(r"^(\d+)\s+(?:(@[^@]+@)\s+)?([A-Za-z0-9_]+)(?:\s(.*))?$")
EVENT_TAGS = {"BIRT", "CHR", "BAPM", "DEAT", "BURI", "CREM", "MARR", "DIV", "ADOP",
              "IMMI", "EMIG", "NATU", "CENS", "RESI", "OCCU", "EVEN"}
CITEABLE_TAGS = EVENT_TAGS | {"NAME"}
RECORD_TAGS = {"INDI", "FAM", "SOUR", "REPO", "NOTE", "OBJE", "SNOTE", "SUBM"}
YEAR_RE = re.compile(r"(\d{4})")


class Node:
    __slots__ = ("level", "xref", "tag", "value", "children", "line_no")

    def __init__(self, level, xref, tag, value, line_no):
        self.level = level
        self.xref = xref
        self.tag = tag
        self.value = value or ""
        self.children = []
        self.line_no = line_no

    def find(self, tag):
        return [c for c in self.children if c.tag == tag]

    def first(self, tag):
        for c in self.children:
            if c.tag == tag:
                return c
        return None

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def fingerprint(self):
        parts = []
        for n in self.walk():
            if n is self:
                continue
            parts.append(f"{n.level} {n.tag} {n.value}")
        return "\n".join(parts)


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw[3:].decode("utf-8"), "utf-8-bom"
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16"), "utf-16"
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return raw.decode("latin-1"), "latin-1 (fallback; check HEAD.CHAR)"


def parse(text: str) -> tuple[list[Node], list[str]]:
    roots: list[Node] = []
    stack: list[Node] = []
    problems: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        m = LINE_RE.match(line.rstrip("\r"))
        if not m:
            problems.append(f"line {i}: unparseable: {line[:80]!r}")
            continue
        level = int(m.group(1))
        node = Node(level, m.group(2), m.group(3).upper(), m.group(4), i)
        if level == 0:
            roots.append(node)
            stack = [node]
            continue
        while stack and stack[-1].level >= level:
            stack.pop()
        if not stack:
            problems.append(f"line {i}: level {level} without parent")
            continue
        if stack[-1].level != level - 1:
            problems.append(f"line {i}: level jumps from {stack[-1].level} to {level}")
        stack[-1].children.append(node)
        stack.append(node)
    return roots, problems


def flatten_conc(node: Node) -> str:
    value = node.value
    for c in node.children:
        if c.tag == "CONC":
            value += c.value
        elif c.tag == "CONT":
            value += "\n" + c.value
    return value


def name_of(indi: Node) -> str:
    n = indi.first("NAME")
    return n.value.replace("/", "").strip() if n else "(no name)"


def year_of(event: Node | None) -> int | None:
    if not event:
        return None
    d = event.first("DATE")
    if not d:
        return None
    m = YEAR_RE.search(d.value)
    return int(m.group(1)) if m else None


def analyze(path: Path, privacy_years: int) -> dict:
    text, encoding = read_text(path)
    roots, problems = parse(text)
    by_xref = {r.xref: r for r in roots if r.xref}
    counts = Counter(r.tag for r in roots)

    head = next((r for r in roots if r.tag == "HEAD"), None)
    version = declared_char = None
    if head:
        gedc = head.first("GEDC")
        if gedc and gedc.first("VERS"):
            version = gedc.first("VERS").value
        if head.first("CHAR"):
            declared_char = head.first("CHAR").value

    # dangling pointers: any value that looks like @X@ and is not a defined record
    dangling = []
    pointed_to = Counter()
    for r in roots:
        for n in r.walk():
            v = n.value.strip()
            if v.startswith("@") and v.endswith("@") and len(v) > 2 and not v.startswith("@#"):
                pointed_to[v] += 1
                if v not in by_xref:
                    dangling.append(f"line {n.line_no}: {r.tag} {r.xref} {n.tag} -> {v} (undefined)")

    # unlinked individuals/families
    unlinked_indi = [f"{r.xref} {name_of(r)}" for r in roots
                     if r.tag == "INDI" and not r.find("FAMS") and not r.find("FAMC")]
    unlinked_fam = [r.xref for r in roots
                    if r.tag == "FAM" and not (r.find("HUSB") or r.find("WIFE") or r.find("CHIL"))]

    # uncited assertions
    uncited = []
    for r in roots:
        if r.tag not in {"INDI", "FAM"}:
            continue
        for n in r.children:
            if n.tag in CITEABLE_TAGS and not n.find("SOUR"):
                label = name_of(r) if r.tag == "INDI" else r.xref
                detail = n.first("DATE").value if n.first("DATE") else n.value
                uncited.append(f"{r.xref} {label}: {n.tag} {detail}".rstrip())

    # possibly living
    cutoff = date.today().year - privacy_years
    living = []
    for r in roots:
        if r.tag != "INDI" or r.first("DEAT") or r.first("BURI"):
            continue
        by = year_of(r.first("BIRT")) or year_of(r.first("CHR"))
        if by and by > cutoff:
            living.append(f"{r.xref} {name_of(r)} b. {by}")

    return {
        "file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "encoding_detected": encoding,
        "head_char": declared_char,
        "gedcom_version": version,
        "records": dict(sorted(counts.items())),
        "parse_problems": problems,
        "dangling_references": dangling,
        "unlinked_individuals": unlinked_indi,
        "empty_families": unlinked_fam,
        "uncited_assertions": uncited,
        "possibly_living": living,
        "_roots": roots,
    }


def diff(old: dict, new: dict) -> dict:
    o = {r.xref: r for r in old["_roots"] if r.xref}
    n = {r.xref: r for r in new["_roots"] if r.xref}
    added = sorted(set(n) - set(o))
    removed = sorted(set(o) - set(n))
    changed = sorted(x for x in set(o) & set(n) if o[x].fingerprint() != n[x].fingerprint())
    return {
        "added": [f"{x} {n[x].tag} {name_of(n[x]) if n[x].tag == 'INDI' else ''}".strip() for x in added],
        "removed": [f"{x} {o[x].tag} {name_of(o[x]) if o[x].tag == 'INDI' else ''}".strip() for x in removed],
        "changed": [f"{x} {n[x].tag} {name_of(n[x]) if n[x].tag == 'INDI' else ''}".strip() for x in changed],
        "new_uncited": sorted(set(new["uncited_assertions"]) - set(old["uncited_assertions"])),
        "new_dangling": sorted(set(new["dangling_references"]) - set(old["dangling_references"])),
    }


def print_report(rep: dict, d: dict | None) -> None:
    print(f"File: {rep['file']}")
    print(f"SHA-256: {rep['sha256']}")
    print(f"GEDCOM version: {rep['gedcom_version'] or 'unknown'}; HEAD.CHAR: {rep['head_char'] or 'none'}; "
          f"bytes decoded as {rep['encoding_detected']}")
    print("Records: " + ", ".join(f"{k}={v}" for k, v in rep["records"].items()))

    def section(title, items, limit=40):
        print(f"\n{title}: {len(items)}")
        for it in items[:limit]:
            print(f"  - {it}")
        if len(items) > limit:
            print(f"  ... {len(items) - limit} more")

    section("Parse problems", rep["parse_problems"])
    section("Dangling references", rep["dangling_references"])
    section("Individuals with no family link", rep["unlinked_individuals"])
    section("Families with no members", rep["empty_families"])
    section("Assertions without SOUR citation", rep["uncited_assertions"])
    section("Possibly living (no death, born inside privacy window)", rep["possibly_living"])
    if d:
        print("\n== Diff vs baseline ==")
        section("Added records", d["added"])
        section("Removed records", d["removed"])
        section("Changed records", d["changed"])
        section("New uncited assertions", d["new_uncited"])
        section("New dangling references", d["new_dangling"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("gedcom", type=Path)
    ap.add_argument("--baseline", type=Path, help="earlier version of the same file for a semantic diff")
    ap.add_argument("--privacy-years", type=int, default=100,
                    help="flag people born within this many years and without a death event (default 100)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    rep = analyze(args.gedcom, args.privacy_years)
    d = diff(analyze(args.baseline, args.privacy_years), rep) if args.baseline else None

    if args.json:
        out = {k: v for k, v in rep.items() if not k.startswith("_")}
        if d:
            out["diff"] = d
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print_report(rep, d)
    return 1 if rep["dangling_references"] else 0


if __name__ == "__main__":
    sys.exit(main())
