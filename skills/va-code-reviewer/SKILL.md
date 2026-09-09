---
name: va-code-reviewer
description: "Use when you need to conduct comprehensive code reviews focusing on code quality, security vulnerabilities, and best practices."
---

# Code Reviewer

Use this skill for the capability described above and keep the user's requested
scope, logic placement, and existing project conventions. Read the relevant
sections of [the domain guide](references/guide.md) for detailed considerations;
select the checks that affect this task instead of treating the guide as a
mandatory full-project checklist.

## Workflow

1. Establish the review, testing, or remediation scope and trace the relevant production data flow.
2. Prioritize reproducible correctness and security issues; connect each finding to its trigger and impact.
3. For a review, report findings with file locations. For requested fixes, implement and verify the affected behavior.

## Task-specific focus

- Review code changes, patterns, and architectural decisions
- Analyze code quality, security, performance, and maintainability
- Provide actionable feedback with specific improvement suggestions

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
