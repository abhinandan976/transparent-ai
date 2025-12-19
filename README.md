# Transparent AI

**Transparent AI** is a lightweight, protocol-first AI orchestration framework
designed to avoid black-box abstractions.

Unlike chain-based frameworks, Transparent AI uses:
- graph-based execution
- explicit state
- deterministic agent loops
- visible memory, cost, and traces
- optional live token streaming

This framework is intended for:
- research
- system design exploration
- debuggable AI agents
- learning modern AI orchestration patterns

---

## Core Concepts

### Graph Execution
Execution is defined as a graph, not a chain.

```text
input → reasoning → decision → loop
