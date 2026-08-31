# Local Genealogy Databases by Country

Reviewed: 2026-08-31. This is the local-first companion to
[databases-by-region.md](databases-by-region.md) and
[source-access-catalog.md](source-access-catalog.md). Re-check the official site,
coverage, access rules, and privacy cutoffs before each project.

The purpose is not to force every search through an English-language global
aggregator. A multilingual agent should search the archive, civil authority,
diocese, municipality, and genealogical society that actually created or holds the
records.

## How to use this catalog

1. Resolve the event-year jurisdiction before choosing a database.
2. Search the national catalog, then the state/province/department archive, diocese,
   municipality, and local indexing project.
3. Search in the current local language, the record language, and any former ruling
   language or script.
4. Record literal place/name text before transliteration or normalization.
5. Check collection coverage before treating zero hits as negative evidence.
6. Use indexes to locate records; cite and inspect the image, certificate, or archive
   unit whenever available.
7. Assume **manual** access unless the service documents an API, bulk export, OAI-PMH,
   IIIF, SRU, or other machine interface.

## Native-language query construction

Build queries from five components:

`[record type] + [name variant] + [place/parish] + [year/range] + [archive term]`

Run all relevant scripts and historical terms. Examples:

- Polish/Russian partition: `akt urodzenia`, `księga metrykalna`, `urodzonych`,
  `метрическая книга`, `о родившихся`, parish name in Polish and Cyrillic.
- French: `état civil`, `naissances`, `mariages`, `décès`, `registres paroissiaux`,
  `tables décennales`, commune and department.
- German: `Standesamt`, `Geburtsregister`, `Heiratsregister`, `Sterberegister`,
  `Kirchenbuch`, historical Kreis and confession.

Never replace a literal form with the translated form. Store all three when needed:

```yaml
literal: "Иван Кулеш"
transliteration: "Ivan Kulesh"
normalized: "Jan Kulesza"
normalization_status: hypothesis
```

## Poland

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **Geneteka — baza Polskiego Towarzystwa Genealogicznego** — https://geneteka.genealodzy.pl/ | Nationwide and neighboring historic territories; indexed births/baptisms, marriages, deaths/burials across denominations | Free/manual index with coverage tables and many scan links. Search nearby parishes; verify the act image. |
| **Geneszukacz** — https://geneszukacz.genealodzy.pl/ | Meta-search across Polish Genealogical Society projects | Free/manual discovery; resolve each hit to its source project and scan. |
| **Skanoteka** — https://skanoteka.genealodzy.pl/ | Scans of metric and genealogical records contributed by PTG projects | Free/manual images; record archive, fonds/unit, book and image. |
| **Metryki** — https://metryki.genealodzy.pl/ | Parish and civil-register scans arranged by archive/place/book | Free/manual images; image number is not act number. |
| **Szukaj w Archiwach** — https://www.szukajwarchiwach.gov.pl/ | Polish State Archives catalog, fonds, units and digitized images | Official catalog/scans. Capture `zespół`, series, `sygnatura`, unit ID and image ID. |
| **BaSIA — Baza Systemu Indeksacji Archiwalnej** — https://www.basia.famula.pl/ | Greater Poland and adjoining areas; archival and civil/parish indexes with scan links | Free/manual index. Confirm exact record and archive unit. |
| **Poznań Project** — https://poznan-project.psnc.pl/ | 19th-century marriages in historical Greater Poland | Free/manual index; use parish and act details to find the register image. |
| **PomGenBaza — Pomorskie Towarzystwo Genealogiczne** — https://www.ptg.gda.pl/language/pl/pomgenbaza/przeszukiwanie-rejestrow-metrykalnych/ | Pomerania; metric, cemetery and related indexes | Free/manual. Search Polish and German place/name forms; verify linked source. |
| **Lubgens — Baza indeksów Lubelszczyzny** — https://regestry.lubgens.eu/search.php | Lublin region and eastern-borderland parishes; multiple denominations and record types | Free/manual index with project downloads/links. Preserve parish and confession. |
| **Projekt Podlasie — indeksy** — https://indeksy.projektpodlasie.pl/ | Podlasie and Mazovia; Roman Catholic, Orthodox, Greek Catholic, Jewish and other registers | Free/manual index and parish catalog. Search Polish, Russian/Cyrillic and denominational variants. |
| **GENEO — Jamiński Zespół Indeksacyjny** — https://jzi.org.pl/ | Augustów, Suwałki and northeastern Poland; detailed local metric indexes | Free/manual; strong local fields but still verify the original act. |
| **Świętogen** — https://www.genealodzy-kielce.pl/indeksy/ | Świętokrzyskie and neighboring archive/diocesan holdings | Free/manual indexes, often paired with GenBaza scans. |
| **Metryki GenBaza** — https://metryki.genbaza.pl/ | Scans from selected state and diocesan archives, with regional subprojects | Registration/manual. Cite holding archive and source book, not only GenBaza. |
| **Genealogia w Archiwach** — https://www.genealogiawarchiwach.pl/archiwum-front?locale=pl | Civil and church registers from participating Kuyavian-Pomeranian and Greater Poland archives | Free/manual index and scans. Preserve archive, unit, register, act and image identifiers. |
| **Archiwum Główne Akt Dawnych (AGAD)** — https://agad.gov.pl/ | Historic central records and former eastern territories; inventories and selected scans | Official catalog/manual. Essential for Kresy and pre-partition jurisdictions. |
| **Biblioteka Kresowa PTG** — https://kresy.genealodzy.pl/ | Gazetteers, maps, heraldry, indexes, scans and reference works for former eastern territories | Discovery/context; cite underlying work or archival unit. |
| **JRI-Poland** — https://www.jri-poland.org/ | Jewish vital and other record indexes by town/archive | Free/manual/donation-supported. Preserve town, year, act and archive reference; verify image. |
| **Jewish Historical Institute collections** — https://cbj.jhi.pl/ | Polish Jewish archival and library collections, community records, testimony and publications | Official digital collection/manual; item rights vary. |
| **Polona** — https://polona.pl/ | Polish newspapers, directories, books, maps, school and institutional publications | Public digital library/API possibilities vary. OCR is a lead; cite publication and page. |

**Polish query pack:** `akta stanu cywilnego`, `księga metrykalna`, `urodzenia`,
`chrzty`, `małżeństwa`, `zgony`, `pochówki`, `spis ludności`, `księga meldunkowa`,
`akta parafii`, `zespół`, `sygnatura`, `parafia rzymskokatolicka`, `prawosławna`,
`greckokatolicka`, `gmina żydowska`, `cmentarz`, `nekrolog`.

## France

France is commune- and department-driven. Do not stop at Filae or Geneanet: the
image is usually held by the departmental or municipal archive.

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **FranceArchives — annuaire des services d'archives** — https://francearchives.gouv.fr/fr/annuaire/departements | Directory of every departmental archive and many municipal services | Use to route to the correct department's current portal. |
| **FranceArchives — état civil numérisé** — https://francearchives.gouv.fr/fr/article/38170 | Department-by-department links to digitized civil registration | Official routing page; interfaces and reuse terms vary by department. |
| **FranceArchives — recensements numérisés** — https://francearchives.gouv.fr/fr/article/26287471 | Department-by-department population-census links | Official routing page; inspect household images. |
| **Archives départementales** | Each department's `état civil`, parish registers, decennial tables, census, military recruitment, notarial, land and tax collections | Free/manual in most departments; some expose IIIF/OAI. Cite department, commune, register, date/act and image. |
| **Archives municipales** | Large-city and commune collections, sometimes including recent civil tables, censuses, electoral rolls and cemetery registers | Manual/local. Search the municipality when departmental holdings are incomplete. |
| **Archives nationales d'outre-mer (ANOM)** — https://recherche-anom.culture.gouv.fr/ | Colonial and overseas civil registration, administration, military and migration records | Official catalog/images/manual. Record territory, commune, register and image. |
| **Archives diplomatiques — état civil consulaire** — https://www.diplomatie.gouv.fr/fr/archives-bibliotheque/effectuer-des-recherches-genealogiques-ou-familiales/actes-d-etat-civil-et-autres-archives-diplomatiques-et-consulaires | French citizens abroad, consular/diplomatic civil records and requests | Official guidance/request workflow; privacy cutoffs apply. |
| **Grand Mémorial** — https://www.culture.fr/Grand-Memorial | Federated First World War military recruitment and related name indexes | Name discovery; open the departmental matricule image and cite it. |
| **Mémoire des hommes** — https://www.memoiredeshommes.sga.defense.gouv.fr/ | Military dead, service, resistance, deportation and conflict databases | Official military source; follow each result to its record/image. |
| **Gallica** — https://gallica.bnf.fr/ | Newspapers, directories, books, military lists, maps and local histories | SRU/OAI/IIIF/OCR available; verify OCR on page image and cite ARK/page. |
| **RetroNews** — https://www.retronews.fr/ | Historical French press | Manual/free/subscription mix. Article claims require correlation. |
| **GeneaBank** — https://www.geneabank.org/ | Indexes contributed by French genealogical associations | Manual/points through member societies. Index is a locator, not the final source. |
| **MémorialGenWeb** — https://www.memorialgenweb.org/ | War memorials, military deaths, cemetery and memorial transcriptions | Volunteer derivative source; verify official file or memorial image. |
| **Filae** — https://www.filae.com/ | Nationwide French civil, census and other indexes | Subscription/manual. Resolve hits to department/commune images. |
| **Geneanet collections and society projects** — https://www.geneanet.org/ | Trees, indexes, cemetery images and local association datasets | Lead source; retain contributor/collection and verify underlying record. |

**French query pack:** `archives départementales`, `archives municipales`, `état
civil`, `registres paroissiaux`, `naissances`, `baptêmes`, `mariages`, `décès`,
`sépultures`, `tables décennales`, `recensement de population`, `liste nominative`,
`registre matricule`, `classe`, `bureau de recrutement`, `minutes notariales`,
`cadastre`, `registre des cimetières`, `avis de décès`.

## Belgium, Luxembourg, Netherlands, and Switzerland

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **Archives de l'État en Belgique / Rijksarchief** — https://search.arch.be/ | Belgian civil/parish registers, population, notarial and archival descriptions/images | Official/manual account for some images. Search French, Dutch and German locality forms. |
| **AGATHA — Belgian State Archives** — https://agatha.arch.be/ | Newer search environment for archival descriptions, digitized records and persons | Official/manual. Treat person hits as finding aids and retain the archival reference. |
| **FelixArchief Antwerpen / Archives de la Ville de Bruxelles** — https://felixarchief.antwerpen.be/ ; https://archives.brussels.be/ | Municipal population, civil, police, migration, building, cemetery and city records | Official local catalogs/manual; city-specific collections can fill national-index gaps. |
| **Genealogical sources / Rechercher des personnes** — https://search.arch.be/fr/rechercher-des-personnes | Belgian person indexes across participating record sets | Index-level discovery; inspect the register image. |
| **Bibliothèque royale de Belgique / KBR BelgicaPress** — https://www.belgicapress.be/ | Digitized Belgian newspapers and periodicals | OCR/manual; cite title/date/page and verify image. |
| **Archives nationales de Luxembourg — online reading room** — https://archives.services-publics.lu/ | National archival catalog and digitized holdings | Official/manual; language may be French, German or Luxembourgish. |
| **Luxembourg civil records** — https://data.matricula-online.eu/ | Participating parish/civil church books | Free/manual images; cite archive/parish/book/page. |
| **Open Archieven** — https://www.openarchieven.nl/ | Dutch and Belgian participating archives; civil, population, church, notarial and other records | API/OAI/bulk/manual. Follow the source archive and scan. |
| **WieWasWie** — https://www.wiewaswie.nl/ | Dutch civil and population records from participating archives | Manual/free/subscription features; cite source archive and act. |
| **AlleFriezen** — https://allefriezen.nl/ | Friesland civil, church, population and notarial records | Manual; many scan links. Search patronymics and municipality variants. |
| **Zeeuwen Gezocht** — https://www.zeeuwengezocht.nl/ | Zeeland civil, church, population, notarial and migration records | Manual/local archive index; verify scan. |
| **Alle Groningers** — https://www.allegroningers.nl/ | Groningen civil, church and population sources | Manual/local index with scans where available. |
| **Amsterdam, Rotterdam and Noord-Hollands Archief family-history portals** — https://www.amsterdam.nl/stadsarchief/ ; https://stadsarchief.rotterdam.nl/en/genealogy ; https://noord-hollandsarchief.nl/english/family-history | Local population registers, civil records, police cards, notarial records and migration | Official municipal/regional archives; retain the contributing archive and record reference. |
| **Archieven.nl — Personen** — https://www.archieven.nl/nl/personen | Federated person search across many Dutch local and regional archives | Manual aggregator; open the contributing archive's record and scan. |
| **Delpher** — https://www.delpher.nl/ | Dutch newspapers, books, journals and radio bulletins | Full-text/OCR/manual; inspect the page image. |
| **Nationaal Archief** — https://www.nationaalarchief.nl/onderzoeken | Dutch national catalog, colonial, migration, military and government records | Official/manual; selected open datasets/APIs vary. |
| **Swiss Federal Archives** — https://www.recherche.bar.admin.ch/ | Federal archival catalog | Official catalog; most family records are cantonal/communal. |
| **Swiss cantonal archives directory** — https://www.eda.admin.ch/countries/usa/en/home/services/genealogy/research-switzerland/staatsarchive.html | Official directory routing to cantonal archives | Resolve canton/commune/confession before requesting civil or church records. |
| **e-codices** — https://www.e-codices.unifr.ch/ | Digitized Swiss manuscripts | Context/specialist evidence, not a general person index. |

**Dutch query pack:** `burgerlijke stand`, `doopboek`, `trouwboek`, `begraafboek`,
`bevolkingsregister`, `gezinskaart`, `persoonskaart`, `notariële akte`, `memorie van
successie`, `militieregister`, `woningkaart`, `overlijdensadvertentie`.

## Germany, Austria, and German-speaking Switzerland

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **Archion** — https://www.archion.de/ | Protestant church books from participating Landeskirchen | Subscription/manual images. Cite Landeskirche, archive, parish, book and page. |
| **Matricula Online** — https://data.matricula-online.eu/ | Catholic and other church books from participating German/Austrian/Swiss dioceses | Free/manual images. Coverage is archive-specific. |
| **CompGen Meta-Suche** — https://meta.genealogy.net/ | Federated search across CompGen databases | Discovery; open the specific database/source. |
| **GOV — Geschichtliches Ortsverzeichnis** — https://gov.genealogy.net/ | Historical places, jurisdictions, parishes and coordinates | Authority/context, especially border and Kreis changes. |
| **GOV documented web service** — https://wiki.genealogy.net/GOV/Webservice | Machine lookup for GOV place/jurisdiction identifiers | Documented service. Cache responses and cite GOV IDs; this is context, not event evidence. |
| **GEDBAS** — https://gedbas.genealogy.net/ | User-submitted GEDCOM trees | Leads only; verify source citations independently. |
| **OFB — Online-Ortsfamilienbücher** — https://ofb.genealogy.net/ | Reconstructed local family books by town/parish | Authored derivative work. Valuable synthesis, but inspect cited church/civil records. |
| **Historische Adressbücher** — https://adressbuecher.genealogy.net/ | Digitized/indexed address directories | Residence/occupation evidence; cite edition, place and page. |
| **Grabsteine** — https://grabsteine.genealogy.net/ | Cemetery and gravestone images/indexes | Verify visible inscription; linked relationships may be inferred. |
| **GenWiki** — https://wiki.genealogy.net/ | Locality, archive, source and society research guides | Routing/context; cite underlying source. |
| **Bundesarchiv invenio** — https://invenio.bundesarchiv.de/ | German federal archival catalog, military, displaced-person and government records | Official catalog/manual; access/privacy restrictions apply. |
| **Arolsen Archives** — https://collections.arolsen-archives.org/ | Nazi persecution, forced labor, displacement and postwar tracing | Document-level scans/manual; cite document ID. |
| **Austrian State Archives** — https://www.archivinformationssystem.at/ | Central Austrian archive catalog, military and imperial records | Official catalog/manual. |
| **Austrian regional archives** | Provincial archive portals for Vienna, Lower Austria, Upper Austria, Styria, Tyrol, Salzburg, Carinthia, Burgenland and Vorarlberg | Land, probate, citizenship, military, estate and municipal records. Route by historical crown land. |
| **ANNO — Historische Zeitungen und Zeitschriften** — https://anno.onb.ac.at/ | Austrian historical newspapers and periodicals | OCR/manual; verify page image. |

**German query pack:** `Kirchenbuch`, `Taufregister`, `Trauregister`,
`Heiratsregister`, `Sterberegister`, `Standesamt`, `Personenstandsregister`,
`Familienregister`, `Melderegister`, `Einwohnermeldekartei`, `Adressbuch`,
`Bürgerbuch`, `Grundbuch`, `Nachlassakte`, `Auswanderer`, `Kreis`, `Landeskirche`,
`Pfarramt`, `Staatsarchiv`.

## Italy, Spain, Portugal, and Latin America

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **Portale Antenati** — https://antenati.cultura.gov.it/ | Italian state-archive civil registration: Napoleonic, Restoration and unified Italy periods | Free/manual indexes/images. Cite State Archive, series, comune, register, act and image. |
| **Sistema Archivistico Nazionale** — https://san.beniculturali.it/ | Italian archive descriptions and institution routing | Catalog/context; resolve to the holding archive. |
| **Archivio di Stato directory** — https://archivi.cultura.gov.it/archivi-di-stato | Routes to provincial State Archives | Civil duplicates, military, notarial, census and local-government records. |
| **Italian diocesan and parish archives** | Pre-civil baptism, marriage, burial, `stato delle anime`, dispensations | Manual/contact; search the historical diocese and parish, not only modern comune. |
| **BeWeb — Beni archivistici ecclesiastici** — https://beweb.chiesacattolica.it/beniarchivistici/ | Italian Catholic diocesan and ecclesiastical archive descriptions | Official church finding aid/manual; route to the diocese or parish holding the register. |
| **PARES — Portal de Archivos Españoles** — https://pares.cultura.gob.es/ | Spanish state archives, colonial, nobility, migration, military and digitized documents | Official/manual catalog/images. Capture archive, fonds, signature and image. |
| **Registro Civil (Spain)** — https://www.mjusticia.gob.es/es/ciudadania/estado-civil/registro-civil | Civil registration and certificate requests | Official/manual; privacy and proof-of-interest rules apply. |
| **Hemeroteca Digital BNE** — https://hemerotecadigital.bne.es/ | Spanish historical newspapers and periodicals | OCR/manual; verify page. |
| **Portal de Archivos de Andalucía** — https://www.juntadeandalucia.es/cultura/archivos/ | Andalusian regional archive network and digitized collections | Official/local routing and catalog. |
| **Arxius en Línia (Catalonia) / Badator (Basque Country)** — https://arxiusenlinia.cultura.gencat.cat/ ; https://www.artxibo.euskadi.eus/ | Regional civil, notarial, judicial, institutional and historical archive catalogs/images | Official regional portals/manual; search Catalan/Basque and Spanish place forms. |
| **Digitarq — Arquivos Nacionais/TT** — https://digitarq.arquivos.pt/ | Portuguese national and district archive descriptions/images | Official/manual; many district archives run Digitarq instances. Cite archive, fonds/book and image. |
| **Tombo.pt** — https://tombo.pt/ | Routing index to Portuguese parish books by district/concelho/parish | Discovery layer; cite the district archive image. |
| **Portal Português de Arquivos** — https://portal.arquivos.pt/ | Aggregated Portuguese archival descriptions and participating repositories | Official network/manual; follow the result to its holding archive and Digitarq record. |
| **Hemeroteca Digital de Lisboa** — https://hemerotecadigital.cm-lisboa.pt/ | Portuguese newspapers, directories and periodicals | OCR/manual; cite publication/page. |
| **Arquivo Nacional do Brasil — SIAN** — https://sian.an.gov.br/ | Brazilian national archival catalog, immigration, government and audiovisual records | Official/manual; record fonds/item. |
| **Arquivo Nacional — Entrada de Estrangeiros / registro civil do Rio** — https://www.gov.br/arquivonacional/pt-br/servicos/acervos | Official guides and digitized/indexed immigration and Rio de Janeiro civil-registration holdings | Official/manual; follow the guide to the database or archival series and record reference. |
| **Hemeroteca Digital Brasileira** — https://memoria.bn.gov.br/ | Brazilian newspapers, journals, directories and publications | OCR/manual; verify page image. |
| **FamilySearch catalog plus local cartórios/paróquias** | Latin American civil and Catholic registers | Use global catalog only to find the local creating authority/film; preserve local archive/parish citation. |
| **Archivo General de la Nación México** — https://www.gob.mx/agn | Mexican national archival guidance and collections | Official catalog/request; state and diocesan archives hold most vital records. |
| **Archivo General de la Nación Argentina** — https://www.argentina.gob.ar/interior/archivo-general | National immigration, census, government and photographic collections | Official/manual; provinces and civil registries hold vital records. |
| **AGN Argentina — antecedentes migratorios** — https://www.argentina.gob.ar/interior/archivo-general-de-la-nacion/consulta-de-antecedentes-migratorios | Official request/search workflow for historical migration-arrival information | Official/manual/request; corroborate index output with the manifest or archival record. |
| **Centro de Estudios Migratorios Latinoamericanos (CEMLA)** — https://cemla.com/ | Argentina passenger-arrival index | Manual/index; confirm ship manifest or archive record. |
| **Archivo Nacional de Chile** — https://www.archivonacional.gob.cl/ | Chilean national, notarial, judicial and administrative holdings | Official/manual/catalog; Civil Registry handles certificates. |
| **SINAR Chile** — https://sinarchile.archivonacional.gob.cl/ | Chilean national and regional archival descriptions | Official catalog/manual; a description proves custody, not the named event. |
| **Archivo General de la Nación Uruguay** — https://www.gub.uy/ministerio-educacion-cultura/archivo-general-nacion | Uruguayan national archival collections | Official/manual; civil/parish sources may remain local. |

**Italian:** `stato civile`, `atto di nascita`, `atto di matrimonio`, `atto di
morte`, `allegati`, `processetti`, `indice decennale`, `registro parrocchiale`,
`battesimo`, `stato delle anime`, `lista di leva`, `ruolo matricolare`.

**Spanish:** `registro civil`, `partida de nacimiento`, `matrimonio`, `defunción`,
`libro parroquial`, `bautismo`, `expediente matrimonial`, `padrón de habitantes`,
`censo`, `protocolo notarial`, `expediente militar`, `archivo diocesano`.

**Portuguese:** `registro civil`, `assento de nascimento`, `casamento`, `óbito`,
`livro paroquial`, `batismo`, `habilitação de casamento`, `passaporte`, `inventário`,
`testamento`, `arquivo distrital`, `freguesia`, `concelho`.

## Scandinavia and the Baltics

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **Riksarkivet Digitala forskarsalen (Sweden)** — https://sok.riksarkivet.se/ | Church books, household examinations, censuses, estate, military and archive catalog | Free/manual plus documented APIs/IIIF/datasets for selected material. |
| **Riksarkivet data APIs** — https://sok.riksarkivet.se/en/data-api | Documented APIs and downloadable datasets for eligible Swedish archival data | Use published endpoints and age/rights limits; preserve dataset/API version and verify indexed data against scans. |
| **SvenskaGravar / Gravar.se** — https://www.svenskagravar.se/ ; https://gravar.se/ | Participating Swedish cemetery and burial databases | Manual/derivative. Verify with cemetery register or visible monument. |
| **ArkivDigital (Sweden)** — https://www.arkivdigital.se/ | Color images and indexes for Swedish church, population, estate and military records | Subscription/manual; cite archive series/volume/image. |
| **Sveriges dödbok / Släktdata projects** — https://www.slaktdata.org/ | Society indexes and downloadable local transcriptions | Derivative index; verify in Riksarkivet/ArkivDigital. |
| **Digitalarkivet (Norway)** — https://www.digitalarkivet.no/ | Church books, censuses, emigration, probate, property, court and military records | Free/manual; scans are primary surrogates, transcriptions are indexes. |
| **Historisk befolkningsregister / National Library newspapers** — https://histreg.no/ ; https://www.nb.no/search?mediatype=aviser | Norwegian historical population links and digitized newspapers | Population links are derivative hypotheses; newspaper OCR is discovery evidence. Verify records/pages. |
| **Gravminner i Norge** — https://www.slektogdata.no/gravminner | Norwegian cemetery/gravestone database | Derivative plus images; verify visible inscription/burial register. |
| **Arkivalieronline / Rigsarkivet (Denmark)** — https://www.sa.dk/ao-soegesider/da/ | Church books, censuses, probate, military and archival scans | Free/manual; cite archive, parish, book/page. |
| **Copenhagen Police Register Sheets** — https://kbharkiv.dk/brug-samlingerne/kilder-paa-nettet/politiets-registerblade/ | Copenhagen residence, movement, occupation and household registration | Official city archive images/index; cite sheet and image. |
| **Dansk Demografisk Database** — https://www.ddd.dda.dk/ | Danish census, emigration and selected transcriptions | Free/manual index; verify scan. |
| **Kansallisarkisto Astia (Finland)** — https://astia.narc.fi/uusiastia/ | Finnish national archive catalog and digital records | Free/manual; Swedish and Russian-era terminology may apply. |
| **National Library of Finland digital collections** — https://digi.kansalliskirjasto.fi/ | Newspapers, journals, ephemera and digitized publications | OCR/manual; verify page image and publication metadata. |
| **HisKi — Genealogical Society of Finland** — https://hiski.genealogia.fi/ | Finnish parish-event transcriptions | Free/manual derivative index; inspect parish book image. |
| **Katiha (Finnish National Archives)** — https://katiha.kansallisarkisto.fi/ | Karelia parish-register transcriptions and searches | Official derivative index/manual; verify against the associated church-book image. |
| **Finland's Family History Association** — https://www.sukuhistoria.fi/ | Church-book and other scans | Free/member/manual; cite original archive/book. |
| **Tímarit.is (Iceland)** — https://timarit.is/ | Icelandic newspapers and periodicals | OCR/manual; verify page. |
| **National Archives of Iceland** — https://skjalasafn.is/ | Census, church, probate and national archival guidance | Official/manual; local interfaces vary. |
| **Rahvusarhiiv AIS / Saaga (Estonia)** — https://ais.ra.ee/ ; https://www.ra.ee/dgs/explorer.php | Estonian archival catalog and digitized church, census, estate and personal records | Free/manual images; search German and Russian historical forms too. |
| **DIGAR newspapers and open data (Estonia)** — https://dea.digar.ee/ ; https://data.digar.ee/ | Historical newspapers plus documented open datasets | OCR/data discovery; cite publication/page and verify scan. |
| **Raduraksti (Latvia)** — https://raduraksti.arhivi.lv/ | Latvian church books, revision lists, censuses and related scans | Registration/manual; search Latvian, German and Russian names/places. |
| **Latvian National Archives databases** — https://eresursi.arhivi.gov.lv/ | Archival catalog and digital resources | Official/manual; dataset coverage varies. |
| **Periodika.lv / Cemety.lv** — https://periodika.lv/ ; https://cemety.lv/ | Latvian digitized press and participating cemetery records | OCR/cemetery indexes are derivative; inspect page or burial/marker evidence. |
| **ePaveldas (Lithuania)** — https://www.epaveldas.lt/ | Lithuanian digitized cultural heritage, newspapers and some church records | Free/manual; cite contributing archive/item. |
| **EAIS — Lithuanian Electronic Archive Information System** — https://eais.archyvai.lt/ | State archive descriptions and digital reading-room material | Official/manual; login or anti-bot controls may apply. Never automate around them. |
| **Cemety.lt** — https://cemety.lt/ | Participating Lithuanian cemetery and burial data | Manual/local derivative evidence; confirm against the cemetery register or marker. |
| **Lithuanian State Historical Archives** — https://lvia.archyvai.lrv.lt/ | Church, nobility, estate and civil holdings | Official catalog/request; Polish, Latin, Russian, Yiddish/Hebrew may occur. |

**Swedish:** `kyrkbok`, `födelse- och dopbok`, `lysnings- och vigselbok`,
`död- och begravningsbok`, `husförhörslängd`, `församlingsbok`, `mantalslängd`,
`bouppteckning`, `in- och utflyttningslängd`.

**Norwegian/Danish:** `kirkebok`, `fødte og døpte`, `viede`, `døde og begravede`,
`folketelling`, `skifte`, `utflyttede`, `lægdsrulle`, `sjømannsrulle`.

**Finnish:** `rippikirja`, `syntynet`, `kastetut`, `vihityt`, `kuolleet`,
`henkikirja`, `muuttaneet`, `perukirja`; also Swedish equivalents.

## Central, Eastern, and Southeastern Europe

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **Porta fontium** — https://www.portafontium.eu/ | Czech-Bavarian border archives and church books | Free/manual scans. |
| **Acta Publica / Moravian Provincial Archive** — https://www.mza.cz/actapublica/ | Moravian parish-register images | Free/manual; cite archive, parish, book and image. |
| **Czech regional archives** — https://www.mvcr.cz/archivy/ | Directory/routing for state regional archives | Official routing; portals differ by region. |
| **Slovak State Archives** — https://www.minv.sk/?statne-archivy-na-slovensku | Archive directory, church/civil, census, notarial and local records | Official/manual/request; many images also via FamilySearch. |
| **Slovakiana — 1930 census sheets** — https://slovakiana.sk/scitacie-harky | Digitized 1930 Slovak census sheets where released | Official cultural portal/manual. Cite sheet, municipality and household. |
| **Hungarian National Archives** — https://mnl.gov.hu/ | National/county archives, civil, church, census, nobility, military and maps | Official catalog/manual; route to county archive and historical county. |
| **MNL AdatbázisokOnline** — https://adatbazisokonline.mnl.gov.hu/ | Hungarian National Archives searchable databases, including migration, census, military, maps and thematic projects | Official/manual. Database-specific coverage and evidence quality vary; follow the record reference. |
| **Hungaricana** — https://hungaricana.hu/ | Hungarian maps, censuses, urbarium, archival documents, newspapers and local histories | Free/manual/API possibilities vary; cite contributing archive/item. |
| **Romanian National Archives** — https://arhivelenationale.ro/ | National/county archive guidance, civil/church, census, military and property holdings | Official/manual; online name-level coverage is limited and county-dependent. |
| **Arhivele Naționale portal** — https://descopera.arhivelenationale.ro/ | Romanian archival descriptions and digitized material where available | Official catalog/manual. |
| **Croatian State Archives** — https://www.arhiv.hr/ | National and regional archive network, registers and archival catalogs | Official/manual; Matricula/FamilySearch coverage varies. |
| **Croatian register search** — https://www.arhiv.hr/hr-hr/Pretraga-mati%C4%8Dnih-knjiga | State Archives routing/search for surviving digitized or described parish/civil registers | Official/manual; record archive, parish, denomination, volume and dates. |
| **Slovenian archival portal SIRAnet** — https://vac.sjas.gov.si/ | Slovenian public archive descriptions and selected digital material | Official/manual catalog. |
| **Archives of Serbia** — https://arhivsrbije.rs/ | Serbian national collections and research guidance | Official/manual; civil/church material often local/regional. |
| **Serbian First World War losses database** — https://www.mod.gov.rs/eng/19604/popis-vojnih-i-civilnih-gubitaka-kraljevine-srbije-u-ljudstvu-u-prvom-svetskom-ratu | Military and civilian losses of the Kingdom of Serbia | Official military compilation; follow source/reference and resolve homonyms. |
| **Bulgarian State Archives** — https://www.archives.government.bg/ | Bulgarian central/regional archive catalog and digital exhibitions | Official/manual; name-level online records are sparse. |
| **ИСДА — Information System of the State Archives (Bulgaria)** — https://isda.archives.government.bg:84/ | Bulgarian archival descriptions and selected digital objects | Official catalog/manual; search fonds/place/creator and retain archive references. |
| **Greek General State Archives (GAK)** — https://www.gak.gr/ | Greek national/regional archives, municipal, electoral, school, refugee and notarial holdings | Official/manual; civil registers often remain municipal. |
| **Greek digital archive portal** — https://arxeiomnimon.gak.gr/ | Archival descriptions and selected digitized records | Official/manual; inspect item provenance. |
| **Cyprus State Archives** — https://www.mjpo.gov.cy/mjpo/statearchive/ | Colonial and government records | Official/manual; civil/church records have separate custodians. |
| **Cyprus access-to-records service** — https://www.gov.cy/en/service/access-to-records/ | Government procedure for inspecting/requesting archival records | Official/manual/request; scope, privacy and copying rules apply. |
| **Ottoman Archives / Turkish State Archives** — https://www.devletarsivleri.gov.tr/ | Ottoman and Republican government records, population and administrative collections | Registration/catalog/request; Ottoman Turkish expertise required. Not a simple vital-record index. |
| **Turkish State Archives catalog** — https://katalog.devletarsivleri.gov.tr/ | Searchable Ottoman and Republican catalog | Official/account/manual; catalog hits are archival finding aids. |
| **Hrant Dink Foundation archive / Houshamadyan** — https://archive.hrantdink.org/?l=en ; https://www.houshamadyan.org/ | Armenian community, place, school, family, testimony, photograph and memory collections from former Ottoman localities | Institutional/community sources; preserve collection provenance and distinguish testimony from civil/parish evidence. |
| **Ukrainian metric-book union catalog** — https://genealogia.com.ua/ | Cross-archive coverage guide for surviving Ukrainian metric books by place, gubernia, district, eparchy and confession | Manual/coverage index. Use it to identify an archive and fonds; it is not proof of an event. |
| **Reabilitovani istoriieiu — National Bank of Repressed Persons** — https://www.reabit.org.ua/nbr/ | Ukraine-wide regional volumes and records concerning Soviet political repression | Manual compiled index/context. Follow references to the oblast volume and archival file. |
| **Pamyat Naroda / OBD Memorial** — https://pamyat-naroda.ru/ ; https://obd-memorial.ru/ | Soviet military service, awards, losses, burials and wartime documents, including people from many present-day countries | Official document portals/manual. Cite each document image and archive reference; transliteration and duplicate identities require care. |
| **Открытый список / Open List** — https://ru.openlist.wiki/ | Collaborative index to Soviet political-repression records across former USSR jurisdictions | Discovery/context only; follow cited case, archive and publication. |

**Czech/Slovak:** `matrika`, `narození/narodení`, `křty/krsty`,
`sňatky/sobáše`, `úmrtí/úmrtia`, `sčítání lidu/sčítanie`, `pozemková kniha`,
`domovský list`, `státní/štátny archiv`.

**Hungarian:** `anyakönyv`, `születési`, `keresztelési`, `házassági`, `halotti`,
`népszámlálás`, `lakcímjegyzék`, `telekkönyv`, `megyei levéltár`.

**Romanian:** `registre de stare civilă`, `nașteri`, `căsătorii`, `decese`,
`registre parohiale`, `recensământ`, `fond arhivistic`, `arhive județene`.

**South Slavic:** `matične knjige`, `rođeni/rojstne`, `vjenčani/poročeni`,
`umrli`, `popis stanovništva`, `državni arhiv`, `župne/crkvene knjige`.

**Greek:** `ληξιαρχικές πράξεις`, `γεννήσεις`, `γάμοι`, `θάνατοι`, `μητρώο
αρρένων`, `δημοτολόγιο`, `ενοριακά βιβλία`, `Γενικά Αρχεία του Κράτους`.

## United Kingdom, Ireland, Isle of Man, and Channel Islands

For a deeper county-, repository-, and record-type catalog with evidence roles and
query vocabulary, see [uk-ireland-local-sources.md](uk-ireland-local-sources.md).

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **FreeBMD / FreeREG / FreeCEN** — https://www.freeukgenealogy.org.uk/ | England/Wales civil indexes, parish transcriptions and census transcriptions | Free/manual/open-data under project terms. Verify certificate/register/census image. |
| **GRO England and Wales** — https://www.gro.gov.uk/gro/content/certificates/ | Official civil index and certificate/PDF ordering | Manual/account; certificate is stronger than index. |
| **The National Archives Discovery** — https://discovery.nationalarchives.gov.uk/ | Central government and contributed local archive catalog | Manual/API under current terms; cite catalogue reference and record image/file. |
| **ARCHON Directory** — https://discovery.nationalarchives.gov.uk/find-an-archive | UK archive and record-office directory | Route to county, borough, university, diocesan and specialist repositories. |
| **ScotlandsPeople** — https://www.scotlandspeople.gov.uk/ | Scottish statutory registers, census, church, wills and valuation rolls | Official/manual/pay-per-view images. |
| **National Library of Scotland Maps** — https://maps.nls.uk/ | Historical maps, estate, town and Ordnance Survey mapping | Place/property context; cite map sheet/date. |
| **People's Collection Wales** — https://www.peoplescollection.wales/ | Welsh local archives, photographs, oral history and documents | Aggregator/local contributions; follow holding institution. |
| **Welsh Newspapers Online** — https://newspapers.library.wales/ | Digitized Welsh newspapers | OCR/manual; verify page and search Welsh/English. |
| **IrishGenealogy.ie** — https://www.irishgenealogy.ie/ | Irish civil and selected church records | Official/free/manual; image/privacy cutoffs vary. |
| **National Archives of Ireland Genealogy** — https://genealogy.nationalarchives.ie/ | 1901/1911 census, wills, transportation, military/police and other datasets | Official/free/manual. |
| **PRONI** — https://www.nidirect.gov.uk/proni | Northern Ireland eCatalogue, wills, valuation, street directories, estate and church records | Official/manual/archive request. |
| **PRONI name-search databases** — https://www.proni.gov.uk/name-search | Wills, pre-1858 diocesan indexes, coroners, Ulster Covenant, Freeholders and other named datasets | Official/manual index. Open the collection-specific record and retain reference. |
| **UKBMD local indexes / Online Parish Clerks** — https://www.ukbmd.org.uk/ ; https://www.ukbmd.org.uk/online_parish_clerk | Local registrar indexes and county/parish volunteer projects | Discovery/derivative. Local indexes can expose register office and sub-district detail absent from GRO; verify the certificate/register. |
| **RootsIreland / county genealogy centres** — https://www.rootsireland.ie/ | County-based church/civil transcriptions | Subscription/manual derivative index; verify image/certificate. |
| **Griffith's Valuation / AskAboutIreland** — https://www.askaboutireland.ie/griffith-valuation/ | Property occupiers, lessors, maps and valuation pages | Indirect residence/property evidence; correlate with revision books. |
| **Registry of Deeds Index Project** — https://irishdeedsindex.net/ | Volunteer index/transcriptions of Irish deed memorials | Lead/derivative; inspect memorial image or archive copy. |
| **Manx National Heritage iMuseum** — https://www.imuseum.im/ | Isle of Man newspapers, census, parish, military and collections | Manual; item-level rights vary. |
| **Jersey Heritage Archives** — https://catalogue.jerseyheritage.org/ | Jersey archive catalog, occupation, court, property and family records | Manual/catalog/request. |
| **Priaulx Library (Guernsey)** — https://www.priaulxlibrary.co.uk/ | Guernsey genealogy, newspapers, directories and local collections | Manual/local; request/source images as available. |

**Welsh additions:** `plwyf`, `bedyddiadau`, `priodasau`, `claddedigaethau`,
`cyfrifiad`, `ewyllys`, alongside English terms.

**Irish additions:** `taifid shibhialta`, `baisteadh`, `pósadh`, `bás`, `daonáireamh`,
`luacháil`, `paróiste`; most historical cataloging remains English.

## United States, Canada, Australia, and New Zealand local routing

These federations require state/province/territory searches. Use directories to avoid
an unmaintainable list of every county.

| Service | Local scope and records | Access and evidence use |
|---|---|---|
| **NARA state archives directory** — https://www.archives.gov/research/alic/reference/state-archives.html | Routes to US state archives | Start here for state vital, probate, land, court, prison and military records. |
| **USGenWeb state/county projects** — https://www.usgenweb.org/ | Volunteer county pages, cemetery, church, tax and local transcriptions | Leads/derivative; verify official/local source. |
| **Reclaim the Records** — https://www.reclaimtherecords.org/ | Acquired US vital and government indexes/datasets | Public datasets; preserve provenance and seek certificates/images. |
| **New York State Archives** — https://digitalcollections.archives.nysed.gov/ | State government, military, institutional and selected vital/local records | Official digital collection/manual. |
| **NYC Historical Vital Records** — https://a860-historicalvitalrecords.nyc.gov/ | Digitized New York City birth, marriage and death certificates by borough and certificate number | Official/free/manual downloads. Cite borough, event, certificate number and image. |
| **Missouri Digital Heritage** — https://www.sos.mo.gov/mdh/ | Death certificates, military, naturalization, land and local collections | Official state portal; inspect document image. |
| **Illinois State Archives databases** — https://www.ilsos.gov/departments/archives/databases.html | State/county marriage, death, military, land, probate and local-government indexes | Official/manual finding aids; request or inspect the underlying record. |
| **Michiganology vital records** — https://michiganology.org/vital-records/ | Michigan historical death certificates and related state records | Official state archive portal; cite certificate/image and registration details. |
| **Washington State Digital Archives** — https://digitalarchives.wa.gov/ | Birth, marriage, death, naturalization, census and government records | Official searchable state archive. |
| **Minnesota People Records Search** — https://www.mnhs.org/search/people | Minnesota births, deaths, state censuses, veterans' graves and First World War records | Official society/state partner index and images where available. |
| **Library of Virginia Chancery Records Index** — https://www.lva.virginia.gov/chancery/ | Virginia county/city chancery causes, many with digitized case files | Official index/images; case packets can establish kinship indirectly. Cite locality, case and image. |
| **BLM General Land Office Records** — https://glorecords.blm.gov/ | US federal land patents, survey plats and tract books | Official/manual images/data; useful for residence, associates and property identity, not direct kinship unless stated. |
| **California Digital Newspaper Collection** — https://cdnc.ucr.edu/ | California historical newspapers | OCR/manual; verify page. |
| **Library and Archives Canada Collection Search** — https://recherche-collection-search.bac-lac.gc.ca/eng/ | Federal census, immigration, military, land and archival records | Official/manual; cite MIKAN/item. |
| **LAC provincial, territorial, and religious archive links** — https://www.canada.ca/en/library-archives/collection/research-help/genealogy-family-history/links.html | Current official routing page for provincial/territorial archives and civil/church record custodians | Search province for vital, land, probate and local-government records. |
| **BAnQ Advitam / collections (Québec)** — https://advitam.banq.qc.ca/ | Québec civil/notarial, census, land, judicial and archival descriptions | Official/manual; French query terms and notarial districts matter. |
| **Royal BC Museum genealogy search** — https://genealogy.royalbcmuseum.bc.ca/ | British Columbia historical birth, marriage, death, colonial marriage and baptism indexes | Official/manual. Order or inspect the registration where available. |
| **Provincial Archives of New Brunswick databases** — https://archives.gnb.ca/Search/ | Vital, land, immigration, newspapers and government databases | Official/free/manual. |
| **Nova Scotia Historical Vital Statistics** — https://archives.novascotia.ca/vital-statistics | Searchable births, marriages and deaths linked to digitized records | Official/free/manual images. |
| **Manitoba Vital Statistics Genealogy Search** — https://vitalstats.gov.mb.ca/Query.php | Historical births, marriages and deaths outside statutory privacy windows | Official/free index; order the fuller registration. |
| **Saskatchewan Genealogy Index / Provincial Archives of Alberta** — https://www.ehealthsask.ca/residents/genealogy/Pages/default.aspx ; https://www.provincialarchives.alberta.ca/how-to/search-your-genealogy | Provincial historical vital indexes and Alberta genealogy/archive guidance | Official provincial resources/manual; coverage and statutory cutoffs differ. |
| **Trove** — https://trove.nla.gov.au/ | Australian newspapers and aggregated state/library/archive metadata | API/manual; follow source institution and verify OCR image. |
| **National Archives of Australia RecordSearch** — https://recordsearch.naa.gov.au/ | Federal immigration, citizenship, military and government files | Official/manual; cite series/control symbol/item. |
| **NSW Registry Family History Search** — https://www.nsw.gov.au/family-and-relationships/family-history-search | New South Wales early church and historical civil BDM indexes | Official/free index; paid image/certificate supplies fuller evidence. |
| **Victoria BDM historical search** — https://www.bdm.vic.gov.au/search-your-family-history | Victorian historical births, marriages and deaths | Official/manual; order/download record according to current options. |
| **Public Record Office Victoria wills/probate and passenger records** — https://prov.vic.gov.au/explore-collection/explore-topic/wills-and-probates ; https://prov.vic.gov.au/explore-collection/explore-topic/passenger-records-and-immigration | Victorian probate files, wills and immigration/passenger indexes/images | Official archive/manual; cite series, item and image. |
| **Queensland family-history records** — https://www.qld.gov.au/family/family-history-research/guide | Queensland historical BDM indexes, images and certificates within published cutoffs | Official/manual; record registration identifiers. |
| **Western Australia Online Index Search Tool** — https://www.wa.gov.au/organisation/department-of-justice/online-index-search-tool | Western Australian historical births, deaths and marriages | Official/free index; order certificate for fuller evidence. |
| **Libraries Tasmania Names Index** — https://libraries.tas.gov.au/slat/records-included-in-the-names-index | Tasmanian births, census, convicts, immigration, wills and other named records | Official index/images where available; cite collection and record. |
| **Australian state archives** | Remaining state and territory archive portals | Probate, immigration, convicts, land, courts and institutions. Route by colony/state and year. |
| **Papers Past** — https://paperspast.natlib.govt.nz/ | New Zealand newspapers, journals, letters, parliamentary papers and books | Free/manual; DigitalNZ offers metadata API discovery. |
| **Archives New Zealand Collections Search** — https://collections.archives.govt.nz/ | Government, immigration, military, court, probate, land and education records | Official/manual; cite agency/series/item. |
| **New Zealand BDM Historical Records** — https://www.bdmhistoricalrecords.dia.govt.nz/ | Historical birth, death and marriage indexes within statutory cutoffs | Official/manual; order certificate/printout for full evidence. |
| **Auckland Council burial and cremation search** — https://www.aucklandcouncil.govt.nz/en/cemeteries/find-burial-cremation.html | Participating Auckland cemeteries | Official council locator; confirm dates and relationships with register/monument/vital records. |
| **Christchurch City Council cemetery records** — https://ccc.govt.nz/services/cemeteries/cemetery-records | Christchurch and Banks Peninsula interments | Official council database/manual; coverage is cemetery-specific. |

**North American query pattern:** `[state/province] archives genealogy`, `[county]
probate index`, `[state] death certificates`, `[town] city directory`, `[religion]
archives [diocese/synod]`, plus the record creator's official terminology.

## Sparse-online jurisdictions

In some countries, online name-level data is genuinely limited. Do not fill the gap
with unsourced trees. Use:

1. national and regional archive catalogs;
2. civil-registry certificate procedures;
3. diocesan/parish/community archive contacts;
4. published fonds inventories and local archival guides;
5. FamilySearch catalog film/image availability;
6. local historical/genealogical societies;
7. a bounded archive request listing place, denomination, event type and years.

This is often the correct workflow for Belarus, much of the Balkans, Greece, Cyprus,
Turkey/Ottoman material, parts of Latin America, and jurisdictions with strict living-
person or civil-register access rules.
