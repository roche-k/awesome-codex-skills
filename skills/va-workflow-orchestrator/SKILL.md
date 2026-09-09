---
name: va-workflow-orchestrator
description: "Design or implement a requested workflow or state machine with explicit transitions, dependency ordering, failure handling, and compensation behavior."
---

# Workflow Orchestrator

## Define an executable workflow

Identify the existing execution framework, inputs, states, transitions, terminal
conditions, and ownership of side effects. Specify transition guards and outputs.
Model failure and cancellation paths alongside successful execution.

For operations that can repeat, define idempotency and deduplication. Bound retries
and explain which failures need compensation, a forward repair, or manual input.
Identify which state survives interruption and how execution resumes consistently.

Implement through the repository's actual registration and runtime mechanisms
when requested. Compile or load that production structure before behavioral
tests. Otherwise deliver the requested state-machine description. Do not imply
that installing this skill starts an engine or authorizes external side effects.
