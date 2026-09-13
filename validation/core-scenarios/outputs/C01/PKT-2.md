# Provide expense entry and monthly-total interface

- Outcome owner: Owner/user-owner.
- Planned executor: session B.
- Project: sim-pocket-v1.

## Inputs and scope

- Required inputs: PKT-1’s docs/expense-contract.md and callable data functions; check versions at completion.
- Exclusive write scope: src/ui/expenses/ and corresponding interface checks.
- Amount field, Food/Transport/Other category choices, save action, and monthly total.
- Verify the interface with a contract-compatible adapter; PKT-3 maintains the integration entry point.

## Acceptance

- [ ] Successful addition displays the latest monthly total.
- [ ] Invalid amounts receive understandable, actionable guidance and do not submit an addition.
- [ ] Display an error on save failure and allow retrying after correction.
- [ ] Empty data displays 0; keyboard operation supports fields and saving.
- [ ] Save interface verification results and the export entry point for integration.

## Next steps

1. Confirm PKT-1 artifacts are readable and match the calling contract.
2. Build the interface and check behavior against success, empty-data, and failure responses.
