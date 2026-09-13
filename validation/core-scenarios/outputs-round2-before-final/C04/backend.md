# Fetch all readable filtered expenses and generate CSV

## Inputs and scope

- Blocked by: the usable contract from contract.md.
- Executor: Agent A.
- Write location
  - src/export/.
  - Corresponding verification.
- Implementation contents
  - Complete query.
  - Permission filtering.
  - Stable sorting.
  - 5000 -record limit.
  - CSV encoding.
- Empty data: output a header.
- Over the limit: produce no file.
- Delivery entry point: implementation version callable by integration.
- Verification deliverable: data comparison evidence.

## Acceptance

- [ ] Cross-page export contains all readable data matching the date range.
- [ ] The export contains only data matching the category filter.
- [ ] Each matching record appears exactly once.
- [ ] Column order matches the contract.
- [ ] Data sorting matches the contract.
- [ ] Chinese notes match their original values after parsing.
- [ ] Comma-containing notes match their original values after parsing.
- [ ] Double-quote notes match their original values after parsing.
- [ ] Newline notes match their original values after parsing.
- [ ] 5000  records generate completely.
- [ ] 5001  records display a prompt to narrow the range.
- [ ] 5001  records create no file.
- [ ] No matches downloads a CSV with only the four-column header.
- [ ] Unreadable data never appears in the output.
- [ ] General error responses match the contract.

## Next steps

1. Read the reviewed contract version.
2. Create known multi-page data.
3. Implement the complete query.
4. Implement CSV serialization.
5. Check each acceptance criterion.
6. Save the integration entry point and verification evidence.
