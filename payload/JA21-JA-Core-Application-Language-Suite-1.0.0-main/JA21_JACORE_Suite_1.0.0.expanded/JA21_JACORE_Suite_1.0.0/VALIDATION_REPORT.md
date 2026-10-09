# Validation Report

## Result

**PASS — structural publication validation**

## Verified

- 10,000 readable technical-corpus records.
- 10,000 unique record IDs and continuous sequences 1–10,000.
- All 10,000 source SHA-256 values match the AST origin hashes.
- Exactly 1,000 `.ja` scripts.
- Exactly 1,000 CSV and JSONL script-catalog entries.
- Exactly 100 scripts from each of ten proficiency levels.
- Exact validation-class composition:
  - 400 positive
  - 150 negative
  - 100 boundary
  - 100 integration
  - 75 security
  - 50 performance
  - 50 determinism
  - 25 interoperability
  - 25 recovery
  - 25 certification
- All 31 language features represented.
- Script files are source-faithful to their linked corpus records.
- Required source header, module, and `policy no_network` declarations present.
- Script brace-balance checks pass.
- Textbook contains exactly 22 chapters and approximately 18,973 words.
- Manifest and SHA-256 inventory generated.
- Maximum relative path length: 72 characters.

## Scope limitation

A native JA Core parser, compiler, VM, package manager, FFI host, host adapter, certificate signer, or R12/MCRT runtime was not supplied. The corpus itself labels actual execution as modeled. This report validates publication structure, hashes, extraction, counts, coverage, catalogs, and packaging; it does not claim native language execution.

## Reproduction

```text
python tools/validate_suite.py .
```
