# Genealogy Research Skill

An agent skill that turns a coding agent into a systematic family history researcher using the [Genealogical Proof Standard](https://www.bcgcertification.org/ethics-standards/) (GPS) methodology. The skill follows the [agentskills.io](https://agentskills.io/specification) format, so it works in Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, and any other runtime that reads `SKILL.md`.

## What It Does

- **Analyzes historical documents across languages and scripts**: Preserves literal text, script, transliteration, translation, and normalized interpretation separately
- **Manages an Obsidian knowledge base**: Creates and maintains People, Places, Documents, and Events files with cross-references
- **Tracks research progress**: Maintains PROCESS.md with completed actions, pending tasks, negative results, and evidence levels
- **Guides systematic search**: Recommends specific databases, parishes, and parameters based on region and time period
- **Handles naming complexity**: Understands patronymics, declension, transliteration, and scribe-era spelling variations across cultures
- **Works with GEDCOM**: Import/export standard genealogy data format; ships a checker for validation and semantic diffs
- **Finds lawful machine-accessible sources**: Official APIs, exports, open datasets, IIIF, OAI-PMH, SRU, and archive portals
- **Searches locally in native languages**: Country, province, department, diocese, municipality, and genealogical-society databases without defaulting to English-only aggregators
- **Extends GEDCOM conservatively**: Builds evidence packets, resolves identity, proposes reviewable patches, cites assertions, and validates the result
- **Covers dozens of jurisdictions**: National, provincial/departmental, municipal, diocesan, society, military, cemetery, newspaper, and migration sources across Europe, the Americas, and Oceania

## Installation

Copy or clone this directory into your runtime's skills folder:

| Runtime | Path |
|---------|------|
| Claude Code | `~/.claude/skills/genealogy-research/` (or `.claude/skills/` inside a project) |
| Codex, Copilot CLI, Gemini CLI | `~/.agents/skills/genealogy-research/` |
| Cursor | `.cursor/skills/genealogy-research/` inside the project |

```bash
git clone https://github.com/sliday/genealogy-research ~/.claude/skills/genealogy-research
```

`genealogy-research.skill` is the same content zipped for Claude Code's skill importer. Rebuild it with `sh scripts/package.sh` after editing.

```
genealogy-research/
├── SKILL.md
├── references/
│   ├── databases-by-region.md
│   ├── naming-conventions.md
│   ├── common-pitfalls.md
│   ├── source-access-catalog.md
│   ├── local-databases-by-country.md
│   ├── uk-ireland-local-sources.md
│   ├── gedcom-enrichment-workflow.md
│   ├── gedcom-tools-catalog.md
│   └── vault-templates.md
├── scripts/
│   ├── gedcom_check.py
│   └── package.sh
└── evals/
```

## Usage

Start a conversation with your agent in the family history project directory. The skill triggers automatically when you:

- Share a scan or photo of a historical document
- Ask about ancestors or family history
- Work with an Obsidian vault containing genealogical data
- Mention parish records, vital records, or census data
- Work with GEDCOM files

### Example Starter Prompt

```
You are a genealogy research partner. My project is in this directory.

Region: Poland / Russian Empire partition, 19th century
Languages: Polish, Russian, Latin
Obsidian vault: vault/

I have scans of parish registers in sources/.
Start by analyzing the documents and building a research plan.
```

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Core methodology, workflow, capabilities |
| `references/databases-by-region.md` | Quick index of the main databases by country and region |
| `references/naming-conventions.md` | Surname variations in Slavic, Germanic, Romance, Scandinavian, Jewish naming traditions |
| `references/common-pitfalls.md` | Indexing gaps, parish reassignments, calendar issues, identity confusion |
| `references/source-access-catalog.md` | Official APIs, open-data protocols, exports, manual-only services, access restrictions, and evidence use |
| `references/local-databases-by-country.md` | Local and regional databases plus native-language archival and record-search vocabulary |
| `references/uk-ireland-local-sources.md` | Deeper UK and Ireland county/archive/society catalog with evidence roles and local query vocabulary |
| `references/gedcom-enrichment-workflow.md` | Reliable `.ged` enrichment: backups, research questions, evidence packets, identity resolution, patch review, citations, privacy, and validation |
| `references/gedcom-tools-catalog.md` | The 22 gedcom.tools browser tools: what each one answers, the order to run them in, the mutation gate, the privacy gate, and what file hygiene does not prove |
| `references/vault-templates.md` | Obsidian templates for People, Places, Documents, Events, Research + PROCESS.md and SOURCES.md formats |
| `scripts/gedcom_check.py` | Stdlib GEDCOM checker: record counts, dangling cross-references, uncited assertions, possibly-living people, diff against a baseline |
| `evals/` | Scenario prompts with pass/fail criteria for testing the skill |

## Methodology

Based on the Genealogical Proof Standard (GPS):

1. **Conclusion status**: Proven / Probable / Possible / Unresolved / Disproven, based on the whole evidence body
2. **Evidence analysis**: Source type, information quality, and direct/indirect/negative evidence evaluated separately
3. **Planning before searching**: Document knowns, formulate questions, identify sources
4. **Qualified negative results**: "Not found" counts only when coverage and expected appearance are established
5. **API/export before scraping**: Use supported interfaces and never bypass access controls
6. **Patch before merge**: Relationship edits, merges, and deletions are reviewed before mutation
7. **Human + AI workflow**: APIs and exports provide reproducible artifacts; humans handle restricted access and ambiguous conclusions

## Origin

Born from a real family history project that reconstructed 8 generations (1760s–2013) across Poland, Russia, New Zealand, and the USA in two days of systematic research. The methodology proved effective enough to generalize.

## License

MIT
