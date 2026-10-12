# Unit 4 — Test and Submit

## Evaluation substitution disclosure

The final official Claude Sonnet run could not complete because the course-linked Claude account returned "You've hit your individual spend limit". The full attempt produced 20 CLI errors and saved no evaluation transcript. At my request, Codex was used to complete an alternative evaluation before submission.

The alternative uses Codex CLI with gpt-6.1-sol and medium reasoning, the same four skill files, the course's exact prompt template, and all 20 frozen scored packages. Each package is graded in a fresh session using only its supplied bundle; gold labels are used for scoring after every response is saved. The original Sonnet harness and the skill were not changed. Complete verdicts, evidence, hashes, and the reproducible alternative runner are in [evaluation/](evaluation/README.md).

This is a disclosed model substitution, not an official Sonnet result. The Sonnet-calibrated pass bar is not asserted for Codex, and instructor approval for the substitution has not been obtained. I am submitting the actual alternative results alongside the completed PR and green CI and asking that the documented account limit be considered.

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s1/pull/138

GitHub username: HiruyWorku.

Opened from my fork at commit `a35b0a4`; only api/routes/health.py, pyproject.toml, and tests/unit/test_health.py are in the PR diff. Local verification: 378 unit tests passed, 53 xfailed; 18 frontend tests passed; lint, format, and targeted health-file typecheck passed. The live HTTP reproduction reports Redis healthy while the separate Postgres bug #61 keeps the overall response at 503.

The Claude live pr-precheck is blocked by the same individual spend limit as the official eval. A separate alternative Codex precheck of the captured real PR package returned **accept**, with all five required checks passing. Its full response is recorded in [evaluation/live-precheck.md](evaluation/live-precheck.md); it is explicitly labeled as a Codex result.

CI: **all five jobs passed** on commit a35b0a4: lint, typecheck, test-unit, test-integration, and frontend. [CI run](https://github.com/codepath/pathreview-ai301-fa26-s1/actions/runs/38188141003). Hosted typecheck passes; the disclosed numpy stub failure is specific to the local environment.

**Branch**

`fix/62-redis-health-check-settings`

## Eval iterations

**Run history**

Recovered from the original Claude session's actual harness outputs, in order. Calibration packages never contribute to agreement scores.

1. `--only pkg-01,pkg-03,pkg-04,pkg-12,pkg-20,calib-03 --include-calibration`: `agreement: 5/5 scored items`.
2. `--only pkg-02,pkg-05,pkg-06,pkg-07,pkg-08,pkg-09,pkg-10,pkg-11,pkg-13,pkg-14`: `agreement: 5/10 scored items`.
3. `--only pkg-02`: `agreement: 0/1 scored items`.
4. `--only pkg-05,pkg-08,pkg-11,pkg-13`: `agreement: 0/4 scored items`.
5. After revising evidence rules, `--only pkg-02,pkg-05,pkg-08,pkg-11,pkg-13,pkg-04,pkg-07,pkg-10,pkg-14,calib-04 --include-calibration`: `agreement: 7/9 scored items`.
6. `--only pkg-05,pkg-08`: `agreement: 1/2 scored items`.
7. `--only pkg-05,pkg-04,pkg-07,pkg-10,pkg-14,calib-04 --include-calibration`: `agreement: 4/5 scored items`.
8. `--only pkg-05`: `agreement: 0/1 scored items`.
9. After distinguishing repo checks from primary repro evidence, the same five scored packages and calib-04: `agreement: 5/5 scored items`.
10. `--only pkg-15,pkg-16,pkg-17,pkg-18,pkg-19`: `agreement: 4/5 scored items`.
11. `--only pkg-16`: `agreement: 0/1 scored items`.
12. After allowing named repo-wide checks to report their result without a count, `--only pkg-16,pkg-04,pkg-07,pkg-10,pkg-14,calib-04 --include-calibration`: `agreement: 5/5 scored items`.

13. Attempted full official Sonnet run: all 20 packages returned CLI errors; `agreement: 0/0 scored items`. The harness wrote no transcript. A diagnostic request returned "You've hit your individual spend limit".
14. Full **alternative Codex run**, gpt-6.1-sol with medium reasoning, using the unchanged skill: **`agreement: 17/20 scored items`**. Categories: `clear-accept 4/7`, `not-tested 4/4`, `silent-drift 4/4`, `standards-wall 2/2`, `unreviewable 3/3`. This is the final run recorded in the submitted eval-run.txt, whose header explicitly identifies the alternative grader. The official Sonnet run remains unavailable; no official PASS is claimed.

**Package analysis**

`pkg-08`, lazygit's untracked-only stash guard: the final Codex run decided `reject`; gold says `accept`. Four checks passed; "Test evidence is decisive and complete" failed. The grader's complete response is in evaluation/responses/pkg-08.md. Its deciding evidence says:

> The primary repro reports the exact toast, no prompt, and untracked.txt still listed, but the tracked-change control merely says it 'creates the stash' without a specific entry, count, or state comparison.

The package's own control text reads:

> Control: with a tracked modification staged, `s` still prompts and creates the stash.

The primary before/after is concrete: before, the prompt completes with an empty stash list; after, the exact error toast appears, no prompt opens, and untracked.txt remains listed. Codex accepted that primary evidence but interpreted the rubric's separate-control requirement more strictly, demanding a stash entry or count for the successful tracked-change control. Gold accepts the package's terse behavior report. I preserved this disagreement in the submitted score rather than replacing the grader's result. `pkg-13` and `pkg-19` also disagree on terse regression-control reports; every other package matches gold.

**Check rationale**

From the uploaded rubric's "Test evidence is decisive and complete" check, its Evidence column reads exactly:

> The PR's test-evidence section, read against every distinct failure mode the plan's test plan names as something the fix must resolve, any separate regression/unchanged-behavior controls, and the repo's own stated checks (lint, typecheck, unit tests, integration tests, or whatever the repo's PR template/docs ask for).

One exact sentence from its pass condition:

> Separate regression/unchanged-behavior controls need the same concreteness as the primary failure mode (a specific returned value, a specific "no diff"/"unchanged" confirmation tied to a real comparison — not a bare adjective), because a control is standing in for evidence about actual behavior.

Another exact sentence:

> A comment-style before/after annotation on the primary failure mode still passes when the annotated values themselves are specific and concrete (exact error text, exact exit code, exact return value); it fails when the comment asserts a match or success ("matches expected output," "now works") without showing the value itself.

The revisions distinguish a vague primary claim from a normal secondary check report. I kept concrete evidence necessary for each plan-named failure mode and control, but stopped requiring counts for lint/typecheck reports. The pkg-05 diagnostic above showed that demanding extra output for "fmt and clippy clean" rejected a package whose behavior evidence was already decisive.

**Trade-offs**

A named repo check reported as passing could be invented; this rubric cannot prove that the author ran the command. Requiring output for every secondary check would provide more material to cross-check, but it also wrongly rejected terse, complete packages. I accept that limitation while requiring concrete facts or directly relevant automated assertions plus a test count for the primary behavior. After the change, the `--only pkg-16,pkg-04,pkg-07,pkg-10,pkg-14,calib-04` canary run scored 5/5, and calib-04 still rejected because only one of its two planned failure modes was evidenced.

The Codex run shows the cost of the strict control wording: pkg-08, pkg-13, and pkg-19 were rejected even though gold accepts them. These are documented false positives; I left the skill unchanged for the model substitution so this run measures the same artifact used in the earlier Claude iterations. A different grader can interpret the same prose differently, so the Codex score is not evidence that the official Sonnet threshold was met.

Related paths: eval-run.txt in this directory, evaluation/ for alternative-run provenance and raw responses, and tools/pr-precheck/.
