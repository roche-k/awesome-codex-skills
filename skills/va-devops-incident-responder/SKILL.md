---
name: va-devops-incident-responder
description: "Use when actively responding to production incidents, diagnosing critical service failures, or conducting incident postmortems to implement permanent fixes and preventative measures."
---

# Devops Incident Responder

Use this skill for the capability described above and keep the user's requested
scope, logic placement, and existing project conventions. Read the relevant
sections of [the domain guide](references/guide.md) for detailed considerations;
select the checks that affect this task instead of treating the guide as a
mandatory full-project checklist.

## Workflow

1. Identify the target environment, current configuration, credentials available, and intended change scope.
2. Use the existing infrastructure and deployment mechanisms; account for state, dependencies, and recovery.
3. Check the affected service or configuration and distinguish a proposed change from one actually applied.

## Task-specific focus

- Review monitoring setup, alerting rules, and response procedures
- Analyze incident patterns, response times, and resolution effectiveness
- Implement solutions improving detection, response, and prevention

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
