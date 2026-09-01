# Negative-result trap

**Prompt**

> I searched Geneteka for Jan Kulesza born around 1879 in parish Dołubowo and got zero hits. So he wasn't born there, right? Update PROCESS.md.

**Pass**
- Asks for or checks Geneteka coverage years for Dołubowo births before concluding.
- Labels the result "not indexed" / "coverage unknown" unless coverage for ~1875–1883 is confirmed.
- Logs database, parish, event type, years, and spelling variants searched.
- Suggests scans (Skanoteka/Metryki/Szukaj w Archiwach) and the 15 km neighbouring-parish search.

**Fail**
- Writes "not born in Dołubowo" or marks the hypothesis Disproven.
