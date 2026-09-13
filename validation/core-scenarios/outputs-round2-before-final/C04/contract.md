# Deliver the complete shared frontend/backend export contract

## Inputs and scope

- Input: [parent-feature.md](parent-feature.md).
- Existing API limitation: current-page response only.
- Executor: Agent A.
- Delivery location: docs/export-contract.md.
- Readers: frontend/backend implementation successors.
- Filter contract
  - Date boundaries.
  - Time zone.
  - Category representation.
- Sorting contract
  - Primary sort.
  - Tie-breaker for equal sort values.
- Query contract
  - Interface for retrieving the complete filtered data set.
  - Connection to the existing paginated API.
  - Location of current-user permission checks.
  - Limit-detection method.
- Response contract
  - Successful file.
  - Empty header file.
  - Limit-exceeded error.
  - General errors.
- CSV contract
  - Encoding.
  - Special-character escaping rules.
  - Chinese example.
  - Comma example.
  - Quote example.
  - Newline example.
- Current gap: these detailed contracts have not been supplied.
- Confirmation method: check choices against existing data and APIs.
- The maintainer decides unresolved semantic conflicts.

## Acceptance

- [ ] Frontend can be implemented independently against the request/response examples.
- [ ] Backend can be implemented independently against the same contract version.
- [ ] Cross-page data sets have determinable results.
- [ ] Date boundaries have determinable results.
- [ ] Tied sort values have a determinable result.
- [ ] Unreadable data has a determinable result.
- [ ] 0 -record case defines a header-file result.
- [ ] 5000 -record case defines a complete-file result.
- [ ] 5001 -record case defines a prompt to narrow the range.
- [ ] 5001 -record case explicitly creates no file.
- [ ] Chinese text round-trips through contract serialization and parsing.
- [ ] Commas round-trip through contract serialization and parsing.
- [ ] Quotes round-trip through contract serialization and parsing.
- [ ] Newlines round-trip through contract serialization and parsing.
- [ ] The complete query is not restricted to the current page.
- [ ] Both successors can locate the adopted version.

## Next steps

1. Inspect existing data.
2. Inspect the API.
3. Complete the shared contract.
4. Add examples.
5. The maintainer reviews the contract.
6. Unblock both implementations once the contract is usable.
