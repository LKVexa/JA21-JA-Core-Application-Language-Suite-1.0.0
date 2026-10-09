# Provenance

## Source input

`JA_Core_Application_Language_Coupling_Mechanics_Corpus.jsonl.gz`

The uploaded gzip contains seven wrapper records representing:
- source corpus schema;
- 10,000-record JA Core JSONL corpus;
- source index;
- source manifest;
- source README;
- samples;
- source checksums.

## Publication transformation

The standalone suite reconstructs those documents, normalizes the 10,000 corpus records into a master file and twenty shards, extracts 1,000 exact source programs using deterministic stratified selection, builds catalogs and teaching materials, and computes a new release manifest.

## Integrity boundary

The source corpus marks actual execution as modeled. This publication does not alter that claim. Structural checks performed by the release tooling are reported separately from native parser, compiler, runtime, FFI, host, or certificate execution.
