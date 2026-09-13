# Fetch all readable filtered expenses and generate CSV

## Inputs and scope

- Blocked by: the usable contract and examples from contract.md.
- Executor: Agent A.
- Write location: src/export/ and corresponding verification.
- Implement complete queries, permission filtering, stable sorting, the 5000 limit, and CSV encoding.
- Empty data outputs a header; exceeding the limit produces no file.
- Deliver an implementation version callable by the integration entry point and data comparison evidence.

## Acceptance

- [ ] The multi-page data set exactly matches the expected complete readable set, each record once.
- [ ] Column order and sorting match the contract.
- [ ] Chinese, commas, quotes, and newlines match the original values after parsing.
- [ ] 0, 5000, and 5001 records meet the contract; exceeding the limit produces no file.
- [ ] Unreadable data is excluded, and applicable error checks pass.

## Next steps

1. Read the reviewed contract version and create known multi-page data.
2. Implement and verify complete queries and serialization; preserve the entry point for integration.
