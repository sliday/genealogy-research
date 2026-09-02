# Review: https://gedcom.tools/for-agents

Date: 2026-09-02. Reviewer: genealogy-research skill maintainer view.
Scope: does page make sense for agents; what to change so agents do real genealogy work.

Verified live: `/for-agents`, `/llms.txt`, `/llms-full.txt`, `/api/health`,
`/api/feedback/config`, `/robots.txt`, `/sitemap.xml`, `/gedcom-validator` (shell, 2563 bytes).

---

## 1. Verdict

Page makes sense. Better than most agent pages. Three things right:

- One copyable prompt per tool. Each prompt names address, job, and required return shape.
- "What does not exist" section. Names missing MCP server, missing upload route, empty SPA shell,
  missing markdown negotiation. Rare honesty. Stops agents inventing an API.
- "Before you ask for the file" section. Puts living-person privacy before the file request.

One structural gap. Page teaches agent to **operate one tool**. Page does not teach agent to
**run a genealogy session**. No order, no preconditions, no stop rule, no state carried between
tools. Agent reading page can pick a tool. Agent cannot plan a repair or a research pass.

Everything below closes that gap.

---

## 2. Highest-value changes

Ranked. Top three matter most.

### 2.1 Say which tools send data off device

**Problem.** Page headline: "tools run in a browser and parse your file locally."
`/api/health` returns `{"ok":true,"model":"openrouter/auto"}`. Merge Conflict Arbitration
described as arguing "with a language model". Note Structurer, Research Gap Planner marked Studio.
So some tools plainly reach a model. Page never separates them.

**Why bad.** Agent will repeat the local-only promise to a person holding living-relative names,
birth dates, addresses. GEDCOM files carry that data by default. Promise then breaks silently.

**Fix.** Add per-tool field. Two values, no hedging:

| value | meaning |
|---|---|
| `local-only` | parse and result never leave browser |
| `sends-to-model` | fragment leaves device |

For every `sends-to-model` tool state: exact fragment sent (whole record? two records? note text
only?), provider, retention, and whether living people are stripped first. One sentence each.

Add global line to "What an agent can do here":

> Not every tool is local. Check the data-flow field before you promise anything. Where a tool
> sends a fragment to a model, say which fragment, and offer the local-only tool that answers a
> smaller version of the same question.

### 2.2 Add ordered workflows, not only a tool list

**Problem.** The 22 tools have hard dependencies. Order is invisible.

Concrete failure: agent runs Duplicate Individual Finder on a mojibake file. "MÃ¼ller" and
"Müller" no longer match. Agent reports "no duplicates". Wrong answer, confident tone.
Encoding Repair must run first. Nothing on the page says so.

**Fix.** Add section "Recipes". Named job, ordered tools, one line why the order holds.
Draft set below. Copy is verbatim, not telegraphic.

**Recipe: the file will not open**
```
1. /gedcom-file-recovery   rebuild the file so a parser accepts it
2. /gedcom-encoding-repair fix the charset before anything reads a name
3. /inspect                confirm version, producer, record counts
4. /gedcom-validator       list what is still wrong
Order matters: name matching and date parsing are both wrong until the encoding is right.
```

**Recipe: clean up an inherited tree**
```
1. /gedcom-validator          the full problem list
2. /link-reciprocity-checker  one-sided FAMS, FAMC, HUSB, WIFE, CHIL pointers
3. /broken-link-repair        pointers to records that are not there
4. /duplicate-finder          people entered twice
5. /merge-workbench           merge one confirmed pair, as one reversible patch
6. /merge-arbitration         only for the pairs step 5 could not settle
7. /determination-ledger      read back every decision now written into the file
Do not start at step 4. Broken pointers make two halves of one person look like two people.
```

**Recipe: before I upload to another service**
```
1. /gedcom-dialect-report  which of my custom tags the destination drops or rewrites
2. /gedcom-converter       convert only if the destination needs the other version
3. /gedcom-validator       confirm the converted file is still sound
4. /living-person-privatiser if the destination is public or shared
Name the destination first. The answer differs for FamilySearch, Ancestry, MyHeritage,
Gramps, WikiTree and GEDmatch.
```

**Recipe: before I share with a relative**
```
1. /living-person-privatiser  redact the living
2. /subtree-extractor         send one branch, not the whole tree
3. /gedcom-validator          confirm every pointer in the extract still resolves
Run the privatiser before the extractor, not after. An extract of unredacted records is
still unredacted.
```

**Recipe: plan the next research**
```
1. /tree-health-score       where the tree is thin
2. /research-gap-planner    the records the tree implies but never cites
3. /citation-parser         turn the free-text citations already there into structured sources
4. /note-structurer         pull the hypotheses and corrections buried in prose notes
This recipe finds questions. It does not answer them. Answering means going to the archive.
```

### 2.3 Add a mutation gate

**Problem.** Prompts are output-shaped ("tell me..."). None says whether tool changes the file,
and none says where the agent must stop and ask a person.

Merge Workbench prompt currently instructs agent to "merge them into one record". Merging two
people is a genealogical conclusion. Under the Genealogical Proof Standard a conclusion needs
correlated evidence and written reasoning. An agent should never merge unasked.

**Fix.** Per-tool field `mutates`: `reports` | `proposes-patch` | `writes-file`.
Then one global rule block:

> An agent may accept, without asking: encoding repair, structural recovery, format conversion,
> and validator findings. These change form, not meaning.
>
> An agent must stop and show the person: any merge, any change to a parent, child or spouse
> pointer, any deleted record, any rewritten date, any accepted determination. These change who
> someone was. Show the proposed patch, the evidence behind it, and the conflict it does not
> settle. Let the person answer.

### 2.4 Add trigger phrases per tool

**Problem.** Prompts written in tool language. People arrive in their own language. Agent must
map one to the other with no help.

**Fix.** One line per tool: "reach for this when the person says ...". Real phrases:

| tool | person says |
|---|---|
| Encoding Repair | "Ã¼ everywhere", "mojibake", "the accents are broken", "Ð² Ñ‚Ñ€ÐµÐµ" |
| Corrupted File Recovery | "Ancestry says my file is invalid", "RootsMagic will not open it" |
| Dialect Report | "will Ancestry keep my custom tags", "made in PAF/Legacy/FTM/Gramps" |
| Format Converter | "it wants GEDCOM 7", "my program only reads 5.5.1" |
| Duplicate Finder | "grandma is in there twice", "same person twice" |
| Merge Arbitration | "are these two the same man" |
| Relationship Calculator | "second cousin once removed", "how am I related to" |
| Impossible Fact Fixer | "she is her own grandmother", "born after her mother died" |
| Date Normaliser | "1750/51", "Old Style", "dates in Polish/Latin/Cyrillic" |
| Living Person Privatiser | "is it safe to share", "my father is still alive" |
| Research Gap Planner | "brick wall", "where do I look next", "stuck on my great-grandfather" |
| Citation Parser | "my sources are just pasted text" |
| Tree Health Score | "how good is my tree" |

Include the misspellings and the non-English words. Genealogy users type them.

---

## 3. Prompt-level fixes, tool by tool

Only tools needing change. Proposed copy verbatim.

### Research Gap Planner
Current prompt returns archive, record set, parish, year range. Good. Two things missing.

Add negative-result vocabulary. Agents report "no record exists" after one search. Wrong, and
in genealogy it is the classic error.

> Use https://gedcom.tools/research-gap-planner to find the records my tree implies but does not
> cite, and tell me how much of the file depends on each, and the archive, record set, parish and
> year range to search. Where a gap sits in a jurisdiction with no online index, say so and name
> the physical repository. When a search returns nothing, report it as not indexed, not online,
> coverage unknown, or not searched. Never report it as absent.

### Citation Parser
Add durable-identifier demand. A URL alone is not a citation; links rot.

> Use https://gedcom.tools/citation-parser to read the archive identifiers out of my free-text
> citations, and tell me the source record it proposes for each, with the structured fields and
> the resolvable link. Keep the repository call number, fonds, film, volume, page, act or
> certificate number and image number where the text carries them. A link on its own is not a
> citation.

### Date Normaliser
Page hides detail that `/llms-full.txt` carries ("five calendars"). Name them. Name the traps.

> Use https://gedcom.tools/date-normaliser to rewrite the dates in my GEDCOM into the standard
> form and tell me every reading the digits do not settle, which it flags instead of guessing.
> Cover dual years such as 1750/51, Julian and Gregorian, localised and Latin month names, and
> the modifiers ABT, BEF, AFT, CAL, EST and BET. Say which calendar each converted date came from.

### Dialect Report
Best-selling answer on the site, weakest framing. Split by destination.

> Use https://gedcom.tools/gedcom-dialect-report to name the program that wrote my file and list
> every custom tag, then tell me what <destination> specifically drops or rewrites, and what I
> lose if I let it. Ask me the destination first.

### Tree Health Score
Add a limit line. Otherwise agent reports 92/100 as "your tree is accurate".

> A score here measures file hygiene: how complete, how sourced, how internally consistent.
> It does not measure whether the tree is true. A fully sourced tree can cite the wrong people.

### Determination Ledger
Prompt lists decisions only. `/llms-full.txt` says the tool also reverts them. Agent reading the
page misses that. Add the revert.

---

## 4. Missing global section: what this site cannot settle

Suggest new short section. Protects users from over-claiming agents.

> These tools govern the file. They check that it parses, that its pointers resolve, that its
> dates are possible, that its people are not entered twice, and that the living are not exposed.
> None of them checks a fact against a record. A duplicate finder finds duplicates, not identity.
> A health score counts citations, it does not weigh them. Proof still comes from the archive.

---

## 5. Machine-surface defects found

Small, real, cheap to fix.

1. **Soft 404 on every unknown path.** `/api/openapi.json`, `/api/tools`, `/api/llm`,
   `/.well-known/ai-plugin.json`, `/api/chat` — all return `200 text/html` (SPA shell).
   Agent probing for an API cannot tell missing from present. Some agents will then invent one.
   Fix: real 404 for unknown `/api/*`. Page already promises "no MCP server"; the server should
   say the same.

2. **Prompts are not machine-readable.** The 22 prompt lines exist only in the rendered SPA.
   Page itself states body is not in the response. So the artifact most useful to an agent is the
   one an agent cannot read without a browser. Fix: publish `/for-agents.txt` (or extend
   `/llms-full.txt`) with the same generated lines, plus the recipes.

3. **`/llms.txt` does not link `/for-agents`.** Add it. Add the recipes too.

4. **Generated artifacts have drifted.** Page claims "Every line is generated from the tool
   definition." Three mismatches say otherwise:
   - Dialect Report: `/llms.txt` names 4 destinations, `/for-agents` names 6 (adds WikiTree,
     GEDmatch).
   - Date Normaliser: `/llms-full.txt` says "five calendars", `/for-agents` says none.
   - Determination Ledger: `/llms-full.txt` says it reverts, `/for-agents` says it only lists.
   Fix: single source, one generator, all three outputs.

5. **No structured tool metadata.** Suggest `/tools.json`: per tool `id`, `url`, `tier`,
   `mutates`, `data_flow`, `requires` (prerequisite tool ids), `inputs`, `outputs`,
   `trigger_phrases`. This is the change that turns a list into something an agent can plan over.
   Everything in section 2 becomes free once this file exists.

6. **`/api/health` leaks a model name into a local-first product.** `openrouter/auto` tells an
   agent a model is configured but not which tools use it. Either drop the field or, better,
   extend it to the per-tool data-flow map from 2.1.

---

## 6. What to keep unchanged

- "What does not exist" section. Keep the tone. Keep the flat refusal to imply an MCP server.
- The omitted-count contract ("where a list is capped the result carries the omitted count").
  Extend it: ask agent to also carry file identity (record counts from `/inspect`, byte size)
  so a later step proves it ran on the same file.
- Privacy section placement, before the file request. Only strengthen it: name Living Person
  Privatiser as a precondition for `sends-to-model` tools, and note it is Pro, so the free path
  is "do not share the file".

---

## 7. Implementation order for the other agent

1. `/tools.json` with `mutates`, `data_flow`, `requires`, `trigger_phrases`. Everything else reads it.
2. Data-flow disclosure per tool (2.1). Highest trust value.
3. Recipes section (2.2).
4. Mutation gate block (2.3).
5. Trigger phrases into the page (2.4).
6. Prompt rewrites (section 3).
7. `/for-agents.txt`, real 404s, generator drift fix (section 5).
