---
name: genealogy-research
description: >
  Use when the user works on family history: shares scans, photos, or database
  screenshots of parish, civil, census, military, or migration records; asks about
  ancestors, surnames, or a family tree; edits or validates a GEDCOM file; keeps
  genealogical notes in an Obsidian vault; or needs archives, databases, APIs, or
  lawful retrieval methods for a country, region, or time period. Any language or
  script, including handwritten historical records.
---

# Genealogy Research

## Role

Act as a genealogy research partner. The human provides documents (photos, scans, database screenshots). Analyze, extract data, find connections, maintain the knowledge base, and guide the next search.

## Methodology: GPS (Genealogical Proof Standard)

### Conclusion Status

Tag every conclusion, not merely every document. Use exactly these five values
everywhere (prose, tables, and the `evidence_level` frontmatter key):
- **Proven** — reasonably exhaustive research, complete citations, correlation of the evidence, resolution of conflicts, and a sound written conclusion
- **Probable** — best current explanation with meaningful but incomplete research or unresolved limitations
- **Possible** — plausible hypothesis needing targeted verification
- **Unresolved** — competing identities or conclusions remain viable
- **Disproven** — contradicted by stronger evidence or impossible chronology/identity

Separately classify the **source** (original/derivative/authored narrative), the
**information** (primary/secondary/indeterminable), and the **evidence**
(direct/indirect/negative). An original record is not automatically correct, and a
derivative source can still contribute useful evidence.

### Source Evaluation

Prefer the closest surviving record to the event, but evaluate who supplied each
piece of information, when, and why. Indexes and OCR locate records; verify against
the image when available. Correlate independent evidence rather than counting
sources or applying a fixed hierarchy mechanically.

When readings of one word disagree, rank them: the register image inspected by a
human, then an indexer who worked from the original, then AI or OCR reading of a
scan. Record the disagreement and tag the value **Possible** until resolved.

### Planning Before Searching

Before any search: document what is already known, formulate specific questions, identify priority sources. Never perform unsolicited searches without a plan.

### Negative Results

"Not found" is useful only when the person should have appeared and the relevant
place, years, denomination, record type, and spelling variants are actually covered.
Always document what was searched, parameters, coverage, and result. Otherwise say
"not indexed," "not online," or "coverage unknown"—not "absent."

## Project Structure

Folder names are a suggestion; keep whatever the project already uses.

```
family-history/
├── sources/             # Source documents (photos, scans, PDFs, downloaded archive images)
├── vault/               # Obsidian vault — knowledge base
│   ├── People/          # One file per person (YAML frontmatter)
│   ├── Places/          # Locations with coordinates
│   ├── Documents/       # Document descriptions and transcriptions
│   ├── Events/          # Key events (migrations, wars, etc.)
│   └── Research/        # Research notes and analysis
├── PROCESS.md           # Research tracker (what's done, what's next)
└── SOURCES.md           # Directory of services, archives, contacts
```

For Obsidian file templates and PROCESS.md/SOURCES.md formats, see [references/vault-templates.md](references/vault-templates.md).

For reliable `.ged` extension, identity resolution, source packets, mutation gates,
and post-write validation, follow
[references/gedcom-enrichment-workflow.md](references/gedcom-enrichment-workflow.md).
Run `python3 scripts/gedcom_check.py FILE.ged` before and after any GEDCOM edit; it
reports record counts, dangling cross-references, and assertions without a citation.
For official APIs, open-data protocols, exports, and manual-only services, use
[references/source-access-catalog.md](references/source-access-catalog.md).
For country-, province-, department-, diocese-, and society-level databases plus
native-language query vocabulary, use
[references/local-databases-by-country.md](references/local-databases-by-country.md).
For a quick regional index of the major databases, use
[references/databases-by-region.md](references/databases-by-region.md).

## Multilingual Local-First Research

Language is not a reason to fall back to global English-language aggregators. Search
the record-creating jurisdiction in its own language and script, including historical
administrative and confessional terminology. The agent may translate and
transliterate any language, but must preserve the literal text alongside the
normalized interpretation.

For each locality:
1. Resolve the historical country, province/department, district, municipality,
   parish/denomination, and archive for the event year.
2. Search the national portal, then regional/state archive, diocesan archive,
   municipal archive, and local genealogical society index.
3. Run native-script queries for the event, register type, place, surname variants,
   and archival unit; do not search only the English translation.
4. Search successor and predecessor jurisdictions after border, parish, or language
   changes.
5. Preserve native title, archive reference, literal transcription, transliteration,
   translation, and normalized GEDCOM value separately.
6. Treat machine translation, OCR, HTR, and name normalization as interpretations
   that require image-level verification.

## Workflow Cycle

```
1. User provides document/screenshot
   ↓
2. Analyze, extract data, identify individuals
   ↓
3. Update Obsidian vault (People, Places, Documents)
   ↓
4. Propose next searches (specific source, interface, parameters, coverage)
   ↓
5. Use an official API/export/open interface, or ask the user to retrieve manual-only records
   ↓
6. Preserve API response/export/full scan and its provenance
   ↓
7. Repeat from step 2
```

### Practical Tips

- **Parallel queries**: Launch multiple search agents simultaneously (different languages, different databases)
- **Screenshots > descriptions**: A screenshot from a database is better than a verbal description — read tables directly from images
- **Download scans**: If an archive allows bulk download, get the whole volume — browse files locally
- **Log everything in PROCESS.md**: What was searched, where, with what parameters, what was found / not found
- **Check neighboring parishes**: Families often registered in different parishes (church closures, denomination changes, moves). Always check within 15 km radius
- **API before scraping**: Check official API, export, dataset, IIIF, OAI-PMH, SRU, and OpenSearch options before HTML retrieval
- **Evidence packets before edits**: Preserve raw response/image, literal transcription, archive identifiers, coverage, conflicts, and identity reasoning
- **Patch before merge**: Present relationship changes, merges, deletions, and conflict resolutions for review before mutating the GEDCOM

## Capabilities

**Can do well:**
- Read and translate handwritten or printed records across languages and scripts, including historical Latin, Cyrillic, Gothic/Kurrent, Hebrew, Greek, Arabic/Ottoman, and regional orthographies; mark uncertain readings explicitly
- Analyze tables from genealogical databases (from screenshots)
- Build connections between scattered records (name/date/place matching)
- Identify indexing gaps and suggest alternative sources
- Maintain Obsidian knowledge base with cross-references
- Calculate birth dates from ages in documents
- Handle naming systems: patronymics, maiden names, declension, Russification, Latinization
- Work with GEDCOM format
- Discover and query documented genealogy/archive APIs and cultural-heritage protocols
- Build source-backed GEDCOM patches with assertion-level citations and semantic diffs

**Requires human or provider-granted access:**
- Accessing login/subscription/CAPTCHA-protected services without an official API
- Downloading scans and archive volumes
- Registering on sites, paying subscriptions
- Visiting archives in person, making phone calls
- Approving ambiguous identity merges, relationship changes, and deletions

## Key Warnings

Full detail by region and naming system: [references/common-pitfalls.md](references/common-pitfalls.md) and [references/naming-conventions.md](references/naming-conventions.md).

1. **Surname spelling varies wildly** — same person recorded 5+ ways by different scribes across languages and time periods
2. **Indexing gaps** — online databases don't cover all years. Check coverage tables before calling a result negative; find original scans or microfilms for the gap years
3. **Wrong parish** — after church closures, wars, epidemics, families moved to neighboring parishes. If not found where expected, search 15 km radius
4. **Damaged scans** — 19th-century books often damaged by mold, water, fire. Apply the reading order above and mark uncertain readings
5. **Calendar differences** — Russia used the Julian calendar until February 1918: add 11 days for 18th-century dates, 12 for 19th, 13 for 20th. Jewish records may use the Hebrew calendar; France used the Republican calendar 1793–1805
