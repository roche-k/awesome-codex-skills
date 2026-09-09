---
name: va-agent-organizer
description: "Break an explicitly requested coordinated task into bounded subtasks matched to available capabilities, with ownership, dependencies, and a concrete execution order."
---

# Agent Organizer

## Organize the work

Start from the user's outcome and inspect the capabilities actually available.
Separate tasks only when their inputs and outputs are concrete. Assign each task
an owner, relevant files or responsibility, dependencies, and a completion test.
Keep dependent work sequential and parallelize only independent bounded work.

Use subagents only when delegation is authorized and the environment exposes it.
Preserve the primary agent's model, reasoning effort, and service tier unless the
user explicitly requests different settings. Pass requirements and necessary
artifacts, not unrelated private context. If delegation is unavailable, execute
the same dependency order in the current session.

Keep coordination in the response unless a written artifact is requested. Report
actual assignments and results; an installed skill is guidance, not a running
worker or a transport service.
