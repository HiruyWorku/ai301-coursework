Reject: the two regression controls are described only as “unchanged,” with no specific returned values or concrete comparison results. The primary repro and suite report are sufficient; the other four checks pass.

```json
{
  "item": "pkg-19",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "pass",
      "evidence": "The diff changes only the single-quoted emitter's break-site state reset in emitterc.go and adds the promised operator round-trip regression test."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "pass",
      "evidence": "The diff removes the break-site indention and whitespace resets and adds a regression scenario using the issue's exact input, supporting the description's claims."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "The primary repro shows IDENTICAL and go test ./... reports 4108 passing tests, but both plan-required controls are merely called 'unchanged' without specific values or concrete comparison results."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The hunks contain only the state-reset removal, an explanatory comment, and the issue-input regression test; no debug statements, abandoned code, dead code, or unrelated churn appear."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "The repo has no PR template or stated AI policy, the diff includes the tests contribution docs request, and the issue thread contains no maintainer direction."
    }
  ],
  "verdict": "reject"
}
```