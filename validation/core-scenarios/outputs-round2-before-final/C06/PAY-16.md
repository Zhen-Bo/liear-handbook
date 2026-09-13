Deliver the JSON export specification.

- Fields
  - Date.
  - Amount.
  - Category.
- Amount is an integer.
- Sort data by date ascending.
- Sort by id ascending within a date.
- Artifact: [docs/export-spec.md](docs/export-spec.md).
- Prerequisite source: PAY-15/fixture://pay-15/data-contract-v2.
- For PAY-11’s JSON export implementation.

## Completed items

1. Completely replace with a JSON specification.
2. Define the three output fields.
3. Add a cross-date sorting example.
4. Add a same-date id sorting example.
5. Specify empty-array output.

## Verification results

- [x] The date definition matches data-contract-v2.
- [x] The amount definition matches the integer contract.
- [x] The category definition matches the string contract.
- [x] Sorting example JSON parses successfully.
- [x] The example sorts date ascending.
- [x] The example sorts id ascending within the same date.
- [x] Empty-data output is explicitly [].

- Evidence: [verification.json](verification.json).
- Historical tested document SHA-256: 8490f7c99aed0eccef65b7f0ffc01300d3ba3a83d96b40b480707d19d6633399
- Hash baseline: actual saved file bytes.
- Local simulated artifact links are relative to this directory.

## Continuation entry point

1. The PAY-11 implementation successor reads docs/export-spec.md.
2. Implement output according to field definitions.
3. Check results against the sorting example.

- English document SHA-256: 00e711a012e15a0b955195aaa3ea7fd7160539ab374bb337ff82ddb0c7ef5fb3
