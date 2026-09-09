---
name: va-cpp-pro
description: "Use when building high-performance C++ systems requiring modern C++20/23 features, template metaprogramming, or zero-overhead abstractions for systems programming, embedded systems, or performance-critical applications."
---

# Cpp Pro

Use this skill for the capability described above and keep the user's requested
scope, logic placement, and existing project conventions. Read the relevant
sections of [the domain guide](references/guide.md) for detailed considerations;
select the checks that affect this task instead of treating the guide as a
mandatory full-project checklist.

## Workflow

1. Establish the language, compiler or runtime version, build entry point, and existing conventions.
2. Implement against those versions and the actual ownership, error-handling, and concurrency model.
3. Build or run the production entry point before selecting focused behavioral checks.

## Task-specific focus

- Review CMakeLists.txt, compiler flags, and target architecture
- Analyze template usage, memory patterns, and performance characteristics
- Implement solutions following C++ Core Guidelines and modern best practices

## Applying the guidance

Use only tools and services actually available in the session. This skill is
instructional guidance; it does not create a subagent, grant tool permissions,
select a model, or supply a context-manager service. Related specialists are
optional; this skill works independently.

Treat source performance numbers, coverage percentages, and version examples as
context, not verified results or universal acceptance gates. Preserve the user's
test and artifact rules. Report only observed outcomes and disclose checks that
could not run. Produce the requested deliverable without creating extra planning
or status files unless the user requests them.
