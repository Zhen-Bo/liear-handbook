# Deliver expense persistence and monthly-total data functions

- Outcome owner: Owner/user-owner.
- Planned executor: session A.
- Project: sim-pocket-v1.

## Inputs and scope

- Input: Project brief, pocket-web/fixture-base-01.
- Exclusive write scope: src/expenses/, corresponding Vitest checks, docs/expense-contract.md.
- Define expense identity, amount, category, creation time, storage key/version, and error results.
- Deliver add, reload, and monthly-total functions with complete call examples.
- Use an injectable clock; determine the current month from the browser’s local year and month.

## Acceptance

- [ ] 85  TWD for Food and TWD 100 for Transport can be saved and reread with matching amounts and categories.
- [ ] Nonpositive or noninteger amounts are not written; write failures return an error the interface can display.
- [ ] Monthly total is 185; previous-month data excluded; empty data is 0.
- [ ] The contract includes inputs, outputs, errors, and call examples that B can integrate directly.
- [ ] Relevant Vitest checks pass; save the version and execution results.

## Next steps

1. Read the empty Vite repository and existing test configuration.
2. Define the complete contract and finish the data functions and verification.
