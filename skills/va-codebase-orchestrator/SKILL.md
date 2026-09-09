---
name: va-codebase-orchestrator
description: "Coordinate a requested repository-wide refactor by mapping dependencies, prioritizing concrete risks, and sequencing changes through the repository's actual interfaces."
---

# Codebase Orchestrator

## Coordinate the requested refactor

Map the affected entry points, initialization, registration, build dependencies,
and ownership boundaries. Rank observed security flaws and behavioral bugs ahead
of architecture, performance, and style preferences. Explain each change using
the affected behavior and files, rather than a general code-purity score.

Preserve the user's requested logic placement and existing authorized scope.
Make changes through the real framework and compile/link its production structure
before designing behavioral tests. Use bounded searches for large repositories
and report unavailable evidence or tools without inventing replacement services.

Continue reversible authorized work without repeated approval gates. Ask only
when an actual missing decision or an action beyond the existing authorization
blocks progress. Present the concrete diff and verification results. Write a
separate refactor plan or metadata file only when requested.
