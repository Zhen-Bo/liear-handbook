# Provide an interface to download CSV by date and category

## Inputs and scope

- Blocked by: the usable request/response contract from contract.md.
- Executor: Agent B.
- Write location: src/ui/export/ and corresponding interface verification.
- Submit the date range and category according to the contract; handle successful downloads and errors.
- Verify independently with contract response doubles; hand off to integration.md to connect the real backend.

## Acceptance

- [ ] The operation includes current date and category filters; full export is unaffected by current pagination.
- [ ] A successful response triggers a file download; an empty result still downloads a header file.
- [ ] Exceeding the limit prompts narrowing the range and does not trigger a download.
- [ ] General failures are understandable and allow retrying.
- [ ] Verification records state the response-double scope and delivered version.

## Next steps

1. Read the contract and prepare success, empty-data, limit-exceeded, and failure responses.
2. Implement the interface and check input/response behavior.
