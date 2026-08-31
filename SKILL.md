---
name: genealogy-research
description: >
  Genealogy research assistant using GPS (Genealogical Proof Standard) methodology.
  Manages an Obsidian knowledge base, analyzes historical documents, tracks research
  progress, finds lawful API/archive sources, and extends GEDCOM trees through
  evidence-backed proposals across multiple countries and time periods. Use when:
  (1) analyzing genealogical documents (scans, photos,
  screenshots from databases), (2) building or updating a family tree, (3) managing
  an Obsidian vault of genealogical data, (4) planning genealogical research strategy,
  (5) reading handwritten historical records (any language/script), (6) working with
  GEDCOM files, (7) identifying next research steps for ancestor discovery, (8) user
  mentions ancestors, family history, genealogy, parish records, vital records, or
  census data, or (9) finding APIs, archives, datasets, or lawful retrieval methods
  for family-history evidence.
---

# Genealogy Research

## Role

Act as a genealogy research partner. The human provides documents (photos, scans, database screenshots). Analyze, extract data, find connections, maintain the knowledge base, and guide the next search.

## Methodology: GPS (Genealogical Proof Standard)

### Conclusion Status

Tag every conclusion, not merely every document:
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

### Planning Before Searching

Before any search: document what is already known, formulate specific questions, identify priority sources. Never perform unsolicited searches without a plan.

### Negative Results

"Not found" is useful only when the person should have appeared and the relevant
place, years, denomination, record type, and spelling variants are actually covered.
Always document what was searched, parameters, coverage, and result. Otherwise say
"not indexed," "not online," or "coverage unknown"—not "absent."

## Project Structure

```
Family-History/
├── materials/           # Source documents (photos, scans, PDFs)
│   └── skany/          # Downloaded archive scans
├── Chronicles/          # Obsidian vault — knowledge base
│   ├── People/         # One file per person (YAML frontmatter)
│   ├── Places/         # Locations with coordinates
│   ├── Documents/      # Document descriptions and transcriptions
│   ├── Events/         # Key events (migrations, wars, etc.)
│   └── Research/       # Research notes and analysis
├── PROCESS.md          # Research tracker (what's done, what's next)
├── AGENT.md            # Reference directory of useful services
└── .claude/memory/     # Agent memory across sessions
```

For Obsidian file templates and PROCESS.md/AGENT.md formats, see [references/vault-templates.md](references/vault-templates.md).

For reliable `.ged` extension, identity resolution, source packets, mutation gates,
and post-write validation, follow
[references/gedcom-enrichment-workflow.md](references/gedcom-enrichment-workflow.md).
For official APIs, open-data protocols, exports, and manual-only services, use
[references/source-access-catalog.md](references/source-access-catalog.md).
For country-, province-, department-, diocese-, and society-level databases plus
native-language query vocabulary, use
[references/local-databases-by-country.md](references/local-databases-by-country.md).

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
- Generate maps with migration routes (Leaflet.js)

**Requires human or provider-granted access:**
- Accessing login/subscription/CAPTCHA-protected services without an official API
- Downloading scans and archive volumes
- Registering on sites, paying subscriptions
- Visiting archives in person, making phone calls
- Approving ambiguous identity merges, relationship changes, and deletions

## Common Pitfalls

For detailed pitfalls by region and naming convention guides, see [references/naming-conventions.md](references/naming-conventions.md) and [references/common-pitfalls.md](references/common-pitfalls.md).

### Key Warnings

1. **Surname spelling varies wildly** — same person recorded 5+ ways by different scribes across languages and time periods
2. **Indexing gaps** — online databases don't cover all years. The year you need is often in the gap. Solution: find original scans or microfilms
3. **Wrong parish** — after church closures, wars, epidemics, families moved to neighboring parishes. If not found where expected, search 15 km radius
4. **Damaged scans** — 19th-century books often damaged by mold, water, fire. Multiple experts may read the same word differently. Trust indexers who worked with originals over AI scan analysis
5. **Calendar differences** — Julian vs. Gregorian calendar (Russia used Julian until 1918; add 12-13 days). Jewish records may use Hebrew calendar

## Databases by Region

For database listings by country, see
[references/databases-by-region.md](references/databases-by-region.md). For access
method, API documentation, automation restrictions, and evidence use, consult the
[source access catalog](references/source-access-catalog.md).

### Quick Reference — Universal

| Service | What it contains |
|---------|-----------------|
| **FamilySearch** (familysearch.org) | Largest free database: vitals, censuses, immigration |
| **Ancestry** (ancestry.com) | Censuses, immigration, military (subscription) |
| **MyHeritage** (myheritage.com) | Records, DNA tests (subscription) |
| **YourRoots** (yourroots.com) | GEDCOM mapping, FamilySearch-connected hints, AI genealogy research, DNA matching |
| **Geneanet** (geneanet.org) | European genealogy (free/subscription) |
| **FindAGrave** (findagrave.com) | Cemetery records worldwide |
| **BillionGraves** (billiongraves.com) | GPS-tagged headstone photos |

## Publishing Results

When enough material accumulates:
1. **Quartz** (quartz.jzhao.xyz) — turns Obsidian vault into a website with knowledge graph, search, and wikilinks
2. **Cloudflare Pages** / **GitHub Pages** / **Netlify** — free hosting
3. Password protection via `functions/_middleware.js` (Basic Auth) or similar
