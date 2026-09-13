# Find why expenses disappear and define the fix scope

## Question and decision

Determine which processing stage causes mobile expense loss in pocket-0.3.1, with enough evidence to choose the fix location.

- Type: research.
- Relation: prerequisite for parent ”Fix expenses occasionally disappearing after saving”.
- Investigation path
  - Save.
  - Reread.
  - Display filtering.

## Inputs and deliverables

- Input
  - Requests.md C03 report.
  - Desktop successful control.
  - Test account.
  - Isolated browser storage.
- Diagnostic output: investigation/expense-disappearance.md.
- Reproduction data: fixtures/expense-disappearance/.
  - Environment.
  - Operation steps.
  - Observation records.
- Suggested review point: check evidence gaps after one controlled reproduction attempt.
- Time limit: not yet agreed.

## Evidence plan

1. Obtain exact phone details.
2. Obtain the browser version.
3. Obtain the date at the time.
4. Obtain the complete operation sequence.
5. Add the reported TWD 85 Food expense in isolated storage.
6. Save data snapshots before and after storage.
7. Refresh and save data snapshots.
8. Save the corresponding screen state.
9. Compare console logs.
10. Trace actual save calls.
11. Compare date-filtering results.
12. Record network requests related to the failure.
13. Rerun the desktop Chrome successful control with the same inputs.
14. Test hypotheses individually; establish causality through repeatable observations or fixed-version code evidence.
15. Define the fix scope from evidence.
16. Define regression cases.
17. Update the parent with conclusions.

## Acceptance

- [ ] The successor can reproduce the failure or obtain equivalent failure observations.
- [ ] Conclusions have sufficient evidence to define the fix boundary.
- [ ] Each adopted reason distinguishes observation from inference.
- [ ] Reasons for rejected hypotheses are verifiable.
- [ ] The original failure has been converted into a determinable regression case.
- [ ] The successful control has been converted into a determinable regression case.

When only hypotheses exist or decision evidence is missing, save progress and continue this investigation.
