# Common Pitfalls in Genealogy Research

Reviewed: 2026-09-01.

## Table of Contents
- [Document and Record Issues](#document-and-record-issues)
- [Database and Indexing Issues](#database-and-indexing-issues)
- [Geographic and Jurisdictional Issues](#geographic-and-jurisdictional-issues)
- [Calendar and Dating Issues](#calendar-and-dating-issues)
- [Identity Confusion](#identity-confusion)
- [Research Process Mistakes](#research-process-mistakes)

---

## Document and Record Issues

### Damaged or Illegible Scans
- 19th-century books often damaged by mold, water, fire, insects
- Multiple experts may give different readings of the same word
- **Guideline:** Rank readings: register image inspected by a human, then an indexer who worked from the original, then AI/OCR reading of a scan. If readings disagree, mark the value "Possible" and note the ambiguity

### Language Switches in Records
- Same parish may switch languages across time periods:
  - Latin → Russian (after 1868 in Russian partition of Poland)
  - Latin → German (in Prussian partition)
  - Latin → Polish (after 1918 independence)
- A single record may mix languages (Latin template, local-language names)

### Margin Notes and Corrections
- Later additions (marriage notes on birth records, death dates) may be in different handwriting
- Cross-references ("see act #X") are extremely valuable — always follow them
- Corrections may indicate errors in the original entry

### Missing Pages
- Pages torn, cut, or missing from bound volumes
- Page numbering gaps indicate missing content
- Microfilm may skip pages if the operator missed them

---

## Database and Indexing Issues

### Indexing Gaps
- **Most critical pitfall.** Online databases rarely cover 100% of years for any parish
- Typical pattern: indexed 1808–1844, then 1851, then 1862 — the years in between are unindexed
- **Always check date coverage** before concluding "not found"
- Solution: find original scans (Skanoteka, Szukaj w Archiwach, FamilySearch microfilms) and browse manually

### Discovery Result Mistaken for Evidence
- Search hints, user trees, indexes, OCR, and AI transcriptions identify candidates; they do not by themselves prove identity or relationship
- Preserve the provider's record ID and collection metadata, then inspect the underlying image or archival record when available
- Attach the citation to the exact GEDCOM assertion it supports, not merely to the person

### Undocumented Endpoint Mistaken for Permission
- A JSON request visible in browser developer tools is not automatically a supported public API
- Prefer official APIs, exports, bulk datasets, IIIF, OAI-PMH, SRU, and OpenSearch
- Do not bypass login, CAPTCHA, paywalls, rate limits, robots controls, or provider restrictions
- For subscription/manual-only services, use the user's browser or official download and analyze the artifact locally

### Indexer Errors
- Volunteer indexers make mistakes: wrong names, transposed digits, misread letters
- **Never trust an index as the final source** — always verify against the scan when available
- Common index errors: confusing similar letters (s/f in old handwriting), wrong year, wrong act number

### Duplicate Entries
- Same record may appear in multiple databases with conflicting data
- Church copy and civil copy of the same event may differ
- Always cite which specific copy you used

### Search Limitations
- Many databases don't support fuzzy/wildcard search
- Diacritical marks: searching "Łukasiuk" won't find "Lukasiuk" in some systems
- **Tip:** Search with and without diacritics, try multiple spelling variants

---

## Geographic and Jurisdictional Issues

### Parish vs. Civil Registration
- Church parish boundaries ≠ civil administrative boundaries
- A village may belong to one parish but a different gmina/volost
- After a church closes, the village may be reassigned to a distant parish

### Church Closures and Reassignments
- Political events cause mass parish closures:
  - Poland 1867: Russian authorities closed many Catholic parishes after January Uprising
  - German Kulturkampf (1870s): affected Catholic parishes in Prussian partition
- Families then registered in neighboring parish — search 15 km radius
- The "wrong" parish may become the right one for a specific time period

### Border Changes
- Borders in Central/Eastern Europe shifted dramatically:
  - Partitions of Poland (1772, 1793, 1795)
  - Napoleon's Duchy of Warsaw (1807–1815)
  - Congress Poland under Russia (1815–1918)
  - Interwar period (1918–1939)
  - WWII occupation and post-war shifts
- Same village may have Polish, Russian, German, and Austrian records depending on period
- **Always determine which jurisdiction the village was in for the specific year**

### Place Name Changes
- Villages renamed across regimes: Polish → Russian → German → Polish again
- Mergers: small villages absorbed into larger ones
- Transliteration variations: Dziadkowice → Дзядковице → Dziadkowize
- **Use historical gazetteers** (Słownik Geograficzny Królestwa Polskiego, Volostnoj Atlas) to map old names to modern ones

### Multiple Places with Same Name
- "Korzeniówka" may exist in 5+ locations — verify the correct one by checking parish/powiat/gubernia
- Cross-reference with surrounding village names mentioned in documents

---

## Calendar and Dating Issues

### Julian vs. Gregorian Calendar
- Russia used Julian calendar until **February 14, 1918** (= Feb 1 Julian)
- Difference: +11 days (18th century), +12 days (19th century), +13 days (20th century)
- Church records in Russian Empire: Julian dates
- Civil records in Austrian Empire: Gregorian dates
- **When converting, note which calendar in your records**

### Hebrew Calendar
- Jewish records may use Hebrew calendar dates
- Conversion tools: hebcal.com
- Year 5700 (Hebrew) ≈ 1939/1940 CE

### French Republican Calendar
- Used 1793–1805 in France and occupied territories
- Records from this period use month names like Vendémiaire, Brumaire, etc.

### Estimated Dates
- Ages in documents are often approximate (± 2–5 years common)
- "Age 60" in a death record from 1909 means born ~1847–1851, not exactly 1849
- Cross-reference multiple documents to narrow birth year range

---

## Identity Confusion

### Same Name, Different Person
- Common names (Jan Kowalski, Ivan Petrov) appear repeatedly in the same parish
- **Distinguish by:** parents' names, spouse name, age, village, witnesses
- Build a cluster of evidence, not a single record

### Different Name, Same Person
- See [naming-conventions.md](naming-conventions.md) for full details
- One person may appear under maiden name, married name, widow's name, nickname
- Spelling variants across documents make the same person look like different people

### Godparents and Witnesses ≠ Relatives (Usually)
- Godparents were often neighbors or friends, not necessarily blood relatives
- BUT patterns emerge: if the same person appears as godparent for all children, they're likely close family
- Witnesses at marriages often are relatives — note their surnames

### Children of Multiple Marriages
- Widowers/widows frequently remarried
- Children from first and second marriages share a father (or mother) but not the other parent
- In records: "first wife" (priore matrimonio) vs. "second wife" — track carefully

---

## Research Process Mistakes

### Confirmation Bias
- Wanting to find a connection makes you see connections that aren't there
- **Every identification must have evidence.** "Same first name in same village" is not proof — it's a hypothesis
- Always consider: could this be a different person?

### Automated Same-Person Merges
- A name/date similarity score can rank candidates but cannot prove identity
- Require correlation across place, chronology, relatives/associates, occupation/address/religion, and record identifiers
- Treat incompatible parents/spouses, impossible chronology, or irreconcilable simultaneous residences as hard contradictions
- Present merges, relationship changes, and deletions as reviewable patches before editing the GEDCOM

### Ignoring Negative Evidence
- "Not found" is not nothing — it's data that eliminates possibilities
- Document every zero-result search: database, collection, parameters, date range, place, denomination, variants, and coverage
- Treat the result as negative evidence only if the person should have appeared and the relevant records are substantially complete and searchable
- Otherwise label it "not indexed," "not online," "coverage unknown," or "not searched"

### Single-Source Reliance
- One index entry is a lead, not a conclusion
- "Proven" has no mechanical source-count minimum: it requires reasonably exhaustive research, complete citations, analysis/correlation, conflict resolution, and a sound written conclusion
- Even original documents can contain errors (scribe mistakes, informant inaccuracies); evaluate each information item and informant
- Multiple databases may repeat the same underlying record and are not independent corroboration

### Weak or Non-Durable Citations
- A homepage, search-results URL, or screenshot without context is not enough
- Capture repository, collection/fonds/series, unit or volume, page/act/certificate/image, stable record ID, URL, and access date
- Save raw API responses and full images before cropping or normalizing; preserve rights/access notes
- Put literal transcription, translation, normalized values, and interpretation in separate fields or notes

### Privacy Leakage
- Do not upload a GEDCOM containing living people to a third party without authorization
- Do not embed API keys, cookies, signed URLs, raw DNA, match identities, contact details, or private correspondence in GEDCOM notes
- Respect provider privacy controls and record closure periods even when a URL is technically reachable

### Not Checking All Record Types
For each time period, check:
- Birth/baptism records
- Marriage records (contain parents' names — often the most informative)
- Death records (contain age, spouse, sometimes parents)
- Census/revision lists
- Confessional lists (annual parish census in Russian Empire)
- Military records
- Immigration/emigration records
- Land records / tax rolls

### Not Working Backwards
- Always work from known to unknown — from yourself backward in time
- Jumping ahead ("I know my ancestor came from village X in 1700") without proving each generation leads to wrong-line errors
- Each generation link must have evidence

### Overreliance on Family Oral History
- Family stories preserve core truths but garble details
- "Grandma came from Germany" might mean Prussian Poland, Volga German colony in Russia, or Austrian Galicia
- Use oral history as a **starting hypothesis**, then verify with documents
