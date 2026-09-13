# Personal expense tracker v1

## Goal

Allow individuals to add expense amounts and categories.
Users can view the monthly total and find saved expenses after refreshing.
Requirement basis: requests.md C01.

## Adopted scope

- Storage: localStorage in one browser.
- Amount: positive integer TWD.
- Category
  - Food.
  - Transport.
  - Other.
- Version 1 capabilities
  - Add an expense.
  - View the current monthly total.
- Working baseline
  - Repository: pocket-web.
  - Version: fixture-base-01.
  - Technology: Vite + TypeScript.
  - Test tool: Vitest.
- Engineering conventions for this round, adjustable during implementation
  - Record the time when adding.
  - Determine the current month from the browser’s local year and month.
  - Inject the clock to verify cross-month behavior.

## Success criteria

- [ ] After adding TWD 85 Food and TWD 100 Transport, the monthly total is TWD 185.
  1. Use isolated localStorage.
  2. Fix the clock in the current month.
  3. Add the two expenses above through the interface.
  4. Check the displayed total is TWD 185.
- [ ] After refresh, both expense amounts and categories match the added content.
  1. Add TWD 85 Food and TWD 100 Transport through the interface.
  2. Refresh.
  3. Compare saved contents record by record.
- [ ] After refresh, the monthly total is still TWD 185.
- [ ] An amount of 0 does not add an expense.
- [ ] A negative amount does not add an expense.
- [ ] A fractional amount does not add an expense.
- [ ] A blank amount does not add an expense.
- [ ] Invalid amounts display corrective guidance.
- [ ] Exclude previous-month expenses from the current monthly total.
- [ ] Empty data has a monthly total of 0.
- [ ] Display the failure result when storage fails.
- [ ] Do not report a successful addition when storage fails.

## Responsibilities and entry points

- Project lead: Owner/user-owner.
- Requirement decision-maker: Owner/user-owner.
- Outcome reviewer: Owner/user-owner.
- Simulated Project: sim-pocket-v1.
- Team: team-pocket.
- Initial work
  - [PKT-1](PKT-1.md): data functions.
    - Executor: session A.
  - [PKT-2](PKT-2.md): expense interface.
    - Executor: session B.
    - Prerequisite: usable PKT-1 contract and data functions.
  - [PKT-3](PKT-3.md): workflow integration.
    - Executor: session A.
    - Prerequisite: PKT-1 artifact.
    - Prerequisite: PKT-2 artifact.

## Next steps

1. A checks the repository state for PKT-1.
2. Deliver the data contract.
3. Complete the data functions and their verification.
