Reject: the diff adds an out-of-scope casing test without a deviation note and omits the planned JSON regression coverage. Test evidence exercises GET header casing, rather than either planned POST JSON reproduction.

```json
{
  "item": "pkg-14",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "fail",
      "evidence": "The plan excludes header casing; the diff adds test_header_casing_preserved and omits the promised JSON regression coverage, with no deviation note."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "pass",
      "evidence": "The diff normalizes headers before the default-header merge and adds a test, supporting the description's implementation claims and generic 'Tests added' statement; the evidence reports all tests pass."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "Only GET header-casing output is provided; neither POST x=1 reproduction nor the unchanged two-header control has concrete evidence, and the added test asserts casing rather than JSON Content-Type."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The diff contains normalization logic, its called helper, an explanatory comment, and an executable test; no debug statements, abandoned code, dead code, or unrelated formatting churn appears."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "The repo has no PR template or AI disclosure requirement; a test is added and suite success is reported, and neither thread commenter provides maintainer direction."
    }
  ],
  "verdict": "reject"
}
```