# JA Core Application Technical Corpus Guide

## Scope

This publication contains **10,000 normalized records** from the uploaded JA Core Application Language corpus. It preserves the source program, semantic interpretation, AST, modeled compiler representation, modeled runtime representation, technical explanation, validation result, optimization notes, R12 record, MCRT record, and Smithson 8S annotation.

## Corpus profile

- Language: **JA Core Application Language**
- Profile: `ja.core`
- Source extension: `.ja`
- Records: **10,000**
- Features: **31**
- Proficiency levels: **10**
- Validation classes: **10**
- Expected pass: **7,500**
- Expected fail: **2,500**
- Native compiler execution: **not supplied**

## Files

- `JA21_JACORE_TECHNICAL_CORPUS_10000.jsonl.gz` — normalized master corpus.
- `shards/JACORE_01.jsonl.gz` through `JACORE_20.jsonl.gz` — 500-record shards.
- `JACORE_INDEX.csv` — flattened navigation and evidence index.
- `JACORE_RECORD_SCHEMA.json` — publication schema.

## Record layers

1. **Source** — complete `.ja` program text.
2. **Semantic interpretation** — meaning, judgment, types, effects, capabilities, and policy.
3. **AST** — stable node identity, source span, attributes, child role, and origin hash.
4. **Compiler representation** — frontend status, diagnostics, R12 lowering, and artifact identity.
5. **Runtime representation** — modeled JA Core VM behavior, sandbox state, and MCRT provenance.
6. **Validation result** — expected status and checks.
7. **Optimization notes** — invariants that transformations must preserve.
8. **Coupling mechanics** — explicitly labeled Smithson 8S proposed framework annotations.

## Trust boundary

The source corpus declares `actual_status: modeled_not_executed`. This suite retains that status. Structural validation verifies record integrity, source hashes, required fields, script extraction, catalogs, manifests, and packaging; it does not convert modeled compiler or runtime evidence into native execution evidence.
