# Conformance and Certification Framework

## Levels

1. **Source conformance** — headers, declarations, syntax, and stable source hash.
2. **Semantic conformance** — names, types, traits, constraints, ownership, effects, and capabilities.
3. **Compiler conformance** — deterministic AST/R12 lowering and diagnostic behavior.
4. **Runtime conformance** — sandbox, resource, capability, effect, and replay behavior.
5. **Certification conformance** — signed evidence bundle, held-out cases, provenance, and limitations.

## Required test families

Positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification.

## Certification rule

A certificate may report only tests actually executed by the named implementation. Corpus-modeled outcomes may be used as expected results, but must not be relabeled as native execution evidence.
