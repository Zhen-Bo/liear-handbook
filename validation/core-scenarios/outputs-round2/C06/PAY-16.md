Deliver the JSON export specification.

- Fields
  - date.
  - amount.
  - category.
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
- Historical tested document SHA-256: bf91d2e0c015f558964e67f7be06f42a0aa6a0ca6012fd73ce542b3be044857c
- Hash baseline: actual saved file bytes.
- Local simulated artifact links are relative to this directory.

## Continuation entry point

1. The PAY-11 implementation successor reads docs/export-spec.md.
2. Implement output according to field definitions.
3. Check results against the sorting example.

- English document SHA-256: 890e9f3d03162c5dd7716e0d8959b0f039bac0f23aedefcecd239c99d0bbf325
