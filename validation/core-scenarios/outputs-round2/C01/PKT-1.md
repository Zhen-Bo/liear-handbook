# Deliver expense persistence and monthly-total data functions

- Outcome owner: Owner/user-owner.
- Planned executor: session A.
- Project: sim-pocket-v1.

## Inputs and scope

- Input
  - [Project brief](project-brief.md).
  - Pocket-web/fixture-base-01.
- Exclusive write scope
  - src/expenses/.
  - Corresponding Vitest checks.
  - docs/expense-contract.md.
- Data contract
  - Expense identity.
  - Amount.
  - Category.
  - Creation time.
  - Storage key.
  - Data version.
  - Error results.
- Function deliverables
  - Add an expense.
  - Reread.
  - Current monthly total.
- Documentation deliverable: complete call examples.
- Clock: injectable.
- Month determination: browser local year and month.

## Acceptance

- [ ] After saving and rereading, TWD 85 Food and TWD 100 Transport match their original values.
- [ ] Nonpositive or noninteger amounts are not written.
- [ ] Write failures return an error the interface can display.
- [ ] TWD 85 and TWD 100 in the same month total TWD 185.
- [ ] Previous-month data is excluded from the current monthly total.
- [ ] Empty data has a monthly total of 0.
- [ ] The contract is sufficient for B to integrate using the call examples.
  1. Read the contract’s input and output definitions.
  2. Call data functions using the success example.
  3. Check error outcomes against error examples.
- [ ] Relevant Vitest checks pass.
- [ ] Verification records identify the tested version.

## Next steps

1. Read the empty Vite repository.
2. Check the existing test configuration.
3. Define the complete contract.
4. Complete the data functions.
5. Run verification and save the record.
