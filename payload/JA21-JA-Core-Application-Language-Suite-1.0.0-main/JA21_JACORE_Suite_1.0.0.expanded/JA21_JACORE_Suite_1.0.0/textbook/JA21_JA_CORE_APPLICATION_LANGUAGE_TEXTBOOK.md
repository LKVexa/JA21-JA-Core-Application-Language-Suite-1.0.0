# JA21 JA Core Application Language
## Technical Textbook — Standalone Suite 1.0.0

**Profile:** `ja.core`  
**Source extension:** `.ja`  
**Corpus:** 10,000 records  
**Example pack:** 1,000 scripts  
**Status:** Provisional corpus-derived publication; native compiler/runtime execution not supplied.

---

## How to use this book

This textbook treats the language as an evidence-bearing application system. Read each program at five levels: source intent, semantic judgment, AST structure, compiler/runtime contract, and provenance. SOPHIA, CHARLOTTE, LANDON, Professor, and Podium appear as review lenses: semantic, structural, executable, pedagogical, and publication integrity. They do not imply independent autonomous execution.

## Parts

- **Part I — Application foundations:** Chapters 1–9
- **Part II — Resource and execution semantics:** Chapters 10–14
- **Part III — Compiler, runtime, and evidence:** Chapters 15–21
- **Part IV — Capstone:** Chapter 22

---

# Chapter 1 — The Core Application Language as a JA21 Suite

## Learning objectives

- Explain how `module` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Establish the language boundary, trust model, evidence stack, and relationship between application source and the larger JA21 suite.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `module`

Defines a compilation and naming boundary. Modules provide stable identity for imports, policy application, and incremental compilation.

In the corpus, `module` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00031` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `module`

```ja
ja source 0.3
module corpus.ja_core.example_00031
use Core
policy no_network

record Item33 { id: Count, label: Text }
function transform_33(item: Item33) -> Result<Item33, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item33 { id: item.id, label: normalized })
}
let sample: Item33 = Item33 { id: 33, label: "module-beginner" }
let result = transform_33(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates module at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.read} ⊢ node-91891a3bad9493dd2694 : ApplicationArtifact ! {state.write} ⇒ validated`. The AST node is `node-91891a3bad9493dd2694` and its origin hash is `ef45ad249f671394aa8af17cd4c178c400a4a7d34e579d41231b723ceb1983ea`. R12 uses operator `match` with record `r12-936eaad635cec75518f9`. The modeled runtime points to MCRT record `mcrt-c9c8afd411ad1b81b571` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Create an evidence map for a small console application and distinguish modeled corpus outcomes from native execution.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `module` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 2 — Modules, Packages, Imports, and Policies

## Learning objectives

- Explain how `module`, `package` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Explain compilation units, reusable package boundaries, imports, stable naming, initialization order, and policy declarations.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `module`

Defines a compilation and naming boundary. Modules provide stable identity for imports, policy application, and incremental compilation.

In the corpus, `module` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `package`

Groups modules and distribution metadata into a deployable application unit while preserving dependency and provenance boundaries.

In the corpus, `package` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00031` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `module`

```ja
ja source 0.3
module corpus.ja_core.example_00031
use Core
policy no_network

record Item33 { id: Count, label: Text }
function transform_33(item: Item33) -> Result<Item33, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item33 { id: item.id, label: normalized })
}
let sample: Item33 = Item33 { id: 33, label: "module-beginner" }
let result = transform_33(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates module at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.read} ⊢ node-91891a3bad9493dd2694 : ApplicationArtifact ! {state.write} ⇒ validated`. The AST node is `node-91891a3bad9493dd2694` and its origin hash is `ef45ad249f671394aa8af17cd4c178c400a4a7d34e579d41231b723ceb1983ea`. R12 uses operator `match` with record `r12-936eaad635cec75518f9`. The modeled runtime points to MCRT record `mcrt-c9c8afd411ad1b81b571` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Split a program into two modules and document every dependency and policy decision.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `module` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 3 — Constants, Immutable Bindings, and Controlled State

## Learning objectives

- Explain how `constant`, `immutable_binding`, `mutable_state` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Contrast compile-time constants, stable local values, and explicit mutation under effect and capability control.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `constant`

Declares a value whose identity is fixed for the compilation unit and may be safely folded when proof obligations are retained.

In the corpus, `constant` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `immutable_binding`

Introduces a stable local name. Immutability narrows the effect surface and improves reasoning, replay, and optimization.

In the corpus, `immutable_binding` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `mutable_state`

Declares controlled state change. Mutation must remain explicit in the effect and capability path.

In the corpus, `mutable_state` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00027` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `constant`

```ja
ja source 0.3
module corpus.ja_core.example_00027
use Core
policy no_network

record Item29 { id: Count, label: Text }
function transform_29(item: Item29) -> Result<Item29, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item29 { id: item.id, label: normalized })
}
let sample: Item29 = Item29 { id: 29, label: "constant-beginner" }
let result = transform_29(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates constant at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {process.spawn:signed} ⊢ node-5f2eeb379e255d766246 : ApplicationArtifact ! {file.write} ⇒ validated`. The AST node is `node-5f2eeb379e255d766246` and its origin hash is `f5be2c54e7f3e899b4f14cfe3dee83592f8fbaa3be0e33ca983806981e3383ab`. R12 uses operator `stream` with record `r12-a5fac7f9626ee2c8f220`. The modeled runtime points to MCRT record `mcrt-569b781dba4e89902215` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Refactor a mutable counter into a small state component and compare its effect surface with an immutable design.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `constant` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 4 — Records, Enums, and Variants

## Learning objectives

- Explain how `record`, `enum`, `variant` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Build algebraic data models whose construction, matching, serialization, and compatibility behavior are explicit.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `record`

Defines a product type with named fields and predictable serialization, construction, and pattern semantics.

In the corpus, `record` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `enum`

Defines a closed set of named alternatives suitable for exhaustive branching and stable wire representation.

In the corpus, `enum` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `variant`

Defines a tagged union whose active case is represented explicitly and checked during pattern matching.

In the corpus, `variant` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00001` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `record`

```ja
ja source 0.3
module corpus.ja_core.example_00001
use Core
policy no_network

record Item3 { id: Count, label: Text }
function transform_3(item: Item3) -> Result<Item3, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item3 { id: item.id, label: normalized })
}
let sample: Item3 = Item3 { id: 3, label: "record-beginner" }
let result = transform_3(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates record at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.read} ⊢ node-c2d0bb38419fc25adce6 : ApplicationArtifact ! {file.read} ⇒ validated`. The AST node is `node-c2d0bb38419fc25adce6` and its origin hash is `5a66a5a5e9c98afae431a0ea717fd7c90e455055508cb4d67adb80244d26fde4`. R12 uses operator `match` with record `r12-93bde4a3b7f90fe4b61a`. The modeled runtime points to MCRT record `mcrt-414dab4edeaa95dfec01` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Model an application command protocol with records and variants, then add an exhaustive dispatcher.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `record` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 5 — Functions and Closures

## Learning objectives

- Explain how `function`, `closure` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Treat callables as typed application artifacts with declared effects, captured environments, and stable identity.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `function`

Defines a typed transformation with declared inputs, outputs, effects, and capability obligations.

In the corpus, `function` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `closure`

Captures lexical bindings in a callable value; capture mode and lifetime remain part of semantic identity.

In the corpus, `closure` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00014` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `function`

```ja
ja source 0.3
module corpus.ja_core.example_00014
use Core
policy no_network

record Item16 { id: Count, label: Text }
function transform_16(item: Item16) -> Result<Item16, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item16 { id: item.id, label: normalized })
}
let sample: Item16 = Item16 { id: 16, label: "function-beginner" }
let result = transform_16(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates function at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {ledger.append} ⊢ node-9413878af45c62c7054d : ApplicationArtifact ! {pure} ⇒ validated`. The AST node is `node-9413878af45c62c7054d` and its origin hash is `d1fe891b5b33ed09d312be8c6a0104df3e16e82fe1a1a05c4ef190bb395d1425`. R12 uses operator `await` with record `r12-7f1a83ede1e765bfec12`. The modeled runtime points to MCRT record `mcrt-54dca5966114a4e1120a` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Write a pure transformation and a closure-based pipeline, then document capture and lifetime requirements.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `function` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 6 — Generics, Traits, and Constraints

## Learning objectives

- Explain how `generic`, `trait`, `constraint` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Separate reusable algorithms from the capabilities and laws required of their type parameters.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `generic`

Abstracts a definition over types or values while preserving constraints needed for valid specialization.

In the corpus, `generic` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `trait`

Describes a behavioral contract that implementations satisfy without erasing type, effect, or provenance evidence.

In the corpus, `trait` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `constraint`

Restricts generic, type, or value parameters so specialization and validation can prove required properties.

In the corpus, `constraint` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00006` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `generic`

```ja
ja source 0.3
module corpus.ja_core.example_00006
use Core
policy no_network

record Item8 { id: Count, label: Text }
function transform_8(item: Item8) -> Result<Item8, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item8 { id: item.id, label: normalized })
}
let sample: Item8 = Item8 { id: 8, label: "generic-beginner" }
let result = transform_8(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates generic at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.write} ⊢ node-5ef66fab12bb7971a43a : ApplicationArtifact ! {file.write} ⇒ validated`. The AST node is `node-5ef66fab12bb7971a43a` and its origin hash is `e313690a63015b57c2f2fd161dbd1a44cf4874fd6154a9cef9de9cbea37a8ded`. R12 uses operator `expand` with record `r12-98964b1413448967bd13`. The modeled runtime points to MCRT record `mcrt-e6e4a692251f003cd85e` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Design a generic repository interface and state the trait and constraint obligations needed for safe specialization.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `generic` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 7 — Options, Results, and Structured Errors

## Learning objectives

- Explain how `option`, `result`, `structured_error` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Represent absence and failure as typed data while retaining context, recovery classification, and causal identity.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `option`

Represents presence or absence without sentinel values, forcing the caller to handle both states deliberately.

In the corpus, `option` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `result`

Represents successful or failed computation as data, enabling typed propagation and explicit recovery.

In the corpus, `result` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `structured_error`

Carries machine-readable failure identity, context, and recovery information instead of unstructured text alone.

In the corpus, `structured_error` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00002` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `option`

```ja
ja source 0.3
module corpus.ja_core.example_00002
use Core
policy no_network

record Item4 { id: Count, label: Text }
function transform_4(item: Item4) -> Result<Item4, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item4 { id: item.id, label: normalized })
}
let sample: Item4 = Item4 { id: 4, label: "option-beginner" }
let result = transform_4(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates option at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {ledger.append} ⊢ node-314f60b7193d82ef47df : ApplicationArtifact ! {ledger.append} ⇒ validated`. The AST node is `node-314f60b7193d82ef47df` and its origin hash is `1647f95f7350c0b8f2b8708bae64b5488f0916c5c261e0a19dd2eea6fddd2263`. R12 uses operator `declare` with record `r12-cb9a6defc6d6125a9b2a`. The modeled runtime points to MCRT record `mcrt-efbe234fc6b637b54edf` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Replace sentinel and exception-like flows with Option, Result, and structured error values.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `option` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 8 — Pattern Matching and Exhaustiveness

## Learning objectives

- Explain how `pattern_match`, `enum`, `variant` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Use declarative decomposition while proving coverage, guard consistency, and stable case behavior.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `pattern_match`

Deconstructs structured values and requires coverage, guard consistency, and predictable case ordering.

In the corpus, `pattern_match` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `enum`

Defines a closed set of named alternatives suitable for exhaustive branching and stable wire representation.

In the corpus, `enum` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `variant`

Defines a tagged union whose active case is represented explicitly and checked during pattern matching.

In the corpus, `variant` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00028` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `pattern_match`

```ja
ja source 0.3
module corpus.ja_core.example_00028
use Core
policy no_network

record Item30 { id: Count, label: Text }
function transform_30(item: Item30) -> Result<Item30, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item30 { id: item.id, label: normalized })
}
let sample: Item30 = Item30 { id: 30, label: "pattern_match-beginner" }
let result = transform_30(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates pattern match at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {file.write:artifacts} ⊢ node-c56aadc577e82ed0b720 : ApplicationArtifact ! {pure} ⇒ validated`. The AST node is `node-c56aadc577e82ed0b720` and its origin hash is `9d68685d672b886e0bdf6366da5f9d96c61cea31093d466c65135fadcb68e2e6`. R12 uses operator `invoke` with record `r12-5247e4195c481e1b81bb`. The modeled runtime points to MCRT record `mcrt-9c5445021d705d762775` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Create an exhaustive state reducer and add a diagnostic case for an omitted branch.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `pattern_match` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 9 — Collections and Serialization

## Learning objectives

- Explain how `collection`, `serialization` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Connect aggregate data structures to ordering, allocation, mutation, schema, version, and wire-safety decisions.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `collection`

Provides typed aggregate storage with declared ordering, mutation, allocation, and iteration semantics.

In the corpus, `collection` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `serialization`

Maps values to stable external representations while preserving schema, version, and safety requirements.

In the corpus, `serialization` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00022` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `collection`

```ja
ja source 0.3
module corpus.ja_core.example_00022
use Core
policy no_network

record Item24 { id: Count, label: Text }
function transform_24(item: Item24) -> Result<Item24, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item24 { id: item.id, label: normalized })
}
let sample: Item24 = Item24 { id: 24, label: "collection-beginner" }
let result = transform_24(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates collection at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {file.write:artifacts} ⊢ node-38eabb628150520c6203 : ApplicationArtifact ! {file.read} ⇒ validated`. The AST node is `node-38eabb628150520c6203` and its origin hash is `43b4855340aa332bde6ef41ac34b25c0c940a126626ab94205a2e7177d26909d`. R12 uses operator `declare` with record `r12-f822bcfd1c4c23b676df`. The modeled runtime points to MCRT record `mcrt-74e32214185dd32d6f17` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Build a versioned collection export and identify compatibility and replay requirements.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `collection` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 10 — Ownership, Borrowing, and Lifetimes

## Learning objectives

- Explain how `ownership`, `borrow`, `lifetime` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Reason about resource responsibility, aliasing, mutation, references, closure captures, and finalization.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `ownership`

Assigns responsibility for resource lifetime and prevents implicit duplication or unsafe concurrent access.

In the corpus, `ownership` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `borrow`

Provides bounded access without transferring ownership; mutability and aliasing rules remain explicit.

In the corpus, `borrow` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `lifetime`

Names or infers the valid duration of references and captured resources.

In the corpus, `lifetime` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00016` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `ownership`

```ja
ja source 0.3
module corpus.ja_core.example_00016
use Core
policy no_network

record Item18 { id: Count, label: Text }
function transform_18(item: Item18) -> Result<Item18, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item18 { id: item.id, label: normalized })
}
let sample: Item18 = Item18 { id: 18, label: "ownership-beginner" }
let result = transform_18(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates ownership at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {file.write:artifacts} ⊢ node-6282216127981373cf16 : ApplicationArtifact ! {ledger.append} ⇒ validated`. The AST node is `node-6282216127981373cf16` and its origin hash is `84b21b15c548d7ab43bfdec68bbfa546f1791182c4ddbe6de385c076d2c4c859`. R12 uses operator `expand` with record `r12-3381ad1f60b6f46f7f85`. The modeled runtime points to MCRT record `mcrt-dfe9daf6999cd959cbec` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Trace ownership through a file-processing pipeline and mark each borrow and lifetime boundary.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `ownership` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 11 — Effects and Capabilities

## Learning objectives

- Explain how `effect`, `capability` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Keep observable operations and authority visible so policy, optimization, and runtime enforcement remain correct.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `effect`

Declares observable operations beyond pure evaluation so optimization and policy cannot erase behavior.

In the corpus, `effect` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `capability`

Names explicit authority required to perform protected effects such as file, state, process, or host access.

In the corpus, `capability` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00012` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `effect`

```ja
ja source 0.3
module corpus.ja_core.example_00012
use Core
policy no_network

record Item14 { id: Count, label: Text }
function transform_14(item: Item14) -> Result<Item14, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item14 { id: item.id, label: normalized })
}
let sample: Item14 = Item14 { id: 14, label: "effect-beginner" }
let result = transform_14(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates effect at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.write} ⊢ node-405f568e0cd47865b961 : ApplicationArtifact ! {state.read} ⇒ validated`. The AST node is `node-405f568e0cd47865b961` and its origin hash is `9e5adbd55a0320925edc82c2e3fe20844cb5aa43a69e0919c1591dbe762a4916`. R12 uses operator `declare` with record `r12-109bb507bd5970fe4aa7`. The modeled runtime points to MCRT record `mcrt-1389476457da9b624e47` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Define a file-writing service with the minimum effect and capability set and a denied unauthorized variant.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `effect` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 12 — Asynchronous Tasks and Streams

## Learning objectives

- Explain how `async_task`, `stream` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Model scheduling, cancellation, timeout, ordering, backpressure, completion, and deterministic testing.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `async_task`

Models a scheduled computation with cancellation, timeout, ownership, and deterministic-test obligations.

In the corpus, `async_task` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `stream`

Models ordered or bounded sequences of values over time, including backpressure and completion behavior.

In the corpus, `stream` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00029` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `async_task`

```ja
ja source 0.3
module corpus.ja_core.example_00029
use Core
policy no_network

record Item31 { id: Count, label: Text }
function transform_31(item: Item31) -> Result<Item31, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item31 { id: item.id, label: normalized })
}
let sample: Item31 = Item31 { id: 31, label: "async_task-beginner" }
let result = transform_31(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates async task at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {file.read:workspace} ⊢ node-d8826085ac6b4104c703 : ApplicationArtifact ! {file.read} ⇒ validated`. The AST node is `node-d8826085ac6b4104c703` and its origin hash is `a296064f3ded44088e94c67a238ab9a1e991967068c7d727bf1f59ba78e5a494`. R12 uses operator `foreign_call` with record `r12-8569ba1a4c2f6f6fc49d`. The modeled runtime points to MCRT record `mcrt-be3f62ff531a5ef2766e` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Create a bounded producer-consumer stream with cancellation and replay evidence.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `async_task` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 13 — Macros and Compile-Time Generation

## Learning objectives

- Explain how `macro`, `compile_time_generation` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Use syntax transformation and generated declarations without losing hygiene, source spans, generator identity, or input hashes.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `macro`

Transforms syntax under controlled expansion rules, with hygiene and source provenance retained.

In the corpus, `macro` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `compile_time_generation`

Produces declarations or artifacts before runtime while preserving generator identity and input hashes.

In the corpus, `compile_time_generation` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00008` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `macro`

```ja
ja source 0.3
module corpus.ja_core.example_00008
use Core
policy no_network

record Item10 { id: Count, label: Text }
function transform_10(item: Item10) -> Result<Item10, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item10 { id: item.id, label: normalized })
}
let sample: Item10 = Item10 { id: 10, label: "macro-beginner" }
let result = transform_10(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates macro at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {ledger.append} ⊢ node-a4a436ce73ec3445f762 : ApplicationArtifact ! {file.read} ⇒ validated`. The AST node is `node-a4a436ce73ec3445f762` and its origin hash is `13a728aba4d009ca0ce52b41957ca520dd93d1ae1850f9a6bed9684ae09176f2`. R12 uses operator `invoke` with record `r12-1a6b9f0469a9149f1aa8`. The modeled runtime points to MCRT record `mcrt-4dc678528bd6a0d76e42` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Design a small code generator and specify its deterministic inputs and emitted provenance.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `macro` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 14 — Reflection, Foreign Functions, and Host Integration

## Learning objectives

- Explain how `reflection`, `foreign_function`, `host_integration` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Cross introspection and host boundaries only through explicit schema, ABI, memory, capability, and policy contracts.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `reflection`

Examines declared structure under a governed policy rather than unrestricted runtime introspection.

In the corpus, `reflection` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `foreign_function`

Bridges to external native functions through explicit ABI, memory, effect, and capability contracts.

In the corpus, `foreign_function` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `host_integration`

Connects JA applications to approved host services while retaining sandbox, policy, and replay evidence.

In the corpus, `host_integration` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00030` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `reflection`

```ja
ja source 0.3
module corpus.ja_core.example_00030
use Core
policy no_network

record Item32 { id: Count, label: Text }
function transform_32(item: Item32) -> Result<Item32, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item32 { id: item.id, label: normalized })
}
let sample: Item32 = Item32 { id: 32, label: "reflection-beginner" }
let result = transform_32(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates reflection at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.write} ⊢ node-affaee99457246b9b894 : ApplicationArtifact ! {ledger.append} ⇒ validated`. The AST node is `node-affaee99457246b9b894` and its origin hash is `8be6688b76e3e7385baa128360e62a850f0cce1e27edfcdc9d3b3f3d40ad8d82`. R12 uses operator `borrow` with record `r12-702b419ec6cfaeb86558`. The modeled runtime points to MCRT record `mcrt-9afd3ca68192998fee8a` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Wrap a host service with a narrow adapter and record the denied operations.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `reflection` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 15 — Semantic Judgments and the Typed AST

## Learning objectives

- Explain how `record`, `function`, `effect` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Read the corpus judgment, AST, origin hash, child roles, types, effects, capabilities, and policy decision as a coherent proof object.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `record`

Defines a product type with named fields and predictable serialization, construction, and pattern semantics.

In the corpus, `record` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `function`

Defines a typed transformation with declared inputs, outputs, effects, and capability obligations.

In the corpus, `function` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `effect`

Declares observable operations beyond pure evaluation so optimization and policy cannot erase behavior.

In the corpus, `effect` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00001` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `record`

```ja
ja source 0.3
module corpus.ja_core.example_00001
use Core
policy no_network

record Item3 { id: Count, label: Text }
function transform_3(item: Item3) -> Result<Item3, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item3 { id: item.id, label: normalized })
}
let sample: Item3 = Item3 { id: 3, label: "record-beginner" }
let result = transform_3(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates record at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.read} ⊢ node-c2d0bb38419fc25adce6 : ApplicationArtifact ! {file.read} ⇒ validated`. The AST node is `node-c2d0bb38419fc25adce6` and its origin hash is `5a66a5a5e9c98afae431a0ea717fd7c90e455055508cb4d67adb80244d26fde4`. R12 uses operator `match` with record `r12-93bde4a3b7f90fe4b61a`. The modeled runtime points to MCRT record `mcrt-414dab4edeaa95dfec01` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Manually derive the semantic and AST evidence for one positive script.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `record` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 16 — Compiler Pipeline and Diagnostics

## Learning objectives

- Explain how `module`, `generic`, `ownership` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Follow source through parsing, resolution, typing, ownership, effects, policy, R12 lowering, optimization, and artifact emission.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `module`

Defines a compilation and naming boundary. Modules provide stable identity for imports, policy application, and incremental compilation.

In the corpus, `module` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `generic`

Abstracts a definition over types or values while preserving constraints needed for valid specialization.

In the corpus, `generic` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `ownership`

Assigns responsibility for resource lifetime and prevents implicit duplication or unsafe concurrent access.

In the corpus, `ownership` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00031` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `module`

```ja
ja source 0.3
module corpus.ja_core.example_00031
use Core
policy no_network

record Item33 { id: Count, label: Text }
function transform_33(item: Item33) -> Result<Item33, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item33 { id: item.id, label: normalized })
}
let sample: Item33 = Item33 { id: 33, label: "module-beginner" }
let result = transform_33(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates module at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {state.read} ⊢ node-91891a3bad9493dd2694 : ApplicationArtifact ! {state.write} ⇒ validated`. The AST node is `node-91891a3bad9493dd2694` and its origin hash is `ef45ad249f671394aa8af17cd4c178c400a4a7d34e579d41231b723ceb1983ea`. R12 uses operator `match` with record `r12-936eaad635cec75518f9`. The modeled runtime points to MCRT record `mcrt-c9c8afd411ad1b81b571` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Compare one accepted and one rejected corpus record and write a stage-specific diagnostic report.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `module` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 17 — Optimization Without Semantic Drift

## Learning objectives

- Explain how `constant`, `collection`, `stream` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Apply folding, specialization, allocation reduction, fusion, or stream planning while preserving protected behavior and evidence.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `constant`

Declares a value whose identity is fixed for the compilation unit and may be safely folded when proof obligations are retained.

In the corpus, `constant` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `collection`

Provides typed aggregate storage with declared ordering, mutation, allocation, and iteration semantics.

In the corpus, `collection` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `stream`

Models ordered or bounded sequences of values over time, including backpressure and completion behavior.

In the corpus, `stream` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00027` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `constant`

```ja
ja source 0.3
module corpus.ja_core.example_00027
use Core
policy no_network

record Item29 { id: Count, label: Text }
function transform_29(item: Item29) -> Result<Item29, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item29 { id: item.id, label: normalized })
}
let sample: Item29 = Item29 { id: 29, label: "constant-beginner" }
let result = transform_29(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates constant at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {process.spawn:signed} ⊢ node-5f2eeb379e255d766246 : ApplicationArtifact ! {file.write} ⇒ validated`. The AST node is `node-5f2eeb379e255d766246` and its origin hash is `f5be2c54e7f3e899b4f14cfe3dee83592f8fbaa3be0e33ca983806981e3383ab`. R12 uses operator `stream` with record `r12-a5fac7f9626ee2c8f220`. The modeled runtime points to MCRT record `mcrt-569b781dba4e89902215` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Propose two optimizations and list the invariants and replay checks required before acceptance.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `constant` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 18 — JA Core VM, Sandboxing, and Runtime Evidence

## Learning objectives

- Explain how `capability`, `async_task`, `host_integration` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Define the runtime boundary, resource accounting, capability consumption, sandbox controls, secret handling, and MCRT emission.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `capability`

Names explicit authority required to perform protected effects such as file, state, process, or host access.

In the corpus, `capability` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `async_task`

Models a scheduled computation with cancellation, timeout, ownership, and deterministic-test obligations.

In the corpus, `async_task` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `host_integration`

Connects JA applications to approved host services while retaining sandbox, policy, and replay evidence.

In the corpus, `host_integration` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00021` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `capability`

```ja
ja source 0.3
module corpus.ja_core.example_00021
use Core
policy no_network

record Item23 { id: Count, label: Text }
function transform_23(item: Item23) -> Result<Item23, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item23 { id: item.id, label: normalized })
}
let sample: Item23 = Item23 { id: 23, label: "capability-beginner" }
let result = transform_23(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates capability at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {process.spawn:signed} ⊢ node-ad52f03b3b42c513e0ae : ApplicationArtifact ! {pure} ⇒ validated`. The AST node is `node-ad52f03b3b42c513e0ae` and its origin hash is `370232fa3b427762ddfa943733f2871b192244579272bb33695b21a34c0550ae`. R12 uses operator `match` with record `r12-e4b3647479a67981adf6`. The modeled runtime points to MCRT record `mcrt-94d3be939291be2f90cd` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Draft a deterministic runtime trace for a capability-gated asynchronous application.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `capability` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 19 — R12 and MCRT Provenance

## Learning objectives

- Explain how `function`, `serialization` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Use R12 for lowered statement identity and MCRT for causal, policy, replay, and certification evidence.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `function`

Defines a typed transformation with declared inputs, outputs, effects, and capability obligations.

In the corpus, `function` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `serialization`

Maps values to stable external representations while preserving schema, version, and safety requirements.

In the corpus, `serialization` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00014` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `function`

```ja
ja source 0.3
module corpus.ja_core.example_00014
use Core
policy no_network

record Item16 { id: Count, label: Text }
function transform_16(item: Item16) -> Result<Item16, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item16 { id: item.id, label: normalized })
}
let sample: Item16 = Item16 { id: 16, label: "function-beginner" }
let result = transform_16(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates function at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {ledger.append} ⊢ node-9413878af45c62c7054d : ApplicationArtifact ! {pure} ⇒ validated`. The AST node is `node-9413878af45c62c7054d` and its origin hash is `d1fe891b5b33ed09d312be8c6a0104df3e16e82fe1a1a05c4ef190bb395d1425`. R12 uses operator `await` with record `r12-7f1a83ede1e765bfec12`. The modeled runtime points to MCRT record `mcrt-54dca5966114a4e1120a` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Construct an evidence chain from source hash to semantic ID, AST node, R12 record, artifact, and MCRT record.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `function` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 20 — Diagnostics, Security, Recovery, and Certification

## Learning objectives

- Explain how `structured_error`, `capability`, `borrow` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Treat failure cases as designed language assets rather than malformed leftovers, and separate expected results from executed evidence.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `structured_error`

Carries machine-readable failure identity, context, and recovery information instead of unstructured text alone.

In the corpus, `structured_error` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `capability`

Names explicit authority required to perform protected effects such as file, state, process, or host access.

In the corpus, `capability` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `borrow`

Provides bounded access without transferring ownership; mutability and aliasing rules remain explicit.

In the corpus, `borrow` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00020` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `structured_error`

```ja
ja source 0.3
module corpus.ja_core.example_00020
use Core
policy no_network

record Item22 { id: Count, label: Text }
function transform_22(item: Item22) -> Result<Item22, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item22 { id: item.id, label: normalized })
}
let sample: Item22 = Item22 { id: 22, label: "structured_error-beginner" }
let result = transform_22(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates structured error at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {ledger.append} ⊢ node-173acf678bdee42d5a79 : ApplicationArtifact ! {file.write} ⇒ validated`. The AST node is `node-173acf678bdee42d5a79` and its origin hash is `900f76a2410a6d26a6954f1c5fcafd16f9468ceaf5d20d341bf1a95dea54df22`. R12 uses operator `borrow` with record `r12-8d22fb3b591d01d373c1`. The modeled runtime points to MCRT record `mcrt-4e9b0bf344098f1618d3` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Build a test matrix spanning all ten validation classes and define safe recovery conditions.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `structured_error` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 21 — Deployment and Interoperability

## Learning objectives

- Explain how `package`, `foreign_function`, `serialization` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Package applications for air-gapped and host-integrated deployment while managing versions, ABIs, schemas, capabilities, and rollback.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `package`

Groups modules and distribution metadata into a deployable application unit while preserving dependency and provenance boundaries.

In the corpus, `package` appears in **324 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `foreign_function`

Bridges to external native functions through explicit ABI, memory, effect, and capability contracts.

In the corpus, `foreign_function` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `serialization`

Maps values to stable external representations while preserving schema, version, and safety requirements.

In the corpus, `serialization` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00009` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `package`

```ja
ja source 0.3
module corpus.ja_core.example_00009
use Core
policy no_network

record Item11 { id: Count, label: Text }
function transform_11(item: Item11) -> Result<Item11, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item11 { id: item.id, label: normalized })
}
let sample: Item11 = Item11 { id: 11, label: "package-beginner" }
let result = transform_11(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates package at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {process.spawn:signed} ⊢ node-b6d60fdc89c0d42e9042 : ApplicationArtifact ! {ledger.append} ⇒ validated`. The AST node is `node-b6d60fdc89c0d42e9042` and its origin hash is `dff2a0a16e4f2a2e47af200abbde412c703e0c2d7f91899b5c7537d5bf21c70a`. R12 uses operator `foreign_call` with record `r12-cd1e2a7b999914569e63`. The modeled runtime points to MCRT record `mcrt-76eef843e82b95e22ea4` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Create a deployment dossier with dependency hashes, host contracts, migration rules, and rollback evidence.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `package` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---

# Chapter 22 — Smithson 8S Coupled Mechanics and the Capstone Toolchain

## Learning objectives

- Explain how `host_integration`, `constraint`, `reflection` participates in a complete JA Core application.
- Trace source identity through semantic, AST, R12, runtime, and MCRT evidence.
- Distinguish a modeled expected result from a result produced by a native implementation.
- Apply policy, determinism, and provenance checks before accepting a transformation.

## Core idea

Integrate the explicitly proposed 8S framework as a governed analytical profile while keeping its claims, tolerances, projections, evidence, and limitations separate from established language semantics.

JA Core is designed around explicit contracts. A source construct is not complete merely because its syntax is recognizable. Its names and types must resolve; ownership and lifetime obligations must be satisfiable; observable effects must be declared; protected operations must have capabilities; policy must admit the operation; lowering must preserve stable identity; and runtime evidence must report what actually occurred. This layered view is what turns a language example into a certifiable application artifact.

The corpus uses a consistent evidence pattern. The source is hashed. The semantic layer supplies a judgment, declared and inferred types, effects, capabilities, policy decision, and proof obligations. The AST binds those facts to a node and source span. The compiler representation supplies frontend status, diagnostics, R12 identity, dependencies, input/output hashes, state, confidence, and artifact name. The runtime representation supplies expected output, observed effects, consumed capabilities, sandbox state, and MCRT identity. Optimization notes state the invariants that must survive transformation.

## Feature focus

### `host_integration`

Connects JA applications to approved host services while retaining sandbox, policy, and replay evidence.

In the corpus, `host_integration` appears in **323 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `constraint`

Restricts generic, type, or value parameters so specialization and validation can prove required properties.

In the corpus, `constraint` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

### `reflection`

Examines declared structure under a governed policy rather than unrestricted runtime introspection.

In the corpus, `reflection` appears in **322 records**. The curated pack includes positive and diagnostic examples wherever the source distribution permits. Use the feature matrix and script catalog to navigate by proficiency level and validation class.

## Corpus-derived example

**Record:** `JACORE-00004` · **Level:** `beginner` · **Class:** `positive` · **Feature:** `host_integration`

```ja
ja source 0.3
module corpus.ja_core.example_00004
use Core
policy no_network

record Item6 { id: Count, label: Text }
function transform_6(item: Item6) -> Result<Item6, Text> effects { pure } {
    let normalized: Text = item.label
    return Ok(Item6 { id: item.id, label: normalized })
}
let sample: Item6 = Item6 { id: 6, label: "host_integration-beginner" }
let result = transform_6(sample)
assert result.is_ok == true
emit json result
```

### Reading the example

Demonstrates host integration at the beginner level for JA Core Application Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.

The semantic judgment is `Environment; Policy; {file.write:artifacts} ⊢ node-0da5ceb30ff91eddb3ce : ApplicationArtifact ! {process.spawn} ⇒ validated`. The AST node is `node-0da5ceb30ff91eddb3ce` and its origin hash is `78aa7deb57654c6b4f664db70e885a03880b1df4832f2baca39fd1111dcd4481`. R12 uses operator `await` with record `r12-529375b34d871e73ab47`. The modeled runtime points to MCRT record `mcrt-8b83c9f1fa006f102464` and determinism class `R3-Deterministic`.

These identifiers should be read as a chain, not as unrelated metadata. A compiler implementation may replace internal structures, but it must provide a traceable mapping from the source construct to the emitted artifact and runtime evidence. Where a transformation changes identity, the supersession relation must be recorded rather than silently discarding provenance.

## Review lenses

- **SOPHIA:** Are meaning, types, ownership, effects, and policy internally consistent?
- **CHARLOTTE:** Are modules, declarations, AST nodes, spans, and interfaces structurally complete?
- **LANDON:** Can the lowering, runtime, sandbox, resource, and replay contracts be implemented and tested?
- **Professor:** Does the example isolate one concept before combining it with harder features?
- **Podium:** Can a reviewer discover the record, script, hashes, diagnostics, and limitations quickly?

## Engineering checklist

- Confirm the source header, module identity, imports, and policy declarations.
- Verify the source hash and source-to-AST span.
- Check declared and inferred types.
- Check ownership, borrowing, lifetime, effect, and capability obligations relevant to the construct.
- Preserve policy decisions and diagnostic stage.
- Record R12 and MCRT identities or an explicit traceable replacement.
- Separate expected outcomes from native test results.
- Retain the Smithson 8S framework’s proposed-status notice when its annotations are used.

## Laboratory

Design a standalone JA Core toolchain and application that emits source, semantic, AST, R12, runtime, MCRT, validation, and limitation evidence.

Deliverables: a `.ja` source file, a source hash, a semantic worksheet, an AST sketch, an R12 tuple, a modeled or native runtime trace clearly labeled, an MCRT record, and a one-page limitation statement.

## Review questions

1. What failure could occur if `host_integration` were optimized without retaining its effect, ownership, or provenance obligations?
2. Which evidence layer should first report an unresolved name, type mismatch, invalid borrow, or denied capability?
3. What is the difference between a source hash, AST identity, R12 identity, and MCRT identity?
4. Which statements in the corpus are expected results, and which would require a native implementation to verify?
5. How would a security or recovery test differ from a positive example for this chapter?

---
