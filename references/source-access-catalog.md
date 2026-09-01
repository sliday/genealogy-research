# Genealogy Source Access Catalog

Reviewed: 2026-09-01. Interfaces and terms change; re-check the linked official documentation before automating.

This catalog answers two separate questions:
1. **Where might the evidence exist?**
2. **How may an agent retrieve it?**

A service's tree, hint, transcription, OCR, or index is not automatically evidence for a GEDCOM assertion. Follow [gedcom-enrichment-workflow.md](gedcom-enrichment-workflow.md) before writing to a tree.

## Access labels

- **API** — documented machine interface intended for third parties.
- **Bulk/OAI/IIIF/SRU** — official dataset or cultural-heritage protocol.
- **Export** — user-initiated GEDCOM/CSV/document download.
- **Manual** — browser, subscription, archive request, or on-site use; do not scrape by default.
- **Observed endpoint** — publicly reachable but not established here as a supported public API; use only for small, user-directed retrieval and expect breakage.

## Choose the source by claim

| Source class | Best for | Reliability caution |
|---|---|---|
| Civil/church register image | Birth, marriage, death, parents, spouses | Informant and clerk can be wrong; confirm correct act, parish, and duplicate copy |
| Census/household register | Residence, household, age, birthplace | Relationships and ages may be approximate; absent people may be elsewhere |
| Probate/guardianship | Kinship, death, property, residence | Legal relationships may not equal biological ones |
| Land/tax/electoral/directory | Residence, occupation, continuity | Usually indirect identity evidence |
| Immigration/naturalization | Origin, arrival, aliases, relatives | Passenger manifests and later declarations may conflict |
| Military | Birth, residence, service, next of kin | Repeated service numbers and full files matter more than name-only indexes |
| Newspaper/obituary | Kinship, residence, life events | OCR is noisy; newspapers repeat errors; inspect the page image |
| Cemetery/memorial | Death/burial, family plot | User memorials are derivative; headstone images are stronger but still later testimony |
| User-submitted tree | Leads, aliases, possible relationships | Never import unsourced relationships as conclusions |
| DNA | Relationship hypotheses and cluster support | Requires consent, relationship modeling, and documentary correlation |
| Gazetteer/map | Place identity and jurisdiction | Supports place context, not personal events by itself |

## A. Documented APIs and open machine interfaces

### Genealogy graphs and tree services

| Service | Interface | Scope | Access and reliability notes |
|---|---|---|---|
| **FamilySearch Developer Platform** | API: https://developers.familysearch.org/ | Family Tree persons/relationships, sources, memories, places, matches, genealogies | Application review, API keys, OAuth 2, compatibility requirements. The main API is excellent for candidate discovery and existing citations. Bulk Family Tree and historical-record feeds require partner agreements; do not assume historical-record bulk access. Docs index: https://developers.familysearch.org/main/llms.txt |
| **WikiTree** | Read-only API: https://www.wikitree.com/wiki/Help:API_Documentation | Public/shared profiles and relationships visible to the logged-in user | Use the API rather than scraping. Include `appId`; published policy currently lists 200 requests/minute and 4,000/hour. Policies: https://www.wikitree.com/wiki/Help:App_Policies . Treat profile data as a lead unless it cites underlying records. |
| **WikiTree data dumps** | Bulk: https://www.wikitree.com/wiki/Help:Database_Dumps | Large-scale public profile data | Prefer for broad analysis when permitted; dumps may lag and omit biographies. Preserve dump date and profile IDs. |
| **Geni Platform API** | API docs: https://www.geni.com/platform/developer/help ; API terms: https://www.geni.com/platform/developer/help/terms?version=1 | Collaborative profiles, relatives, trees, projects and profile search subject to permissions | OAuth and an approved application are required. Treat Geni graph assertions as leads unless supported by cited records. Follow profile privacy and attribution requirements; do not substitute API graph edges for proof. |
| **Open Archives (Netherlands and Belgium)** | API/OpenAPI, file exports, OpenSearch, OAI-PMH: https://api.openarchieven.nl | Civil registration and other participating archival genealogical records, plus transcriptions | Strong discovery layer with source citations and record IDs. Published throttle is 4 requests/second per IP; use a descriptive user agent. Follow links back to the contributing archive/image. |

### National archives, libraries, newspapers, books

| Service | Interface | Scope | Access and reliability notes |
|---|---|---|---|
| **US National Archives Catalog (NARA)** | API docs: https://www.archives.gov/research/catalog/help/api ; open dataset: https://www.archives.gov/developer/national-archives-catalog-dataset | Federal archival descriptions and digitized records: census, immigration, military, naturalization, land, courts | API/catalog hits often describe a series rather than name-index every page. Capture NAID, record group, series, file/item, and image. |
| **Library of Congress** | JSON/YAML API: https://www.loc.gov/apis/json-and-yaml/ | Books, maps, photographs, manuscripts, newspapers, authority data | No key for normal public requests. Use collection/item IDs, rights fields, and original repository metadata. |
| **Chronicling America** | loc.gov API guide: https://www.loc.gov/apis/additional-apis/chronicling-america-api/ ; datasets: https://guides.loc.gov/chronicling-america/additional-features | Historic US newspapers, page images, OCR, title and issue metadata | Since 2025 the collection uses the loc.gov API. OCR produces leads; verify names and relationships on the page image. |
| **Digital Public Library of America** | API: https://pro.dp.la/developers/api-basics ; policies: https://pro.dp.la/developers/policies | Aggregated US cultural-heritage metadata | API key required. DPLA usually points to a contributing institution; cite the underlying item, not only the aggregator. |
| **Internet Archive** | Search and metadata APIs: https://archive.org/developers/index-apis.html ; IIIF: https://iiif.archive.org/iiif/documentation | City directories, county histories, yearbooks, newspapers, scanned books, archival collections | Check item rights and provenance. OCR/name hits are leads; cite item identifier and page/image. |
| **Google Books** | Books API: https://developers.google.com/books | Digitized books and bibliographic metadata | Useful for directories, local histories, regimental and institutional histories. Availability and full-text rights vary. |
| **HathiTrust** | APIs: https://www.hathitrust.org/the-collection/data-resources/ | Bibliographic and eligible full-text research services | Access varies by API, rights, and institutional status. Use as discovery when page access is restricted. |
| **Trove (National Library of Australia)** | API: https://trove.nla.gov.au/about/create-something/using-the-api/what-is-the-trove-api | Australian newspapers, people/organizations, books, images, archives and contributed metadata | Active key required; commercial use needs explicit permission. Full newspaper OCR is available through the API. Verify against page images. |
| **Canadiana / Héritage** | IIIF pattern and navigation: https://www.crkn-rcdr.ca/en/navigating-collections | Digitized Canadian publications and archival microfilm, including immigration, military, Indigenous, government and private fonds | Canadiana documents an IIIF manifest form for items. Collection-scale harvesting/reuse is not assumed; follow CRKN terms and item rights. Preserve the Canadiana ID plus the Library and Archives Canada fonds/series/MIKAN provenance when present. |
| **DigitalNZ** | API v3: https://digitalnz.org/developers/api-docs-v3 | New Zealand cultural, government, newspaper, image, audio, and archival metadata | Public content can be queried without a key at lower limits; keys are recommended for regular/high-volume use. DigitalNZ is an aggregator—follow the source record. |
| **Papers Past** | Search: https://paperspast.natlib.govt.nz/ ; programmatic discovery through DigitalNZ: https://digitalnz.org/developers | New Zealand newspapers, magazines, letters/diaries, parliamentary papers | Use DigitalNZ for metadata discovery; verify OCR on Papers Past page images and retain publication/date/page. |
| **Europeana** | APIs: https://www.europeana.eu/en/apis ; API portal: https://api.europeana.eu/ | European archival, library, museum, newspaper, image, and manuscript metadata | Mostly read-only search/record interfaces; API key may be required. Rights vary per item. Follow `edm:isShownAt`/provider links to the holding institution. |
| **Gallica / Bibliothèque nationale de France** | API hub: https://api.bnf.fr/ ; search, OAI, OCR, document, and IIIF services: https://api.bnf.fr/fr/api-document-de-gallica | French books, newspapers, directories, maps, manuscripts, images | Use ARK identifiers. OCR is discoverability evidence only; verify on the scan. Rights/reuse are item-specific. |
| **Swedish National Archives (Riksarkivet)** | API overview: https://sok.riksarkivet.se/en/data-api (verify current path; older /data-api/api URLs did not respond on 2026-09-01) | Search API, OAI-PMH, IIIF, linked-data representations, archival descriptions and selected open datasets | Some interfaces are beta or dataset-specific. Preserve archive/volume/image identifiers and inspect the underlying image. |

### Machine interfaces with constrained or uncertain scope

| Service | Interface | Scope | Access and reliability notes |
|---|---|---|---|
| **The National Archives (UK) Discovery** | API terms and help entry: https://www.nationalarchives.gov.uk/terms-and-conditions/discovery-for-developers-about-the-application-programming-interface-api/ | UK central-government and contributed archive catalog descriptions | A documented Discovery API exists, but it is principally a catalogue interface. Confirm the current endpoint/help before implementation, obey its terms, and capture catalogue references. A description of a file or series is not proof of a personal event. |
| **Archives Portal Europe** | Metadata guidance: https://www.archivesportaleurope.net/metadata-usage-guidelines/ | European archival finding aids | The portal recommends API use, but the consumer endpoint/schema was not confirmed in this review. Do not invent an endpoint; use the portal manually and link to the holding archive with its reference code. |
| **Findmypast developer interfaces** | Public documentation repository: https://github.com/findmypast/public_docs | Selected Findmypast integration APIs | Availability to a repository does not imply open access to record content. Treat as partner/approved access unless Findmypast grants credentials and scope; ordinary research remains browser/subscription based. |

### Poland and Central Europe machine access

| Service | Interface | Scope | Access and reliability notes |
|---|---|---|---|
| **Szukaj w Archiwach (Polish State Archives)** | Portal: https://www.szukajwarchiwach.gov.pl/ ; file metadata/download endpoints observed in the browser are undocumented | Polish archival descriptions and digitized scans | Authoritative for holdings and images. Record `zespół`, series, unit/sygnatura, unit ID, file/image ID, and image position. The file endpoints are treated here as observed public interfaces, not a guaranteed stable developer API. |
| **Archives Portal Europe / Europeana** | APIs above | Finding aids from Poland, Czechia, Hungary, Baltics and other contributors | Useful when national portals are difficult to search programmatically; always resolve to the holding archive. |
| **Matricula Online** | Portal: https://data.matricula-online.eu/ ; project information: https://www.icar-us.eu/en/cooperation/online-portals/matricula/ | Church-register images across participating European dioceses/archives | No general public search API is relied upon here. Use manual navigation and stable archive/parish/book/page identifiers; obey image rights. |

### Places, jurisdictions, and identifiers

| Service | Interface | Scope | Access and reliability notes |
|---|---|---|---|
| **FamilySearch Places** | Through FamilySearch API: https://developers.familysearch.org/main/page/places-endpoints | Historical and modern standardized place names | Useful for normalization and alternate names; retain the place as written in the record separately. |
| **Wikidata Query Service** | SPARQL: https://query.wikidata.org/ | Alternate place names, administrative entities, dates, coordinates, external IDs | Context only unless the claim is independently sourced. Follow rate/usage guidance. |
| **GeoNames** | API: https://www.geonames.org/export/web-services.html | Global place names and coordinates | Account required for web services. Good for modern geocoding; historical jurisdiction may differ. |
| **OpenStreetMap Nominatim** | API policy: https://operations.osmfoundation.org/policies/nominatim/ | Modern geocoding and place context | Public instance has strict usage limits. Not an authority for historical parish/civil boundaries. |
| **Getty Thesaurus of Geographic Names** | Linked Open Data: https://www.getty.edu/research/tools/vocabularies/lod/ | Historical and alternate place names | Useful for authority control; retain record-era names. |

## B. High-value services that are manual, export-first, or permissioned

Do not infer permission to scrape from the absence of an API. For these services, use the user's browser/session, official download/export, or a provider agreement.

### Commercial and collaborative trees/record aggregators

| Service | Access | Best use | Caution |
|---|---|---|---|
| **Ancestry** — https://www.ancestry.com/ | Manual/subscription; user GEDCOM and record downloads where offered | Censuses, immigration, military, vital records, newspapers, user trees and hints | No general public research API is documented here. Ancestry terms restrict automated scraping; use browser/export. Hints and member trees are leads. |
| **MyHeritage** — https://www.myheritage.com/ | Manual/subscription; user GEDCOM/export where offered; partner integrations by agreement | International historical records, trees, newspapers, DNA matching | Do not automate private/internal endpoints. Verify Smart Matches and Record Matches against underlying records. |
| **YourRoots** — https://yourroots.com/ | Manual/account; GEDCOM upload and user exports only | GEDCOM mapping, FamilySearch-connected hints, AI research leads, DNA matching | Terms prohibit bots and AI agents without written authorization; no public API. AI output is a lead, not evidence. |
| **Findmypast** — https://www.findmypast.com/ | Manual/subscription/export where offered | UK/Ireland censuses, parish records, newspapers, military and migration | No general public research API is relied upon here. Use browser and licensed downloads. |
| **Geneanet** — https://en.geneanet.org/ | Manual/free/subscription; GEDCOM import/export for owned trees | European user trees, indexed collections, archival projects | User trees are lead generators; cite original records. |
| **Geni** — https://www.geni.com/ | Manual/shared-tree workflows; documented OAuth API for approved applications | Collaborative world tree | Profile claims need underlying sources and identity reconciliation. See the API row above. |
| **FamilySearch Historical Records** — https://www.familysearch.org/search/ | Manual search/download; selected partner/API access | Billions of indexed records and images | General API access does not imply unrestricted historical-record access. Some images require a FamilySearch Center or partner site. |
| **FamilySearch Catalog** — https://www.familysearch.org/search/catalog | Manual catalog lookup | Collection/film discovery and coverage | Catalog entries identify holdings, not a person. Record film/DGS numbers and access restrictions. |

### Canada, Australia, and New Zealand public archives

| Service | Access | Holdings/use |
|---|---|---|
| **Library and Archives Canada Collection Search** — https://www.canada.ca/en/library-archives/collection/search.html | Manual/free; downloads and orders as offered | Censuses, passenger/border records, citizenship, First World War personnel, land petitions, Métis scrip, Indigenous and residential-school records, government/private fonds, books and directories. No supported general public collection API was verified; preserve MIKAN/item references. |
| **Canadiana / Héritage** — https://www.canadiana.ca/ ; https://heritage.canadiana.ca/ | Manual/free and documented item-level IIIF | Digitized publications and LAC microfilm. Cite the archival provenance and reel/page, not only the viewer. Do not bulk harvest without current permission. |
| **National Archives of Australia RecordSearch** — https://recordsearch.naa.gov.au/ | Manual/free; digitized downloads and copy orders where offered | Immigration, citizenship, defence/service, security, government and personal records. No supported general public API was verified; capture series, control symbol, item ID and image. |
| **Archives New Zealand Collections Search** — https://collections.archives.govt.nz/ | Manual/free; copy/order workflows | Government archives including immigration, military, court, probate, land, education and employment records. No supported general public collection API was verified; cite agency/series/item/archive location. Copying guidance: https://www.archives.govt.nz/research-guidance/copying-and-citing-archives |
| **US state and local archives** — NARA state-archives directory: https://www.archives.gov/research/alic/reference/state-archives.html | Manual; repository-specific API, CONTENTdm, IIIF, OAI-PMH, CSV or open-data interfaces may exist | State vital, court, land, probate, prison, school, military, tax and local-government records. Verify the interface on each archive's official developer/open-data page; do not generalize one state's permissions to another. |

### United Kingdom and Ireland

| Service | Access | Holdings/use |
|---|---|---|
| **FreeBMD** — https://www.freebmd.org.uk/ | Manual; open-data reuse only under current project licence/approved channels | England and Wales civil registration index. Order/inspect certificates for strong proof. |
| **FreeREG** — https://www.freereg.org.uk/ | Manual; project open-data channels under current licence | Parish-register transcriptions. Verify against register images where available. |
| **FreeCEN** — https://freecen2.freecen.org.uk/ | Manual; project open-data channels under current licence | UK census transcriptions. Compare image and household context. |
| **General Register Office, England and Wales** — https://www.gro.gov.uk/gro/content/certificates/ | Manual/account/order | Official civil indexes and certificates. |
| **ScotlandsPeople** — https://www.scotlandspeople.gov.uk/ | Manual/pay-per-view | Scottish civil registration, censuses, church records, wills and valuation rolls. |
| **The National Archives Discovery** — https://discovery.nationalarchives.gov.uk/ | Manual/API only when current official Discovery documentation grants it | UK central government and 2,500+ archive catalog descriptions; military, migration, probate and courts. Capture catalogue references. |
| **IrishGenealogy.ie** — https://www.irishgenealogy.ie/ | Manual/free | Irish civil and church records; image access and privacy cutoffs vary. |
| **National Archives of Ireland Genealogy** — https://genealogy.nationalarchives.ie/ | Manual/free | Censuses, valuation, wills, military/police and other datasets. |
| **PRONI** — https://www.proni.gov.uk/ | Manual/free and archive request | Northern Ireland wills, valuation, directories, church and estate records. |
| **RootsIreland** — https://www.rootsireland.ie/ | Manual/subscription | Irish church and civil transcriptions. Verify against images/certificates. |

### Continental Europe

| Service | Access | Holdings/use |
|---|---|---|
| **Antenati** — https://antenati.cultura.gov.it/ | Manual/free | Italian civil-registration images and indexes. Cite archive, collection, register, act and image. |
| **Archion** — https://www.archion.de/ | Manual/subscription | German Protestant church-register images. |
| **CompGen / GOV** — https://www.compgen.de/ ; https://gov.genealogy.net/ | Manual; selected project downloads/interfaces | German genealogy indexes, directories, place/jurisdiction gazetteer. Verify personal assertions in records. |
| **German Federal Archives** — https://www.bundesarchiv.de/EN/Navigation/Home/home.html | Catalog/manual request | Military, citizenship, displaced persons and federal records; privacy/access rules apply. |
| **French departmental archives** — directory: https://francearchives.gouv.fr/fr/annuaire/departements | Manual; some departments expose IIIF/OAI independently | Parish and civil registers, censuses, military recruitment, notarial and land records. Interfaces and reuse terms vary by department. |
| **WieWasWie** — https://www.wiewaswie.nl/en/ | Manual/subscription features | Dutch civil and population records. Prefer Open Archives API for lawful automation where the same archives participate. |
| **Danish National Archives / Arkivalieronline** — https://www.rigsarkivet.dk/en/ | Manual/free; datasets as separately published | Church books, censuses, probate and military records. |
| **Norwegian Digital Archives (Digitalarkivet)** — https://www.digitalarkivet.no/en/ | Manual/free; official downloads where offered | Norwegian censuses, church books, emigration, probate, military and other archives. No supported general read/search API was verified in this review; do not reverse-engineer site services. Check transcriptions against scans. |
| **National Archives of Finland / Astia** — https://astia.narc.fi/uusiastia/ | Manual/free; open datasets as separately published | Finnish church, military, court, map and administrative holdings. |
| **Porta fontium** — https://www.portafontium.eu/ | Manual/free | Czech-Bavarian archival material and parish registers. |
| **Czech regional archives / Acta Publica** — https://www.mza.cz/actapublica/ | Manual/free | Moravian parish-register images; regional systems vary. |
| **Hungarian National Archives** — https://mnl.gov.hu/angol | Manual/catalog/request | Civil, church, census, nobility, military and administrative records. |

### Poland, Ukraine, Baltics, Russia and neighboring regions

| Service | Access | Holdings/use |
|---|---|---|
| **Geneteka** — https://geneteka.genealodzy.pl/ | Manual/free | Polish parish/civil indexes. Use coverage tables and nearby-parish search; verify against scans. |
| **Skanoteka** — https://skanoteka.genealodzy.pl/ | Manual/free | Parish-register scans connected to Polish Genealogical Society projects. |
| **Metryki** — https://metryki.genealodzy.pl/ | Manual/free | Polish metric-book scans/index links. |
| **PRADZIAD / Polish archival holdings search** — https://www.szukajwarchiwach.gov.pl/ | Manual/catalog | Determines which vital/parish books survive and where; critical for coverage analysis. |
| **Poznań Project** — https://poznan-project.psnc.pl/ | Manual/free | 19th-century Greater Poland marriage indexes. |
| **AGAD** — https://agad.gov.pl/ | Manual/catalog/scans | Central Archives of Historical Records in Warsaw; former eastern territories and historic state records. |
| **Ukrainian archival portal** — https://archives.gov.ua/en/ | Manual/catalog/archive request | National and regional archive directories, guides and digitization links. War and access conditions change. |
| **Lithuanian State Historical Archives / ePaveldas** — https://lvia.archyvai.lrv.lt/en/ ; https://www.epaveldas.lt/ | Manual | Church, estate, nobility and civil records; catalog and digital-library coverage varies. |
| **Latvian Raduraksti** — https://raduraksti.arhivi.lv/ | Manual/registration | Church books, censuses and revision lists. |
| **Estonian Saaga / AIS** — https://www.ra.ee/dgs/explorer.php ; https://ais.ra.ee/ | Manual/free | Digitized church, census, estate and archival catalog records. |
| **OBD Memorial** — https://obd-memorial.ru/ | Manual/free | Soviet WWII losses, burials, missing personnel and document images. |
| **Pamyat Naroda** — https://pamyat-naroda.ru/ | Manual/free | Soviet WWII awards, units, operations and service documents. |
| **Podvig Naroda** — https://podvignaroda.ru/ | Manual/free | Soviet award records and citations. |

### Jewish, Holocaust, displacement and migration

| Service | Access | Holdings/use |
|---|---|---|
| **JewishGen** — https://www.jewishgen.org/ | Manual/registration; collection-specific downloads only when offered | Global Jewish indexes, communities, burial, Holocaust and family-finder data. Verify against cited archive/record. |
| **JRI-Poland** — https://www.jri-poland.org/ | Manual/free/donation-supported | Indexes to Jewish vital and other Polish records with archive references. |
| **Yad Vashem Names Database** — https://yvng.yadvashem.org/ | Manual/free | Pages of Testimony, victim records, transport and Shoah documentation. Informant-submitted pages require correlation. |
| **Arolsen Archives** — https://collections.arolsen-archives.org/en/ | Manual/search/download subject to terms | Nazi persecution, forced labor, displaced persons and postwar tracing documents. Cite document IDs and images. |
| **USHMM Collections** — https://collections.ushmm.org/search/ | Manual/catalog and collection-specific access | Holocaust archives, oral histories, photographs, lists and survivor/victim documentation. |
| **Ellis Island / Statue of Liberty Foundation** — https://heritage.statueofliberty.org/ | Manual/account | New York passenger arrivals and ship manifests; verify the manifest image and line. |
| **Steve Morse One-Step** — https://stevemorse.org/ | Manual search aid | Front-end search tools for multiple databases. Cite the underlying database/record, not the search aid. |
| **Immigrant Ships Transcribers Guild** — https://www.immigrantships.net/ | Manual/free | Volunteer passenger-list transcriptions. Seek the original manifest. |

### Military, burial, newspapers and specialist sources

| Service | Access | Holdings/use |
|---|---|---|
| **Commonwealth War Graves Commission** — https://www.cwgc.org/find-records/find-war-dead/ | Manual/free | Commonwealth war dead and cemeteries. Capture service number, unit, date, cemetery/memorial. |
| **Volksbund grave search** — https://www.volksbund.de/en/erinnern-gedenken/gravesearch-online | Manual/registration | German war dead and burial data. |
| **Fold3** — https://www.fold3.com/ | Manual/subscription | US and international military indexes/images. Verify service file image and identifiers. |
| **Find a Grave** — https://www.findagrave.com/ | Manual/free | User memorials and cemetery photographs. Memorial text is derivative; distinguish headstone transcription from contributor claims. |
| **BillionGraves** — https://billiongraves.com/ | Manual/free/subscription features; partner access by agreement (site did not respond to automated check on 2026-09-01) | GPS-tagged cemetery images/transcriptions. Verify the image and cemetery. |
| **Newspapers.com** — https://www.newspapers.com/ | Manual/subscription | Historical newspaper OCR and images. Cite newspaper, date, page, column, and clipping/image. |
| **British Newspaper Archive** — https://www.britishnewspaperarchive.co.uk/ | Manual/subscription | British and Irish newspapers. Verify OCR on page image. |
| **Google Newspaper Archive** — https://news.google.com/newspapers | Manual/free, incomplete | Scanned newspapers with inconsistent metadata/search. |
| **Elephind** — https://elephind.com/ | Manual metasearch | Cross-collection newspaper discovery. Cite the contributing repository/title. |

### DNA services

| Service | Access | Safe use |
|---|---|---|
| **AncestryDNA, MyHeritage DNA, 23andMe, FamilyTreeDNA** | Manual/account/export as explicitly offered | Use match lists and segment tools only with consent and provider terms. Do not publish raw DNA or living-person identities in GEDCOM. |
| **GEDmatch** — https://www.gedmatch.com/ | Manual/account/upload with explicit consent | Cross-platform matching and tools. Respect kit privacy levels and law-enforcement settings. |
| **DNA Painter** — https://dnapainter.com/ | Manual/account | Relationship modeling and chromosome mapping; analytical aid, not independent proof. |

## C. Protocols worth testing before writing a scraper

Many archives expose standards even when they do not advertise a bespoke API.

| Protocol | What it provides | Discovery/usage rule |
|---|---|---|
| **IIIF Presentation/Image API** — https://iiif.io/api/ | Manifests, canvases/pages, image tiles and stable image services | Look for a manifest link in item metadata. Preserve manifest URL, canvas ID, rights, and image region; do not assume download rights. |
| **OAI-PMH** — https://www.openarchives.org/pmh/ | Harvestable metadata records and sets | Use `Identify` first, record metadata prefix/set/datestamp, and obey resumption tokens. Metadata usually points to—not replaces—the source image. |
| **SRU/SRW** — https://www.loc.gov/standards/sru/ | Standard search/retrieve for library catalogs | Query published endpoints only; retain record schema and stable identifier. |
| **EAD / EAC-CPF** | Archival finding aids and authority records | Useful for fonds/series/person/organization discovery, not automatically event-level evidence. |
| **Linked Data / RDF** | Stable URIs and graph relationships | Follow provenance and source institution; graph assertions may be derivative. |
| **CSV/XML/RDF bulk export** | Reproducible local search | Preserve file hash, release date, license, schema, and source URL. |

Before scraping HTML, check in this order:
1. official API/developer page;
2. user export/download;
3. dataset/open-data page;
4. IIIF manifest;
5. OAI-PMH/SRU/OpenSearch/linked-data link;
6. written permission;
7. only then, conservative HTML retrieval if terms and robots permit it.

## D. Source discovery checklist for a new country or locality

A catalog can never enumerate every municipal, diocesan, regional, and specialist archive. For a new place, systematically search for:

1. national archives and national library;
2. civil registration authority and privacy cutoffs;
3. regional/state/provincial archives;
4. diocesan, parish, synagogue, mosque, or denominational archives;
5. census, household register, revision list, and population register;
6. probate, guardianship, notarial, court, land, tax, and electoral records;
7. military, conscription, pension, casualty, and prisoner records;
8. migration, passenger, border, passport, naturalization, alien, and displaced-person files;
9. newspapers, obituaries, directories, yearbooks, occupational and institutional records;
10. cemetery, funeral-home, burial, memorial, and religious burial-society records;
11. local genealogical/historical societies and archive catalogs;
12. surviving-record inventories and explicit coverage gaps.

For every newly discovered service, record: official owner, collection scope, years/places/denominations, interface, authentication, rate limit, cost, rights, stable IDs, image availability, export format, update date, and whether it is an index, transcription, image, or original archival description.
