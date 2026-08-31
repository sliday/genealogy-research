# Evidence-Safe GEDCOM Enrichment

Use this workflow when the task is to extend, correct, or reconcile a `.ged` tree from external sources. It is deliberately conservative: discovery may be automated; conclusions and GEDCOM mutations require traceable evidence and conflict review.

Normative references:
- FamilySearch GEDCOM 7 specifications: https://gedcom.io/specs
- Current GEDCOM repository and releases: https://github.com/FamilySearch/GEDCOM
- Board for Certification of Genealogists, standards and Genealogical Proof Standard overview: https://www.bcgcertification.org/ethics-standards/
- FamilySearch GEDCOM X specifications, useful when consuming FamilySearch APIs: https://github.com/FamilySearch/gedcomx

## Non-negotiable rules

1. **Never merge a hint directly.** User trees, search hints, indexes, OCR, and AI transcriptions are leads until verified against an identifiable record or a defensible body of correlated evidence.
2. **Preserve the input.** Work on a copy; do not renumber existing XREF IDs unnecessarily; retain the original file and a change log.
3. **Attach provenance at assertion level.** A source on a person is not enough. Cite the source from each event, name, relationship, or other assertion it supports.
4. **Keep record text separate from interpretation.** Preserve literal transcription, normalized value, translation, and inference as different fields or notes.
5. **Do not silently resolve conflicts.** Record conflicting dates, names, places, and relationships; explain the resolution or leave the conclusion open.
6. **Protect living people.** Do not send living-person details to third-party services without authorization. Do not publish private records, contact details, DNA data, or credentials in GEDCOM notes.
7. **Respect access rules.** Prefer official APIs, exports, OAI-PMH, IIIF, and bulk datasets. Never bypass login, CAPTCHA, paywalls, rate limits, robots controls, or technical restrictions.

## Phase 1: Inspect and preserve the GEDCOM

1. Detect GEDCOM version and character encoding from `HEAD`.
2. Save a byte-identical backup and compute a checksum.
3. Parse the file with a GEDCOM-aware parser; do not edit it as unstructured text unless the change is trivial and validation is available.
4. Inventory:
   - individuals and families;
   - names and aliases;
   - dates and date ranges;
   - places and historical jurisdictions;
   - relationships;
   - existing sources, repositories, notes, media, and external IDs;
   - living or possibly living people.
5. Run a baseline validator appropriate to the declared GEDCOM version. Preserve pre-existing errors separately from new errors.

## Phase 2: Define a bounded research question

Work one relationship or event at a time. Good questions look like:
- Who were the parents of Maria Nowak, married in Łomża about 1888?
- Is the Jan Kowalski in the 1900 census the same person as the 1894 immigrant?
- Which source supports the death date currently stored for X?

For the target person, create an anchor packet:
- all recorded name forms and scripts;
- sex/gender as recorded, not guessed from name alone;
- date ranges with uncertainty;
- places plus parish/civil jurisdiction for the relevant year;
- relatives, associates, witnesses, occupations, religion, addresses, and migration clues;
- known contradictions;
- prior searches and coverage gaps.

## Phase 3: Build a source ladder

Choose sources by the claim being tested, jurisdiction, time, denomination, and likely record survival.

| Claim | Start with | Corroborate with |
|---|---|---|
| Parent-child link | Birth/baptism, guardianship, probate | Census/household register, marriage, obituary, DNA cluster |
| Spousal link | Marriage license/register | Church marriage, census, probate, newspaper notice |
| Birth | Civil/church birth record | Census, school, military, death record |
| Death | Civil death record, burial register | Probate, obituary, cemetery image |
| Residence | Census/household register | Directory, tax/land, electoral register |
| Migration | Passenger/border record | Naturalization, passport, alien file, census |
| Military service | Service/pension file | Draft card, casualty list, unit history |
| Name change/alias | Court/naturalization record | Repeated records linking family, address, occupation |

An index locates a record. A scan or archival image is usually stronger than the index, but even an original record can contain incorrect informant or clerk information. Evaluate each information item, not just the container.

## Phase 4: Search reproducibly

For every query, log:
- research question and target person;
- service and collection;
- stable collection/catalog URL;
- exact query, filters, spelling variants, and date/place radius;
- search date;
- result count or negative result;
- collection coverage and known gaps;
- API version, endpoint, pagination cursor, and response timestamp when applicable.

Search exact anchors first, then relax one dimension at a time. Generate variants for diacritics, transliteration, patronymics, maiden/married forms, aliases, and historical place names. Do not treat fuzzy search scores as evidence.

A negative search becomes evidence only when:
1. the person should reasonably appear in that record set;
2. the relevant jurisdiction, event type, denomination, and years are covered;
3. spelling/indexing limitations were tested; and
4. the search can be reproduced.

Otherwise record **not indexed**, **not online**, **coverage unknown**, or **not searched**—not “absent.”

## Phase 5: Create an evidence packet for every candidate

Store the raw response or full archival image before interpretation. Each packet should contain:

```yaml
candidate_id: local-stable-id
research_question: "..."
target_xref: "@I42@"
service: "..."
collection_title: "..."
collection_id: "..."
record_id: "..."
record_url: "https://..."
repository: "..."
archive_reference: "fonds/series/unit/page or film/image"
accessed: "YYYY-MM-DD"
record_type: "birth|marriage|death|census|..."
record_date_literal: "..."
record_place_literal: "..."
transcription_literal: "..."
normalized_fields: {}
translation: "..."
people_as_recorded: []
informant_and_role: "..."
image_or_raw_response: "relative/path"
rights_or_access_note: "..."
coverage_note: "..."
conflicts: []
identity_assessment: "accept|reject|unresolved"
reasoning: "..."
```

Use repository call number, film, volume, page, act/certificate number, image number, and stable record ID whenever available. A URL alone is not a durable citation.

## Phase 6: Resolve identity before adding facts

Compare candidates on independent dimensions:
- name and variant plausibility;
- age/date compatibility;
- exact place and historical jurisdiction;
- parents, spouse, children, witnesses, and associates;
- occupation, religion, address, military unit, or migration chain;
- chronology and biological plausibility;
- contradictions and common-name collision risk.

### Decision gate

**Accept** only when the candidate is uniquely consistent with the anchor packet and no unresolved hard contradiction remains.

**Reject** when a hard contradiction cannot be explained—for example, incompatible spouse/parents, simultaneous residences that cannot coexist, impossible chronology, or a different stable identity.

**Unresolved** when several people remain plausible or the only support is another tree, an index without enough identifiers, OCR, or a name/date coincidence.

Do not use a numeric match score as a substitute for written reasoning. Scores may rank candidates, but they do not prove identity.

## Phase 7: Draft a patch, do not mutate blindly

Produce a human-reviewable proposal first:

| Target | Proposed change | Evidence | Conflicts | Decision |
|---|---|---|---|---|
| `@I42@ BIRT` | Add `12 MAR 1881`, Dołubowo | archive citation + image | Census implies 1880 | Accept as recorded birth; retain census discrepancy |
| `@F9@ CHIL` | Link `@I42@` | Birth act names both parents | none | Accept |
| `@I42@ DEAT` | Replace 1945 with 1944 | index only | family note says 1945 | Unresolved; no mutation |

Unless the user explicitly authorizes automatic application, stop at the proposal for relationship changes, merges, and deletions.

When applying:
- add or reuse a `SOUR` record with repository and bibliographic details;
- attach a source citation to the exact event/name/relationship;
- preserve literal page/act/image locator in the citation;
- add transcription or extracted text without overwriting normalized values;
- preserve conflicting values in notes or parallel assertions supported by their own citations;
- record service record IDs and access date;
- use standard GEDCOM tags where possible and document any extension tags;
- never embed API keys, session URLs, cookies, or private DNA identifiers.

## Phase 8: Validate and reconcile

After mutation:
1. serialize to a new file;
2. run syntax validation for the declared GEDCOM version;
3. re-parse the output;
4. compare record counts and XREF references;
5. check for dangling family/person/source/repository/media links;
6. check date and relationship plausibility;
7. verify every new assertion has a citation;
8. confirm living-person redaction policy;
9. generate a semantic diff and research log entry.

Deliver:
- original path and enriched path;
- validator results;
- additions, corrections, merges, and unresolved candidates;
- source list with stable identifiers;
- negative searches and coverage gaps;
- exact next research actions.

## Automation policy

| Access | Allowed behavior |
|---|---|
| Official API | Use documented endpoints, auth, pagination, attribution, and rate limits; cache raw responses |
| Official bulk/open dataset | Preserve version/date/license and source institution; verify record-level identifiers |
| OAI-PMH / IIIF / SRU | Use published interfaces; retain manifest/record IDs and rights statements |
| User export/download | Analyze locally; preserve export timestamp and provider IDs |
| Public web page with permissive terms | Fetch conservatively only after reviewing terms and `robots.txt`; identify the client and rate-limit |
| Login, subscription, CAPTCHA, or bot protection | Human/browser workflow only unless the provider has granted API access |
| Undocumented endpoint | Treat as unstable; do not build bulk collection around it without permission; prefer manual capture or official export |

`robots.txt` is not a license and terms are not replaced by technical accessibility. When permission is ambiguous, default to manual retrieval and ask the user to provide the record or export.

## Anti-patterns

- Adding ancestors from another user's tree with no underlying sources
- Converting an index match into a “proven” fact without checking identifiers and coverage
- Declaring someone absent because one spelling returned zero hits
- Scraping commercial sites because an internal JSON endpoint is visible
- Overwriting a date instead of preserving and explaining conflict
- Merging same-name people without family, place, and chronology correlation
- Citing only a homepage or search-results URL
- Uploading a GEDCOM containing living people to a third party without consent
- Treating DNA ethnicity estimates as proof of a specific relationship
