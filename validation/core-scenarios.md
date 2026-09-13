# Core scenario validation

Validation date: 2026-09-13.

This report preserves the historical assessment from 2026-09-13. The manifest identifies the tested version.
Changes to the current skill are validated separately through affected cases.

## Results

- Core decisions in all six first-round cases matched the pre-exercise expectations.
- First-round list formatting required rework.
- The first-round C06 deliverable SHA-256 did not match the saved file.
- After correction, core decisions and deliverable content in all six cases passed review.
- All twenty final file and model checks passed.

## Validation baseline

- Fixed input: [requests.md](core-scenarios/inputs/requests.md).
- Pre-exercise expectations: [expected.md](core-scenarios/expected.md).
- Tested version: [skill-manifest.json](core-scenarios/skill-manifest.json).
- Execution method: [run-record.md](core-scenarios/run-record.md).
- Original task: [evaluator-task.txt](core-scenarios/evaluator-task.txt).
- Original first-round outputs: [outputs/](core-scenarios/outputs/README.md).
- First-round file checks: [artifact-check.json](core-scenarios/artifact-check.json).
- Final outputs: [outputs-round2/](core-scenarios/outputs-round2/README.md).
- Final file checks: [artifact-check-final.json](core-scenarios/artifact-check-final.json).

Fixed inputs and expectations were saved before the independent evaluation session began.
The evaluator produced usable drafts following the skill, wrote C01, C05, and C06 operations to isolated JSON models, and read them back.
Review also compared fixed expectations with saved artifacts.

All six cases ran in the same independent session.
Routing records distinguish first use from reused resources, reflecting the evaluator's recorded loading behavior.
Original data, simulated object IDs, and product deliverables are all synthetic.

## Round 1 C01 Blank initialization

- Fixed input: requests.md, "C01 Blank initialization".
- Expected: produce the first batch of work ready for handoff using minimal environment configuration.
- Actual routing: [C01/route.json](core-scenarios/outputs/C01/route.json).
  - workspace-setup.
  - project-planning.
  - project-brief.
  - issue-decomposition.
  - planning-and-dependencies.
- Actual deliverables
  - [environment.md](core-scenarios/outputs/C01/environment.md): minimal environment mapping.
  - [project-brief.md](core-scenarios/outputs/C01/project-brief.md): first-version expense-tracking commitment.
  - [PKT-1.md](core-scenarios/outputs/C01/PKT-1.md): expense data capability.
  - [PKT-2.md](core-scenarios/outputs/C01/PKT-2.md): interface and response verification.
  - [PKT-3.md](core-scenarios/outputs/C01/PKT-3.md): real localStorage integration acceptance.
  - [workspace.json](core-scenarios/outputs/C01/workspace.json): one simulated Project and three issues.
- Judgment
  - [x] Reused the existing Team.
  - [x] Reused existing statuses.
  - [x] Preserved the human Assignee.
  - [x] Preserved monthly-total acceptance.
  - [x] Preserved save-failure acceptance.
  - [x] Arranged first-batch dependencies by deliverables.
  - [ ] Expressed independent list outcomes separately.
- Some first-round checkboxes combined multiple outcomes.
- Operation evidence: [operations.json](core-scenarios/outputs/C01/operations.json).

## Round 1 C02 Existing project takeover

- Fixed input: requests.md, "C02 Existing project takeover".
- Expected: organize FIN-10 using the currently effective environment and latest requirements.
- Actual routing: [C02/route.json](core-scenarios/outputs/C02/route.json).
  - workspace-setup.
  - policy.
  - multi-agent-coordination.
  - issue-lifecycle.
- Actual deliverables
  - [environment.md](core-scenarios/outputs/C02/environment.md): corrected stale mappings.
  - [FIN-10.md](core-scenarios/outputs/C02/FIN-10.md): draft date contract using the user-selected time zone.
- Judgment
  - [x] Selected the effective Project using both pages of data.
  - [x] The latest FIN-10 decision replaced the old FIN-8 recommendation.
  - [x] Preserved FIN-9's existing execution assignment.
  - [x] Produced only the authorized drafts.
- Operation evidence: [operations.json](core-scenarios/outputs/C02/operations.json).

## Round 1 C03 Vague bug

- Fixed input: requests.md, "C03 Vague bug".
- Expected: first obtain diagnostic evidence sufficient to determine the fix scope.
- Actual routing: [C03/route.json](core-scenarios/outputs/C03/route.json).
  - issue-types.
  - issue-decomposition.
  - decomposition-edge-cases.
  - Bug template.
  - Research template.
- Actual deliverables
  - [parent-bug.md](core-scenarios/outputs/C03/parent-bug.md): overall acceptance for restoring persistent storage.
  - [investigation-issue.md](core-scenarios/outputs/C03/investigation-issue.md): delivery criteria for diagnostic evidence.
  - [sequence.json](core-scenarios/outputs/C03/sequence.json): only diagnosis can start first; fix content follows its findings.
- Judgment
  - [x] Classified restoration of promised persistence behavior as a Bug.
  - [x] Kept iOS storage limits and date filtering as hypotheses.
  - [x] Investigation acceptance requires usable evidence and regression cases.
  - [x] Preserved overall acceptance for the original commitment.
- Operation evidence: [operations.json](core-scenarios/outputs/C03/operations.json).

## Round 1 C04 Large feature

- Fixed input: requests.md, "C04 Large feature".
- Expected: arrange delivery of complete CSV export around a usable contract.
- Actual routing: [C04/route.json](core-scenarios/outputs/C04/route.json).
  - issue-decomposition.
  - planning-and-dependencies.
  - feature-decomposition.
  - Feature template.
- Actual deliverables
  - [parent-feature.md](core-scenarios/outputs/C04/parent-feature.md): overall acceptance for complete export.
  - [contract.md](core-scenarios/outputs/C04/contract.md): shared query and response contract.
  - [backend.md](core-scenarios/outputs/C04/backend.md): complete query and CSV.
  - [frontend.md](core-scenarios/outputs/C04/frontend.md): interface verification using a contract-compatible double.
  - [integration.md](core-scenarios/outputs/C04/integration.md): actual browser download and data comparison.
  - [plan.md](core-scenarios/outputs/C04/plan.md): backend and frontend run concurrently after the contract; integration waits for both deliverables.
- Judgment
  - [x] Multiple consumers share one usable contract.
  - [x] Child items retain their own necessary verification.
  - [x] The parent retains the original export commitment and overall acceptance.
  - [x] Planning respects two Agents and a single review slot.
  - [ ] Accepts success at 5000 records and rejection at 5001 separately.
- The first round combined both in one checkbox.
- Operation evidence: [operations.json](core-scenarios/outputs/C04/operations.json).

## Round 1 C05 PR merged without acceptance

- Fixed input: requests.md, "C05 PR merged without acceptance".
- Expected: require rework based on the commitment of 240 records versus 80 actual records, returning to exp-implement.
- Actual routing: [C05/route.json](core-scenarios/outputs/C05/route.json).
  - issue-lifecycle.
  - policy.
  - writing.
- Actual deliverables
  - [EXP-21.md](core-scenarios/outputs/C05/EXP-21.md): effective body for fixing missing records.
  - [verification.json](core-scenarios/outputs/C05/verification.json): computed missing IDs 81–240, totaling 160 records, from the fixture summary.
  - [workspace-before.json](core-scenarios/outputs/C05/workspace-before.json): original Done state.
  - [workspace.json](core-scenarios/outputs/C05/workspace.json): updated to exp-implement.
- Judgment
  - [x] PR merge and unit tests did not replace complete-data acceptance.
  - [x] Rework continued in the original issue.
  - [x] Character and permission conditions without results remained unchecked.
  - [x] The next step locates missing records through the query path.
  - [x] Preserved steps for retesting necessary conditions.
- Operation evidence: [operations.json](core-scenarios/outputs/C05/operations.json).

## Round 1 C06 Second Agent takeover

- Fixed input: requests.md, "C06 Second Agent takeover".
- Expected: complete the JSON specification using currently effective requirements and assignment.
- Actual routing: [C06/route.json](core-scenarios/outputs/C06/route.json).
  - multi-agent-coordination.
  - handoff.
  - issue-lifecycle.
  - documentation.
- Actual deliverables
  - [docs/export-spec.md](core-scenarios/outputs/C06/docs/export-spec.md): JSON export specification.
  - [PAY-16.md](core-scenarios/outputs/C06/PAY-16.md): current JSON deliverable and verification entry points.
  - [verification.json](core-scenarios/outputs/C06/verification.json): example parsing and content comparison results.
  - [workspace-before.json](core-scenarios/outputs/C06/workspace-before.json): simulated state before takeover.
  - [workspace.json](core-scenarios/outputs/C06/workspace.json): simulated state after the update.
- Judgment
  - [x] New requirements replaced the old CSV draft.
  - [x] Took over under the assignment that A had stopped and B was the sole writer.
  - [x] The embedded PAY-15 contract supported field definitions.
  - [x] The document's JSON example parsed successfully.
  - [x] Example ordering was correct.
  - [x] Example field projection was correct.
  - [ ] Document SHA-256 matched the verification entry point.
- The first-round declared hash corresponded to an LF string, while the saved file used CRLF.
- Operation evidence: [operations.json](core-scenarios/outputs/C06/operations.json).

## First-round findings and resolution

1. List formatting required rework.
   - Location: C01/PKT-1.md, "monthly total is 185; previous-month data is excluded; empty data is 0".
   - Location: 5000- and 5001-record acceptance in C04/parent-feature.md.
   - Impact: independent outcomes could not record acceptance status separately.
   - Resolution: reviewed all six cases using the existing writing rules, separating independent information and independently failing outcomes.
2. C06 evidence version identifiers were inconsistent.
   - The actual file contained 66 CRLF sequences.
   - After normalizing CRLF to LF, SHA-256 exactly matched the value declared in the verification record.
   - Evidence: [round1-hash-difference.json](core-scenarios/round1-hash-difference.json).
   - Code location: [build_outputs.py](core-scenarios/outputs/build_outputs.py) calculated the hash from the encoded document string.
   - Impact: a successor could not verify the saved file using the declared hash.
   - Resolution: computed the hash from actual saved bytes and synchronized document verification, issue body, and simulated readback.

## Evidence boundaries

- The evaluator saved routing records according to loaded and reused resources.
- C02 pagination judgments used the two pages supplied by the fixture.
- C05 set calculations used the fixture's exact ID summary.
- C06 verification covered document content and JSON examples.
- Original outputs from the first and second rounds were saved separately; corrections did not overwrite first-round evidence.

## Second-round review

- Snapshot: [outputs-round2-before-final/](core-scenarios/outputs-round2-before-final/README.md).
- Independent file checks: [artifact-check-round2.json](core-scenarios/artifact-check-round2.json).
- Lists were split by information unit.
- Document hashes matched saved bytes.
- Twenty file and model checks passed.
- C04 wording revisions introduced ambiguity in the filtered set.
  - Location: the first acceptance item in parent-feature.md.
  - Location: the first acceptance item in backend.md.
  - Location: the first acceptance item in integration.md.
  - "All records matching the date range" and the next item, "only records matching the category," conflict when the date range includes records in other categories.
  - Conditions jointly determining the data set should remain in the same acceptance judgment.
- C06 body field names differed from the specification.
  - PAY-16.md used Date, Amount, Category.
  - The JSON specification used lowercase date, amount, category.
  - Field names must match exactly.
- Review requested removing routine missing-value statements that did not affect the draft.
- The C02 phrase for "integration item" required a correction from Simplified to Traditional Chinese in the original text.

These differences were corrected with minimal document edits.
Affected model and file evidence was recalculated together.

## Corrected results

| Scenario | Adopted result | Deliverable entry point | Readback evidence |
| --- | --- | --- | --- |
| C01 | Reused minimal configuration and preserved separate acceptance items for the first batch | [Brief](core-scenarios/outputs-round2/C01/project-brief.md) | [readback](core-scenarios/outputs-round2/C01/readback.json) |
| C02 | Organized FIN-10 using the latest requirements | [FIN-10](core-scenarios/outputs-round2/C02/FIN-10.md) | [readback](core-scenarios/outputs-round2/C02/readback.json) |
| C03 | Delivered diagnostic evidence sufficient to determine fix scope first | [Investigation draft](core-scenarios/outputs-round2/C03/investigation-issue.md) | [readback](core-scenarios/outputs-round2/C03/readback.json) |
| C04 | Accepted CSV delivery against the complete filtered set | [Parent](core-scenarios/outputs-round2/C04/parent-feature.md) | [readback](core-scenarios/outputs-round2/C04/readback.json) |
| C05 | Returned missing-record correction to Implementing | [EXP-21](core-scenarios/outputs-round2/C05/EXP-21.md) | [readback](core-scenarios/outputs-round2/C05/readback.json) |
| C06 | Completed the documentation issue after verifying the JSON specification | [JSON specification](core-scenarios/outputs-round2/C06/docs/export-spec.md) | [readback](core-scenarios/outputs-round2/C06/readback.json) |

- [x] Independent information uses separate list items in all six cases.
- [x] Independently failing outcomes use separate checkboxes.
- [x] Conditions jointly determining a filtered set remain one set judgment.
- [x] C06 field names match the JSON contract.
- [x] C06 document-byte SHA-256 matches verification.
- [x] C06 document hash matches the issue body.
- [x] C06 simulated body matches the saved body.
- [x] Original fixed requirements and pre-exercise expectations retained their SHA-256 values.
- [x] All thirty skill files remained identical to the tested manifest.

Historical final C06 document SHA-256: `bf91d2e0c015f558964e67f7be06f42a0aa6a0ca6012fd73ce542b3be044857c`.

Diff references:

- C01: [List revision](core-scenarios/outputs-round2/C01/revision.diff).
- C02: [Removal of routine statements](core-scenarios/outputs-round2/C02/followup-revision.diff).
- C04: [Set semantics revision](core-scenarios/outputs-round2/C04/followup-revision.diff).
- C04: [Set equality judgment](core-scenarios/outputs-round2/C04/set-equality-revision.diff).
- C06: [Field and hash synchronization](core-scenarios/outputs-round2/C06/followup-revision.diff).
