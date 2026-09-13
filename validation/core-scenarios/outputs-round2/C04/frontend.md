# Provide an interface to download CSV by date and category

## Inputs and scope

- Blocked by: the usable request/response contract from contract.md.
- Executor: Agent B.
- Write location
  - src/ui/export/.
  - Corresponding interface verification.
- Submit the date range.
- Submit the category filter.
- Handle successful downloads.
- Handle error responses.
- Verification method: contract response doubles.
- integration.md handles connection to the real backend.

## Acceptance

- [ ] The request includes the current date range.
- [ ] The request includes the current category filter.
- [ ] Full export requests are not restricted to the current page.
- [ ] A successful response triggers a file download.
- [ ] Empty results still download a header file.
- [ ] Exceeding the limit displays a prompt to narrow the range.
- [ ] Exceeding the limit does not trigger a download.
- [ ] General failures display understandable errors.
- [ ] Allow retrying after failure.
- [ ] Verification records state the response-double scope.
- [ ] Verification records identify the delivered version.

## Next steps

1. Read the contract.
2. Prepare success responses.
3. Prepare empty-data responses.
4. Prepare limit-exceeded responses.
5. Prepare general failure responses.
6. Implement the interface.
7. Check each acceptance behavior.
