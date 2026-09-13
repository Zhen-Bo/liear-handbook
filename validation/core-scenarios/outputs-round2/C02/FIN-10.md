# Complete the import date contract for monthly-report integration

## Goal

Let the monthly-report integration successor use one contract to determine import dates and cross-month assignment.

- Type: documentation.
- Project: Ledger/proj-ledger.
- Current state: Ready/fin-ready.
- Outcome owner: Mina/user-mina.
- Suggested successor: session B.
- Source
  - Latest FIN-10 body in Requests.md C02.
  - Mina’s latest Project comment.

## Adopted conclusions

- Use the user-selected time zone.
- Express date inputs in ISO format.
- Provide the completed document to monthly-report integration.

## Deliverables

- docs/import-date-contract.md
  - Acceptance rules for ISO date-only.
  - Acceptance rules for timestamps with offsets.
  - How to obtain the selected time zone.
  - Time-zone application order.
  - Missing-time-zone handling.
  - Invalid-ISO handling.
  - Cross-month examples.
  - Comparison examples across different browser time zones.
- To confirm
  - Currently accepted ISO subset.
  - Missing-time-zone handling.
- Confirmation method: inspect existing import and user time-zone settings contracts.
- Keep ambiguous content as open decisions.

## Acceptance

- [ ] Each accepted ISO form has a determinable result.
- [ ] Cross-month examples determine month assignment.
- [ ] The same input and selected time zone yield the same month assignment across different browser time zones.
- [ ] Invalid-input handling is usable by integration.
- [ ] Missing-time-zone handling is usable by integration.
- [ ] The monthly-report integration successor can locate the document.
- [ ] The document identifies the applicable version.

## Next steps

1. Open docs/ledger-brief.md/fixture-ledger-02.
2. Inspect the existing import contract.
3. Inspect the user time-zone contract.
4. Document accepted ISO forms.
5. Add cross-month cases.
6. Hand the completed document to monthly-report integration.

Schedule FIN-8 once the FIN-9 artifact is usable.
