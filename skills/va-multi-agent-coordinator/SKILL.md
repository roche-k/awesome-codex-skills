---
name: va-multi-agent-coordinator
description: "Plan or carry out authorized coordination of multiple workers with explicit sequencing, file ownership, handoffs, and failure handling."
---

# Multi Agent Coordinator

## Coordinate actual workers

Identify the actual worker roster, shared task, dependencies, and resource limits.
For each handoff specify the input, output, recipient, and completion condition.
Choose a sequential pipeline for dependent work or fan-out/fan-in for independent
work. Give shared files one owner or use separate output paths to avoid collisions.

Use only the collaboration tools and shared storage exposed by the environment.
There is no message bus, worker pool, RPC endpoint, or queue created by installing
this skill. Delegate only when authorized, inheriting the primary agent's model,
reasoning effort, and service tier unless the user requests otherwise.

Define bounded retries, cancellation, failure propagation, and recovery for each
handoff. Treat unusable output as a failed dependency instead of silently assuming
success. Reconcile results against the requested outcome. Present plans in the
response unless the user asks for a file, and distinguish plans from executed work.
