# Complete the import date contract for monthly-report integration

## Goal

Let the monthly-report integration successor use one contract to determine import dates and cross-month assignment.

- Type: documentation.
- Project: Ledger/proj-ledger.
- Current state: Ready/fin-ready.
- Outcome owner: Mina/user-mina.
- Suggested successor: session B.
- Source: latest FIN-10 body and Mina’s Project comment in requests.md C02.

## Adopted conclusions

- Use the user-selected time zone.
- Express date inputs in ISO format; the contract must specify the accepted forms.
- Provide the completed document to monthly-report integration.

## Deliverables

- docs/import-date-contract.md.
  - Explicit rules for accepting ISO date-only and timestamps with offsets.
  - How to obtain and apply the selected time zone, in order.
  - Determine missing-time-zone and invalid-ISO handling.
  - Input/expected-result examples across months and different browser time zones.
- Current data does not define the accepted ISO subset or missing-time-zone handling; inspect existing import and user time-zone settings contracts first, keeping ambiguities as open decisions.

## Acceptance

- [ ] Each accepted ISO form includes input, selected time zone, and an explicit result.
- [ ] Cross-month examples determine month assignment.
- [ ] The same input and selected time zone yield the same month assignment across different browser time zones.
- [ ] Invalid-input and missing-time-zone handling are directly usable by integration.
- [ ] The monthly-report integration successor can locate the document and applicable version.

## Next steps

1. Open docs/ledger-brief.md/fixture-ledger-02 and inspect existing import and time-zone contracts.
2. Document accepted ISO forms and cross-month cases in the draft.
3. Provide the completed document to monthly-report integration; schedule FIN-8 once FIN-9 artifacts are usable.
