# JA Core Application Architecture

```text
SOURCE (.ja)
   │
   ├── module / package / imports / policies
   ├── values / records / enums / variants
   ├── functions / generics / traits / constraints
   ├── ownership / borrow / lifetime / collections
   ├── effects / capabilities / async / streams
   └── macros / reflection / FFI / host integration
   │
   ▼
FRONTEND
   lexical structure → parse tree → typed AST → source spans
   │
   ▼
SEMANTIC GATES
   names → types → ownership → effects → capabilities → policy
   │
   ▼
R12 LOWERING
   stable statement identity → operator → dependencies → hashes
   │
   ▼
JA CORE VM / HOST ADAPTERS
   deterministic test mode → sandbox → resource accounting
   │
   ▼
MCRT EVIDENCE
   causal parents → policy status → replay identity → certificate
```

## Governing rule

A transformation is acceptable only when it preserves observable application behavior, protected-effect boundaries, capability checks, stable provenance, and the interaction order that changed the result.

## Five review lenses

- **SOPHIA — semantic integrity:** types, effects, ownership, and meaning.
- **CHARLOTTE — structural integrity:** syntax, AST shape, packages, and interfaces.
- **LANDON — executable integrity:** lowering, runtime, sandbox, and replay.
- **Professor — pedagogical integrity:** teachability, progression, and assessment.
- **Podium — publication integrity:** discoverability, consistency, and release evidence.
