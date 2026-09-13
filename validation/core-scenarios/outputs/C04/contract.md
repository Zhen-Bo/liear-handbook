# Deliver the complete shared frontend/backend export contract

## Inputs and scope

- Input: parent-feature.md; the existing query API provides only current-page responses.
- Executor: Agent A.
- Delivery location: docs/export-contract.md, used by both implementation sub-issues.
- Define date boundaries, time zone, category representation, stable sorting, and tie-breakers.
- Define the interface for retrieving all filtered data and its connection to the existing paginated API.
- Define where current-user permission checks occur and how limits are detected.
- Define successful file responses, empty header files, limit-exceeded responses, and general errors.
- Define CSV encoding and special-character escaping; provide Chinese, comma, quote, and newline cases.
- These contract details are missing; inspect existing data/APIs and record choices first. The maintainer decides unresolved conflicts constrained by existing product semantics.

## Acceptance

- [ ] Frontend and backend can be implemented independently against the same request/response examples.
- [ ] Cross-page data, date boundaries, sort ties, and unreadable data all have determinable results.
- [ ] 0, 5000, and 5001 records have explicit file or error outcomes.
- [ ] Special characters round-trip through contract serialization and parsing.
- [ ] The contract does not treat the current page as the complete data set; both implementation sub-issues can locate the adopted version.

## Next steps

1. Inspect existing data and APIs, then complete the shared contract and examples.
2. Unblock both implementations after the maintainer reviews the usable version.
