# Core scenario run record

This is an English translation of the historical Chinese run.
The original files and verdicts are preserved in commit `86b6e5b` on `archive/zh-tw-baseline`.
`tested-skill.zip` and `skill-manifest.json` retain their original bytes and identify the Chinese skill tested in that run.

- Prose, fixtures, examples, generator strings, and diffs in this directory are English translations.
- Historical hashes and verdicts remain unchanged in the original fields, including the first-round hash mismatch.
- `localization.sha256` and `localizedSha256` identify translated files. The English document hash in each PAY-16 body is synchronized with its simulated workspace body.
- `check_artifacts.py` checks English fixture and artifact integrity against the preserved skill archive. Its results do not establish behavioral validation of the English skill or replace the historical verdicts.

- Date: 2026-09-13 (Asia/Taipei).
- Execution environment: Windows PowerShell.
- Evaluator: independent evaluation Agent.
- Launch mode: `fork_turns=none`.
- Input: `requests.md` and `linear-handbook/SKILL.md` in the isolated copy.
- Isolated root: `<isolated-directory>/`.
- Output scope: `outputs/` in the isolated root.
- Skill version: per-file SHA-256 in [skill-manifest.json](skill-manifest.json).
- Fixed requirements SHA-256 before launch: `5901fe874ebe7721ade1ce57adc8069e384d176e079f6cff537d8e359689f3d7`.
- Expected criteria SHA-256 before launch: `3daa6593d1f9aa9d2142eac2ebff4d4383ffab5902a5c41c9d95d2bf83131116`.

## Execution boundaries

- The evaluator received only fixed requirements and the packaged skill.
- Expected results and this report are not supplied to the evaluator.
- All six cases were processed in one independent session, with separate outputs and routes.
- All read results come from synthetic fixtures.
- Simulated updates are restricted to isolated files.
- The reviewer copies the independent output unchanged to `outputs/`, then writes a separate verdict.

## Evaluator task

Complete C01–C06 individually using the specified skill.
Save directly usable deliverables and simulated operation records for every case.
Record relative skill paths actually loaded; mark reused resources reused for this case.
Keep missing data unknown; operation records distinguish plans from actual isolated-file operations.

## Reverification entry point

1. Obtain the skill version matching skill-manifest.json.
2. Copy the skill and inputs/requests.md into a new isolated directory.
3. Create an empty output directory.
4. Start a new independent session using the first-round task in evaluator-task.txt, replacing the isolated path.
5. After the new evaluator finishes, check its original output against expected.md.

`outputs/build_outputs.py` is the English translation of the first-round evaluator’s document generation and checking code.
Rerunning it generates the translated fixture content; a new behavioral evaluation requires fresh independent requirement handling.

## Round 2

- Trigger: first-round list formatting violated writing rules.
- Trigger: first-round C06 document hash differed from saved bytes.
- Executor: original evaluation session.
- Revision inputs: original fixed requirements, original outputs, violation locations, and conceptual rules.
- Output scope: `outputs-round2/` in the isolated root.
- Round 2 is regression checking after revisions based on findings.
- First-round independent decisions and failure records remain preserved.
