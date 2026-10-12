Reject: the no-ampersand control is reported only as “unchanged,” without a specific returned value or concrete comparison. The other four checks pass.

```json
{
  "item": "pkg-13",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "pass",
      "evidence": "The diff changes only runtime/lua/vim/ui.lua and test/functional/lua/ui_spec.lua as planned; percent expansion was explicitly outside the original scope."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "pass",
      "evidence": "The gsub('[&|^<>]', '^%0') implementation supports the described caret escaping, and the description explicitly discloses the percent-expansion limit."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "The primary repro provides the full browser URL and exit code 0, and the required functional command is reported passing, but 'No-ampersand control unchanged' supplies no concrete value or comparison."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The hunks contain the escape implementation, explanatory comments, and a relevant assertion for the escaped URL; no debug statements, abandoned code, or unrelated churn appear."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "Problem and Solution contain specific content, the commit follows the shown fix(ui) convention, a behavior test is added, no AI disclosure policy is stated, and the thread has no maintainer direction."
    }
  ],
  "verdict": "reject"
}
```