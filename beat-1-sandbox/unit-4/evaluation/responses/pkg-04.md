Reject: `CHANGELOG.md` is outside the plan’s stated scope without a deviation note. The description also overstates the fallback flag set, and the test evidence lacks concrete results.

```json
{
  "item": "pkg-04",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "fail",
      "evidence": "The plan names src/pager.rs and one flag-derivation unit test; the diff also changes CHANGELOG.md without a deviation note."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "fail",
      "evidence": "The description claims the fallback uses 'the same flag set the successful probe path uses'; the fallback contains only --RAW-CONTROL-CHARS, while both successful paths include an additional flag."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "'Colors work now in paging mode' gives no concrete repro result or comparison with the less -R control; the added scenario test is accompanied only by 'cargo test passes', without a passing test count."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The hunks contain the Windows fallback change, explanatory comments, its assertion test, and a changelog entry; no debug statements, abandoned code, dead code, or unrelated formatting churn appear."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "There is no PR template, AI disclosure requirement, or maintainer direction; the diff includes the behavior-change test and CHANGELOG.md entry requested by the contribution guide."
    }
  ],
  "verdict": "reject"
}
```