# Find why expenses disappear and define the fix scope

## Question and decision

Determine whether mobile expense loss in pocket-0.3.1 occurs during saving, rereading, or display filtering, with enough evidence to choose the fix location.
This diagnosis is a research prerequisite for the parent ”Fix expenses occasionally disappearing after saving”.

## Inputs and deliverables

- Input: requests.md C03 report, successful control, test account, and isolated browser storage.
- Output: investigation/expense-disappearance.md.
- Reproduction data: fixtures/expense-disappearance/, preserving environment, steps, and observations.
- Check evidence gaps after one controlled reproduction attempt; no time limit has been agreed.

## Evidence plan

1. Obtain the exact phone, browser version, date, and complete operation sequence.
2. Add the reported TWD 85 Food expense in isolated storage; save data snapshots and screen states before/after saving and after refresh.
3. Compare console logs, actual save calls, and date-filtering results; record only relevant network requests.
4. Rerun the desktop Chrome successful control with the same inputs.
5. Test hypotheses individually; establish causality through repeatable observations or fixed-version code evidence.
6. List the fix scope and regression cases from evidence, and update the parent.

## Acceptance

- [ ] The successor can reproduce the failure using the environment and data, or equivalent failure observations exist.
- [ ] Conclusions have traceable evidence sufficient to define the fix boundary.
- [ ] Each adopted reason distinguishes observation from inference; rejection reasons are verifiable.
- [ ] The original failure and successful control have been converted into determinable regression cases.

When only hypotheses exist or decision evidence is missing, save progress and continue this investigation.
