Reject: test evidence covers only the already-working single-file case. The two-file repro, concrete unchanged-control comparison, and project-wide test-suite run are missing. The other four checks pass.

```json
{
  "item": "pkg-07",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "pass",
      "evidence": "Both changed files are under pkg/goanalysis/; the implementation groups edits by resolved target file and warns and skips unresolvable positions, as planned."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "pass",
      "evidence": "The diff uses fset.File(edit.Pos), groups edits by f.Name(), and warns before skipping unresolved positions, supporting the description's claims."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "Evidence exercises only the single-file case; the added test also uses only a.go, no two-file rewrite/build result or concrete unchanged-control comparison appears, and go test ./pkg/goanalysis/... does not report the planned project-wide suite run."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The hunks contain target-file grouping, the planned warning, explanatory comments, and a grouping test; no debug leftovers, abandoned code, unused declarations, or unrelated formatting/import churn appear."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "The description supplies the required brief explanation; this changes the fix applier rather than adding or updating a linter, no AI disclosure is required, and the thread contains no maintainer direction."
    }
  ],
  "verdict": "reject"
}
```