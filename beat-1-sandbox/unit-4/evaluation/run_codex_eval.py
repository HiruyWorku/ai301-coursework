#!/usr/bin/env python3
"""Disclosed alternative grader; does not modify or impersonate the Sonnet harness."""
import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def grade(item_id, prompt, output, expected_names):
    # Fresh session, empty working directory, package-only evidence, no gold labels.
    with tempfile.TemporaryDirectory(prefix="unit4-codex-") as isolated:
        answer = output / "responses" / f"{item_id}.md"
        command = ["codex", "exec", "--ephemeral", "--skip-git-repo-check",
                   "--sandbox", "read-only", "--ignore-user-config", "-C", isolated,
                   "-m", "gpt-6.1-sol", "-c", 'model_reasoning_effort="medium"',
                   "--json", "-o", str(answer), "-"]
        proc = subprocess.run(command, input=prompt + "\nDo not use tools. All evidence is in this prompt.",
                              text=True, capture_output=True, timeout=420)
        (output / "events" / f"{item_id}.jsonl").write_text(proc.stdout)
        if proc.returncode:
            raise RuntimeError(f"{item_id}: Codex exit {proc.returncode}: {proc.stderr[-500:]}")
        events = [json.loads(line) for line in proc.stdout.splitlines() if line.strip()]
        forbidden = {"command_execution", "mcp_tool_call", "web_search", "file_change"}
        if any(event.get("item", {}).get("type") in forbidden for event in events):
            raise RuntimeError(f"{item_id}: grader used tools instead of package-only evidence")
        raw = answer.read_text()
        blocks = re.findall(r"```json\s*(\{.*?\})\s*```", raw, re.DOTALL)
        if not blocks:
            raise RuntimeError(f"{item_id}: missing fenced JSON verdict")
        result = json.loads(blocks[-1])
        checks = result.get("checks", [])
        if result.get("item") != item_id or [c.get("name") for c in checks] != expected_names:
            raise RuntimeError(f"{item_id}: wrong item or incomplete rubric checks")
        if any(c.get("grade") not in {"pass", "fail", "unclear"} or not c.get("evidence") for c in checks):
            raise RuntimeError(f"{item_id}: invalid check grade or missing evidence")
        expected_verdict = "accept" if all(c["grade"] == "pass" for c in checks) else "reject"
        if result.get("verdict") != expected_verdict:
            raise RuntimeError(f"{item_id}: verdict contradicts required-check grades")
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--harness", type=Path, required=True)
    parser.add_argument("--skill", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    for name in ["responses", "events"]:
        (output / name).mkdir(parents=True, exist_ok=True)
    spec = importlib.util.spec_from_file_location("course_harness", args.harness)
    course = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(course)
    tool = course.load_tool(args.skill)
    if tool is None:
        raise RuntimeError("Incomplete skill")
    names = [line.split("|")[1].strip() for line in tool["rubric"].splitlines()
             if line.startswith("|") and line.rstrip().endswith("required |")]
    packages = args.harness.parent / "packages"
    ids = [f"pkg-{number:02}" for number in range(1, 21)]
    results = {}
    print("Alternative Codex evaluation: gpt-6.1-sol, medium reasoning, 20 packages", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {}
        for item_id in ids:
            prompt = course.PROMPT_TEMPLATE.format(**tool, item_id=item_id,
                                                   bundle=(packages / f"{item_id}.md").read_text())
            futures[pool.submit(grade, item_id, prompt, output, names)] = item_id
        for future in concurrent.futures.as_completed(futures):
            item_id = futures[future]
            results[item_id] = future.result()
            print(f"{item_id}: {results[item_id]['verdict']}", flush=True)
    # Gold labels are loaded only after all independent model responses exist.
    gold_path = args.harness.parent / "gold-labels.json"
    gold = json.loads(gold_path.read_text())
    items = {item["id"]: item for item in gold["items"] if not item.get("calibration")}
    categories = {}
    matched = 0
    rows = []
    for item_id in ids:
        result, reference = results[item_id], items[item_id]
        agree = result["verdict"] == reference["verdict"]
        matched += agree
        counts = categories.setdefault(reference["category"], [0, 0])
        counts[0] += agree
        counts[1] += 1
        rows.append(f"{item_id}  {reference['category']:15}  {reference['verdict']:6}  {result['verdict']:6}  {'yes' if agree else 'NO'}")
    provenance = {
        "kind": "alternative Codex evaluation, not official Sonnet harness",
        "model": "gpt-6.1-sol", "reasoning_effort": "medium",
        "cli": subprocess.check_output(["codex", "--version"], text=True).strip(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "harness_sha256": digest(args.harness), "runner_sha256": digest(Path(__file__)),
        "gold_sha256": digest(gold_path),
        "skill_sha256": {rel: digest(args.skill / rel) for rel in course.TOOL_FILES.values()},
        "package_sha256": {item_id: digest(packages / f"{item_id}.md") for item_id in ids},
        "agreement": [matched, len(ids)], "categories": categories,
        "results": [dict(results[item_id], gold=items[item_id]["verdict"],
                         category=items[item_id]["category"]) for item_id in ids],
    }
    (output / "results.json").write_text(json.dumps(provenance, indent=2) + "\n")
    transcript = [
        "# ALTERNATIVE CODEX EVALUATION — NOT THE OFFICIAL SONNET RUN",
        f"# generated by run_codex_eval.py at {provenance['timestamp']}",
        "# model: gpt-6.1-sol; reasoning: medium; " + provenance["cli"],
        "# Reason: Claude account hit its individual spend limit; user requested a disclosed Codex fallback.",
        "# Same course prompt template, frozen packages, skill files, and gold labels.",
        "# Independent package-only sessions; gold used only for scoring after all verdicts were saved.",
        "# The course's Sonnet-calibrated pass bar is not asserted for this model.",
        "# Instructor acceptance of this substitution has not been obtained.",
        f"# course harness sha256: {provenance['harness_sha256']}",
        *[f"# {rel} sha256:{value}" for rel, value in provenance["skill_sha256"].items()],
        "", "item    category         gold    verdict  agree", *rows, "",
        "categories: " + "  ".join(f"{name} {a}/{b}" for name, (a, b) in sorted(categories.items())),
        f"agreement: {matched}/20 scored items", "",
    ]
    for item_id in ids:
        transcript += [f"## {item_id}: full grader response", (output / "responses" / f"{item_id}.md").read_text(), ""]
    (output.parent / "eval-run.txt").write_text("\n".join(transcript))
    print(f"agreement: {matched}/20 scored items", flush=True)


if __name__ == "__main__":
    main()
