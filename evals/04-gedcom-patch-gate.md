# GEDCOM patch gate

**Prompt** (attach `fixtures/sample.ged`)

> Add a death date of 12 Feb 1944 for Jan Kulesza from this index entry and fix whatever else is wrong in the file.

**Pass**
- Runs `python3 scripts/gedcom_check.py evals/fixtures/sample.ged` first and reports the dangling `@S9@` and uncited assertions.
- Presents a patch table (target, change, evidence, conflicts, decision) before writing.
- Keeps the existing `ABT 1945` in a note or parallel assertion; does not overwrite silently.
- Refuses to mark the death Proven from an index alone.
- After writing, re-runs the checker with `--baseline` and shows the diff.

**Fail**
- Edits the file directly, replaces 1945, or writes no citation.
