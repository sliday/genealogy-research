# Evals

Scenario prompts for checking that the skill changes agent behaviour. Run each prompt
in a fresh session with the skill installed and without it, then compare against the
pass criteria. `fixtures/` holds inputs.

| # | File | Tests |
|---|------|-------|
| 1 | `01-negative-result-trap.md` | Refuses to call a person "absent" without coverage |
| 2 | `02-same-name-identity.md` | Does not merge two same-name candidates on name/date alone |
| 3 | `03-scraping-temptation.md` | Chooses API/export/manual over an observed JSON endpoint |
| 4 | `04-gedcom-patch-gate.md` | Proposes a patch and runs `gedcom_check.py` instead of mutating directly |
| 5 | `05-local-language-search.md` | Searches the native-language archive first, preserves literal text |
