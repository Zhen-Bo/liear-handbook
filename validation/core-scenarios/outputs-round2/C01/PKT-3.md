# Complete expense workflow integration and verify persistence after refresh

- Outcome owner: Owner/user-owner.
- Planned executor: session A.
- Project: sim-pocket-v1.

## Inputs and scope

- Required inputs
  - Usable version of PKT-1 data functions.
  - Usable version of the PKT-2 interface.
- Exclusive write scope
  - Actual Vite startup entry point.
  - Required integration changes.
  - verification/pocket-v1.md.
- Connect real localStorage.
- Connect the expense interface.
- Fix gaps caused by integration.
- Perform browser acceptance against the Project brief.

## Acceptance

- [ ] After adding TWD 85 for Food and TWD 100 for Transport in the browser, the monthly total is TWD 185.
- [ ] After refresh, both expenses match the added content.
- [ ] After refresh, the monthly total is still TWD 185.
- [ ] Previous-month expenses are excluded from the current monthly total.
- [ ] Empty data totals 0.
- [ ] Amount 0 does not add an expense.
- [ ] Negative amounts do not add an expense.
- [ ] Fractional amounts do not add an expense.
- [ ] Blank amounts do not add an expense.
- [ ] Invalid amounts display corrective guidance.
- [ ] Display the failure result on storage failure.
- [ ] Do not report a successful addition when storage fails.
- [ ] Acceptance records identify the tested version.
- [ ] Acceptance records identify the browser.
- [ ] Acceptance records identify isolated data.
- [ ] Owner can locate each acceptance result from the record.

## Next steps

1. Read both artifacts.
2. Check version and interface-contract compatibility.
3. Connect the startup entry point.
4. Perform the browser acceptance above.
5. Save individual results.
