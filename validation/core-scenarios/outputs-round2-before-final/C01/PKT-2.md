# Provide expense entry and monthly-total interface

- Outcome owner: Owner/user-owner.
- Planned executor: session B.
- Project: sim-pocket-v1.

## Inputs and scope

- Required inputs
  - PKT-1’s docs/expense-contract.md.
  - PKT-1’s callable data functions.
- Exclusive write scope
  - src/ui/expenses/.
  - Corresponding interface checks.
- Interface contents
  - Amount field.
  - Category choices: Food/Transport/Other.
  - Save action.
  - Current monthly total.
- Interface verification: use a contract-compatible adapter.
- Integration entry-point maintainer: PKT-3.

## Acceptance

- [ ] Successful addition displays the latest monthly total.
- [ ] Invalid amounts display corrective guidance.
- [ ] Invalid amounts do not submit an addition.
- [ ] Display an error on save failure.
- [ ] Allow retrying after a save failure.
- [ ] Empty data displays a total of 0.
- [ ] Keyboard operation can complete the add flow.
- [ ] Interface verification results are saved.
- [ ] The integration successor can locate the interface export entry point.

## Next steps

1. Confirm the PKT-1 artifact version.
2. Check the calling contract.
3. Build the interface.
4. Check behavior against each acceptance criterion.
