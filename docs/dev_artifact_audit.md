# PLE starter: dev-set baseline and output-first experiment

Source: committed `artifacts/manifest.json` from the original Pi + Claude Opus 5.5 starter. This is a **historical baseline**, not an evaluation of the branch's revised prompt.

- Model: `google-cloud/claude-opus-5-5`
- Artifact generation recorded: 2026-10-20
- Dev tasks: 29
- Arithmetic mean of the 29 recorded `reward` fields: **0.491242**
- Exact 1.0 tasks: `backfeed-energization-reply`, `data-center-site-model`
- Exact 0 tasks: four (details below).

| Task | Reward | Recorded files | Observation |
| --- | ---: | ---: | --- |
| `foundation-strategy` | 0 | 0 | The recorded final message is `[tool call]`; trajectory ends on a tool call, not a completed deliverable. |
| `solar-witness-test-package` | 0 | 0 | The final message describes checking API access; no requested package is recorded. |
| `data-hall-mep-routing` | 0 | 1 | Manifest records `output/solution.py` only; the final message claims an `output/model.ifc` existed, but that generated IFC is not in the recorded deliverables. |
| `data-hall-mep-routing-offset` | 0 | 1 | Same issue: `solution.py` recorded; generated IFC not recorded. |

## Hypothesis and intervention

A plausible failure mode is **exploration and implementation without packaging the final graded files**. The trajectories and artifact manifest establish the missing recorded outputs, but do not establish why those outputs were missing or whether fixing the prompt will improve the score.

The experimental `harness.py` prompt explicitly requires: read the complete output contract, write a minimal valid deliverable early, run generators instead of submitting source code alone, use task MCP tools where available, and verify final file paths and archives before ending.

This changes executable harness content. Therefore **do not submit this branch's old `artifacts/`**: the original manifest was generated with the baseline prompt. Keep `main` and its historical artifacts intact until a legitimate run demonstrates reproducibility.

## Validation required before a scored submission

1. Run `python -m unittest discover -s tests -v` for basic prompt-contract and Python syntax checks.
2. From the **competition repository**, run `uv run python -m kit check ../ple-harness --cancel-test`. The kit requires local Docker and a working model proxy.
3. Run `uv run python eval/run.py ../ple-harness` to regenerate **all 29** dev-task artifacts under the revised harness. Do not hand-edit artifacts.
4. Run `uv run python -m kit artifacts ../ple-harness` and check exact paths, nonempty deliverables, and evaluator output; compare each task with the original manifest, especially all four zeros.
5. Commit the generated artifacts together with the changed harness, then re-run `kit check`. Only consider a scored submission if the new tested entry genuinely improves the target outcome and passes all checks.

The contest allows only three scored submissions. This proposal spends **zero** submissions and is not yet a validated leaderboard improvement.
