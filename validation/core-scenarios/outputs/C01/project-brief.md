# Personal expense tracker v1

## Goal

Allow individuals to add expense amounts and categories, view this month’s total, and retain data after refresh.
Requirement basis: requests.md C01.

## Adopted scope

- Persist expenses in localStorage within one browser.
- Amounts are positive integer TWD.
- Categories: Food, Transport, Other.
- Version 1 provides expense addition and the monthly total.
- Working baseline: pocket-web/fixture-base-01, Vite + TypeScript, Vitest.
- Engineering conventions for this round: record time when adding; determine the current month from browser local year/month; inject the clock to verify cross-month behavior. These are adjustable implementation choices.

## Success criteria

- [ ] After adding TWD 85 Food and TWD 100 Transport, the monthly total is TWD 185.
  1. Use isolated localStorage and a fixed current-month clock.
  2. Add two expenses through the interface.
  3. Check categories and amounts, then refresh.
  4. Confirm both records remain and the total is still TWD 185.
- [ ] 0, negative, fractional, and blank amounts do not add an expense; the interface displays corrective guidance.
- [ ] Previous-month expenses are excluded; empty data produces a monthly total of 0.
- [ ] Display the failure result when storage fails; do not report a successful addition.

## Responsibilities and entry points

- Project lead, requirement decisions, and outcome acceptance: Owner/user-owner.
- Simulated Project: sim-pocket-v1, Team team-pocket.
- Initial work
  - PKT-1: data contract, localStorage persistence, and monthly total; session A.
  - PKT-2: expense entry and monthly total interface; session B, waiting for a usable PKT-1 contract.
  - PKT-3: connect the real persistence flow and perform acceptance; session A, waiting for PKT-1 and PKT-2 artifacts.
- Next step: A checks the repository state for PKT-1, delivers a readable data contract and verified data functions.
