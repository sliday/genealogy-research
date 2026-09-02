# GEDCOM Tools (gedcom.tools) — Agent Catalog

Reviewed: 2026-09-02. Third-party site, not affiliated with this skill. Routes and tiers change; re-check https://gedcom.tools/for-agents before relying on a detail here.

A set of 22 single-purpose browser tools for `.ged` files. They repair, inspect, and reorganize a GEDCOM file. **None of them establishes a genealogical fact.** File hygiene is not proof. Everything in [gedcom-enrichment-workflow.md](gedcom-enrichment-workflow.md) still governs what may be written into a tree and on what evidence.

## How an agent may use this site

Verified 2026-09-02.

| Capability | Reality |
|---|---|
| MCP server | Does not exist. No endpoint, no package, no transport. Do not attempt an MCP connection. |
| File upload API | Does not exist. No route accepts a GEDCOM file. Parsing happens in the reader's own browser. |
| Machine-readable index | `/llms.txt` (22 tools, one sentence each) and `/llms-full.txt` (adds guarantees). Neither runs a tool. |
| Tool page fetched without a browser | Empty shell (~2.5 KB). Head is complete; body renders client-side. Findings are never in the HTTP response. |
| Markdown negotiation | Not built. `/gedcom-validator.md` and `Accept: text/markdown` both return HTML. |
| Health check | `/api/health` → `{"ok":true,"model":"openrouter/auto"}`. Says nothing about a file. |
| Feedback form rules | `/api/feedback/config` → sitekey, kinds, length bounds. |
| Unknown paths | Return `200 text/html` (SPA shell), not 404. `/api/openapi.json`, `/tools.json`, `/.well-known/ai-plugin.json` all answer 200 with the app shell. **A 200 here is not evidence a route exists.** Do not infer an API from a status code. |

So there are exactly two useful moves:

1. **Hand the person a link and a prompt.** The person opens the tool, drops the file, reads the findings back. This is the normal path.
2. **Call the code in the repository.** Each tool is a pure function `run(doc, opts, ctx)` in `src/tools/<id>/index.ts`, no DOM, no network. Only available when working inside that repository.

Never claim to have run a tool. The agent cannot execute one over HTTP.

## Privacy gate — apply before naming any tool

A GEDCOM file normally contains living people: names, birth dates, places, addresses, sometimes phone numbers and email. Skill rule 6 (protect living people) applies in full.

- The site states files are parsed in the browser and not uploaded. That promise covers the site's own parsing. **It does not cover the file entering an agent's context window.** Once the agent reads the file, the agent owns the promise.
- Some tools are LLM-backed by their own description: **Merge Conflict Arbitration** ("argues both sides ... with a language model"), and the Studio tier (**Note Structurer**, **Research Gap Planner**). `/api/health` confirms a model is configured (`openrouter/auto`).
- The site publishes **no per-tool data-flow map**. Until it does, treat the LLM-backed tools as sending record fragments off device, and say so to the person before recommending one.
- Before any tool that leaves the device, and before pasting file contents into the agent's own context: redact first (**Living Person Privatiser**) or work on a deceased-only branch (**Subtree Extractor**). Privatiser is Pro. If the person will not pay, the free answer is *do not share the file*, not *share it anyway*.

## Tool table

Tier: Free / Pro / Studio (paid tiers gate the tool; check before recommending).
Effect classes are read off the published tool descriptions, not from a machine-readable field the site publishes. Verify in the tool before trusting one.

- `reports` — read-only findings
- `writes` — produces a corrected file
- `proposes` — produces a reviewable patch the person accepts or rejects
- `advises` — produces a verdict or plan, changes nothing

### Repair a file that will not open or reads wrong

| Tool | Route | Tier | Effect | Reach for it when |
|---|---|---|---|---|
| Corrupted File Recovery | `/gedcom-file-recovery` | Free | writes | "Ancestry says my file is invalid", "RootsMagic will not open it", truncated or mangled export |
| Encoding Repair | `/gedcom-encoding-repair` | Free | writes | "Ã¼ everywhere", mojibake, broken diacritics, Cyrillic as `Ð²`, ANSEL from an old program |
| GEDCOM Validator | `/gedcom-validator` | Free | reports | Any unknown-condition file. Returns record, line, severity, and the tool that fixes each |
| File Inspector | `/inspect` | Free | reports | Need version, producing program, encoding, record counts before deciding anything |
| Format Converter | `/gedcom-converter` | Free | writes | Destination demands 7.0 or only reads 5.5.1. Lists constructs the target cannot hold |

### Fix internal structure

| Tool | Route | Tier | Effect | Reach for it when |
|---|---|---|---|---|
| Link Reciprocity Checker | `/link-reciprocity-checker` | Free | reports | One-sided FAMS, FAMC, HUSB, WIFE, CHIL pointers. Sorts each into probable duplicate, orphan, or incomplete entry |
| Broken Link Repair | `/broken-link-repair` | Pro | proposes | Pointers to records that are not there; records nothing points at |
| Impossible Fact Fixer | `/impossible-fact-fixer` | Free | proposes | "She is her own grandmother", born after mother's death, married before birth. Separates impossible from merely unusual |
| Date Normaliser | `/date-normaliser` | Pro | proposes | Dual years (1750/51), Old Style, localised or Latin month names, mixed date forms. Flags readings the digits do not settle instead of guessing |

### Identity and merging

| Tool | Route | Tier | Effect | Reach for it when |
|---|---|---|---|---|
| Duplicate Individual Finder | `/duplicate-finder` | Free | reports | "Grandma is in there twice". Distinguishes a duplicate from a child named after a dead sibling (necronym) |
| Merge Workbench | `/merge-workbench` | Pro | proposes | One pair already confirmed by evidence. Produces a single reversible patch |
| Merge Conflict Arbitration | `/merge-arbitration` | Pro | advises | One pair that will not resolve. Answers merge / do not merge / not enough evidence, plus what would settle it. **LLM-backed** |
| Determination Ledger | `/determination-ledger` | Pro | reports | Read back every merge, rejected merge, necronym verdict, confidence, and negative finding written into the file. Per `/llms-full.txt` it can also revert them |

### Understand and share

| Tool | Route | Tier | Effect | Reach for it when |
|---|---|---|---|---|
| GEDCOM Viewer | `/gedcom-viewer` | Free | reports | Browse people, families, pedigree, timeline. Shows every name tag as written |
| Relationship Calculator | `/relationship-calculator` | Free | reports | "Second cousin once removed", "how am I related to". Names kinship both directions with the parent/child chain |
| Tree Health Score | `/tree-health-score` | Free | reports | "How good is my tree". Score /100 on completeness, sourcing, consistency |
| Dialect Report | `/gedcom-dialect-report` | Free | reports | "Will Ancestry keep my custom tags". Names the producing program and which tags FamilySearch, Ancestry, MyHeritage, Gramps, WikiTree, GEDmatch drop or rewrite |
| Living Person Privatiser | `/living-person-privatiser` | Pro | writes | Before any sharing, publishing, or upload. Redacts the living, then scans output for addresses, phones, emails, leaked names |
| Subtree Extractor | `/subtree-extractor` | Free | writes | Send one branch, not the whole tree. Confirms every pointer in the output resolves inside the output |

### Research planning

| Tool | Route | Tier | Effect | Reach for it when |
|---|---|---|---|---|
| Citation Parser | `/citation-parser` | Pro | proposes | Free-text citations that should be structured SOUR records |
| Note Structurer | `/note-structurer` | Studio | proposes | Prose NOTEs hiding hypotheses, corrections, negative findings, open questions. **LLM-backed** |
| Research Gap Planner | `/research-gap-planner` | Studio | advises | "Brick wall", "where do I look next". Names records the tree implies but never cites, plus archive, record set, parish, year range. **LLM-backed** |

## Order matters

Tool order is not optional. Wrong order produces confident wrong answers.

**A file that will not open**
```
gedcom-file-recovery → gedcom-encoding-repair → inspect → gedcom-validator
```
Name matching and date parsing are both unreliable until the encoding is right. Running Duplicate Finder on a mojibake file makes "MÃ¼ller" and "Müller" different people, and the tool reports no duplicates. That is a false negative delivered in a confident tone.

**Clean up an inherited tree**
```
gedcom-validator → link-reciprocity-checker → broken-link-repair
→ duplicate-finder → merge-workbench → merge-arbitration → determination-ledger
```
Do not start at duplicate detection. Broken pointers split one person into two halves that then look like two people.

**Before uploading to another service**
```
gedcom-dialect-report → gedcom-converter (only if required) → gedcom-validator
→ living-person-privatiser (if the destination is public or shared)
```
Ask the destination first. The answer differs per service.

**Before sharing with a relative**
```
living-person-privatiser → subtree-extractor → gedcom-validator
```
Privatiser before extractor. An extract of unredacted records is still unredacted.

**Planning the next research**
```
tree-health-score → research-gap-planner → citation-parser → note-structurer
```
This sequence produces questions, not answers. Answering means going to the archive. Route the resulting questions through [source-access-catalog.md](source-access-catalog.md) and [local-databases-by-country.md](local-databases-by-country.md).

## Mutation gate

Maps to Phase 7 of [gedcom-enrichment-workflow.md](gedcom-enrichment-workflow.md).

**May be applied without asking** — these change form, not meaning:
- encoding repair, corrupted-file recovery, format conversion, validator findings that are purely structural.

**Must stop and show the person** — these change who someone was:
- any merge (Merge Workbench, Merge Arbitration);
- any change to a FAMC, FAMS, HUSB, WIFE, or CHIL pointer (Broken Link Repair);
- any deleted or quarantined record;
- any rewritten date (Date Normaliser, Impossible Fact Fixer);
- any determination accepted back into the file (Note Structurer, Determination Ledger).

Present the proposed patch, the evidence behind it, and the conflict it does not settle. A tool's confidence number ranks candidates; it does not prove identity.

## What these tools cannot settle

State this plainly whenever reporting a result:

- A duplicate finder finds records that look alike. It does not establish that two records are one person. Identity resolution is Phase 6 of the enrichment workflow, and it needs correlated evidence from records, not field similarity.
- A health score counts citations and completeness. It does not weigh evidence. A tree can score 95/100 and descend from the wrong man.
- A validator proves the file is well formed. It says nothing about whether the file is true.
- Merge Arbitration produces an argument, not a source. Its verdict is a lead under skill rule 1, exactly like a hint or an index match.

## Reporting contract

When relaying a tool's output back to a person:

1. Carry the omitted count. Where a list is capped, the result states how many findings were left out. Report that number.
2. Carry file identity. Record counts from `/inspect` plus byte size, so a later step can prove it ran on the same file. Genealogy sessions run for days across several programs.
3. Carry the record and line for every finding. The tools supply both.
4. Name the tier. Do not send someone to a Pro or Studio tool without saying it is paid.
5. Say what the tool did not do. See the section above.

## Known drift between the site's own artifacts

The page states every line is generated from the tool definition. Three mismatches found 2026-09-02, so prefer the tool page itself when a detail matters:

- **Dialect Report** — `/llms.txt` names four destinations, `/for-agents` names six (adds WikiTree, GEDmatch).
- **Date Normaliser** — `/llms-full.txt` says five calendars, `/for-agents` names none.
- **Determination Ledger** — `/llms-full.txt` says it reverts determinations, `/for-agents` says it only lists them.
