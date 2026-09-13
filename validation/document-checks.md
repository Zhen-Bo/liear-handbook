# Document checks before assembly

The following preserves manual checks of operation documents before assembly.
Each conclusion applies to the verification date and version in its original record.

## maintenance

The following preserves the scenario walkthrough results from 2026-09-12.

- [x] Feedback duplicates existing work and lacks sufficient supporting information.
  1. Preserve the source during intake checks.
  2. Check for duplicates and add the information to the existing issue.
  3. Waiting items have an owner for missing information and a return time.
- [x] Work has not been updated for a long time but already has a deliverable.
  1. Open the deliverable first.
  2. Record the valid delivery.
- [x] A prerequisite issue is still open but its input is available.
  1. Determine which operations in this item are affected.
  2. Preserve valid dependencies.
  3. Record the executable scope.
- [x] A PR is merged but deployment verification is missing.
  1. Preserve unmet conditions.
  2. Determine completion only after obtaining verification evidence following release.
- [x] A previous recurrence is unfinished and the template has changed.
  1. Check the previous and next work items.
  2. Check the scheduled content.
  3. List generation behavior as something to confirm before adoption.
- [x] A closed issue is not archived because its parent is unfinished.
  1. Check the official relationship conditions.
  2. Explain the delay using relationship state.
- [x] Maintenance time has run out while ordinary candidates remain.
  1. Save the remaining scope.
  2. Continue handling incidents through the incident process.
- [x] An incident has recovered but its permanent fix is unfinished.
  1. Record recovery evidence.
  2. Link follow-up fixes to trackable work.
  3. Add the fix deliverables and acceptance criteria.

## multi-agent-coordination

- [x] Role responsibilities and identity fields are clearly distinguished.
- [x] Executable work has selection criteria.
- [x] Claims have a recoverable assignment entry point.
- [x] Rereading before updates preserves others' effective changes.
- [x] Scope conflicts are handled according to shared resources.
- [x] Work can resume after handoff under existing authorization.
- [x] Both examples completed the scenario walkthrough step by step.
- [x] Atomic guarantees are separated from process recommendations.
- [x] Official facts have identifiable source sections.

## planning-and-dependencies

- [x] The feature selection table distinguishes deliverable stages from scheduling.
- [x] Executable work requires checking prerequisite deliverables and execution capacity.
- [x] WIP values are labeled as example settings.
- [x] B and C can run concurrently across milestones.
- [x] Starting D still requires B and C to finish.
- [x] At the end of Cycle 1, "CSV data capability available" and "the user can complete a download" receive different outcome judgments.
- [x] Official feature facts have source references and verification dates.

## project-planning

- [x] Each of the six workflow steps lists inputs.
- [x] Each of the six workflow steps lists operations.
- [x] Each of the six workflow steps lists completion criteria.
- [x] Success criteria in both examples can be judged.
- [x] Unconfirmed requirements in both examples retain their status and confirmation method.
- [x] Brief fields cover the information needed for handoff in both examples.
- [x] Feature conclusions match the official section content.

## tool-recovery

The following is a paper check performed on 2026-09-13 using the document's steps; its evidence level is a workflow walkthrough.

- [x] No search result is found after a creation timeout.
  1. Enter "unknown creation outcome".
  2. Complete the original-scope query, then perform supplementary checks.
  3. Keep the outcome unknown if creation still cannot be ruled out; there is no path to recreate.
- [x] Another person has added a paragraph before an update.
  1. Compare with the baseline.
  2. Merge this operation's changes before submitting.
  3. Read back the full text to check the added paragraph.
- [x] The third page times out.
  1. Resume from the next-page cursor saved on the second page.
  2. Merge results by ID.
  3. Complete the query only after explicitly reading the final page.
- [x] The connector returns a rate limit without a reset.
  1. Pause requests using the same credentials.
  2. Apply bounded backoff.
  3. Save progress if still limited after three attempts.
- [x] Reading works but writing is denied.
  1. Stop writing.
  2. Check scopes and connection reach.
  3. Reread the target after necessary access is restored.
- [x] Issue creation succeeds but relationship setup fails.
  1. Reuse the obtained ID.
  2. Check existing relationships.
  3. Add only the missing relationships and read back.
- [x] PUT succeeded but finalize timed out.
  1. Find existing attachment candidates.
  2. Locate by asset path, then compare downloaded bytes.
  3. Preserve an unknown outcome when confirmation is impossible; there is no path to recreate the row directly.

## workspace-setup

- [x] All seven settings explain their purpose.
- [x] All seven settings list when to adopt them.
- [x] Minimal configuration is labeled as a recommendation.
- [x] Blank environments have an initialization checklist.
- [x] Existing environments have a takeover checklist.
- [x] Environment records allow actual values to be entered individually.
- [x] Operational steps include readback after writing.
- [x] Official sources identify sections.

## decomposition-edge-cases

Check method: compare the document with the decomposition guide and prerequisite templates.

- [x] All three examples include parent integration acceptance.
- [x] Every child item has inputs.
- [x] Every child item has an identifiable output.
- [x] Every child item has a scope.
- [x] Every child item has assessable acceptance criteria.
- [x] Real dependencies correspond to necessary deliverables.
- [x] Operations that cannot run concurrently have specific reasons.
- [x] Bug diagnosis is accepted against decision evidence from the research template.
- [x] Bug fixes preserve the original template's expiry-notice contract.
- [x] Refactoring preserves the original template's target structure and entry-point behavior.
- [x] Migration preserves the original template's cutover and recovery boundaries.
- [x] Migration adds exercises for draining in-flight writes and protecting new data.
- [x] Eight local references and section targets pass checks.

## feature-decomposition

Check method: compare the example body with prerequisite documents.

- [x] All four original child items have inputs.
- [x] All four original child items have identifiable planned outputs.
- [x] All four original child items have scopes.
- [x] All four original child items have assessable acceptance criteria.
- [x] The follow-up child item for cross-page reading can be handed off independently.
- [x] Every blocker corresponds to a missing necessary deliverable.
- [x] The reason for running API and interface work concurrently is valid.
- [x] Parent acceptance covers the user's actual download flow.

## project-bootstrap

Review date: 2026-09-13.
Evidence scope: the document's paper plan and referenced guides.

- [x] Workspace configuration matches the initialization guide.
- [x] TASK-D's overall acceptance covers every success criterion in the brief.
- [x] TASK-A's contract is used by TASK-B and TASK-C.
- [x] TASK-B and TASK-C acceptance does not require each other's undelivered outputs.
- [x] TASK-D waits for real storage and interface deliverables.
- [x] Interface development for "the user can complete the to-do flow" can run concurrently with storage implementation for "to-do data can be saved reliably".
- [x] Every issue has a single deliverable boundary.
- [x] Every issue has necessary inputs.
- [x] Every issue has a deliverable location.
- [x] Every issue has checkbox acceptance criteria.
- [x] Simulated identifiers and values to replace in a real environment are identifiable.
