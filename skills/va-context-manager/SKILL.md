---
name: va-context-manager
description: "Organize context and shared state for an existing workflow, including provenance, naming, ownership, handoffs, and recovery after interruption."
---

# Context Manager

## Manage the actual context

Identify the decisions, requirements, artifacts, and current state needed by the
next step. Reuse existing context and storage conventions. Keep one canonical
owner for each mutable fact, attach source paths to evidence, and distinguish
confirmed decisions from assumptions or superseded information.

For a handoff, include the outcome, current status, relevant paths, constraints,
completed checks, and next dependency. Limit context to what the recipient needs.
Keep sensitive information out of unnecessary copies. Define when stale state
must be refreshed and how an interrupted workflow resumes without repeating work.

This skill does not supply a context API, database, cache server, or persistent
memory service. Use the session's actual capabilities. Store new context files
only when they are part of the user's requested deliverable.
