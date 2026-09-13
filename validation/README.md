# Validation entry points

## Current content

Run from the repository root. Markdown parsing uses `markdown-it-py`.

```powershell
python validation/check_skill_links.py skills/linear-handbook
python validation/build_review_package.py
```

- Skill checks cover relative links, sections, entry-point reachability, and private-information markers.
- Review packaging selects Git-trackable files and checks extracted bytes and document links.
- ZIP files go in `deliverables/`; execution results go in `validation/generated/`.

## Historical behavior validation

- [Core scenarios](core-scenarios.md): drafts, simulated operations, first-round issues, and corrected deliverables for six task types.
- [Recovery scenarios](recovery-scenarios.md): simulated operations for conflicts, timeouts, partial success, and permission errors.
- [Document checks](document-checks.md): manual checks of operation documents before assembly.
- [Adopted decisions](v1-decisions.md): reasons for adopting writing and structure requirements.

```powershell
python validation/core-scenarios/check_artifacts.py outputs-round2
python validation/recovery/replay.py
```

Core checks compare saved inputs, outputs, routes, and the tested version.
`core-scenarios/tested-skill.zip` preserves the thirty files matching the tested manifest exactly.
This check does not rerun the Agent; historical results apply to the preserved skill version.
Recovery replay reruns the simulator with saved synthetic requests and compares responses and final states.

## English translation

The reports, synthetic fixtures, and recorded responses have been translated into English.
Historical judgments and tested-version hashes retain their original meaning and values.
[Recovery translation metadata](recovery/localization.json) records the translated expectation hash separately from the historical baseline.
Recovery replay verifies the translated requests, responses, and states; it is not a new assessment of Agent decisions.

## Preservation rules

- Version fixed cases, expected results, and necessary evidence.
- Preserve original judgments for failed cases and save corrected results separately.
- Replace personal paths with relative paths or isolated-directory placeholders.
- `recovery/raw/` preserves fixed simulation evidence.
- `artifacts/auth-report.md` in the permission-error case refers to a simulated remote deliverable; link checks list it separately as a simulated reference.
- Keep private execution logs in `private/`.
- Put newly generated check results in `generated/`.

After changing a workflow or template, rerun the affected cases and preserve the version tested in that run.
