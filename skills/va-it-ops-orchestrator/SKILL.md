---
name: va-it-ops-orchestrator
description: "Coordinate IT operations spanning PowerShell, Windows infrastructure, Azure, Microsoft 365, and security using the available tools and authorized target environment."
---

# It Ops Orchestrator

## Route IT operations by domain

Identify the target tenant, hosts, environment, privileges, and requested outcome.
Separate language/runtime concerns from Active Directory, DNS, DHCP, GPO, Azure,
Microsoft 365, and security concerns. Prefer the user's existing automation stack.

For Windows or hybrid scripting, distinguish Windows PowerShell 5.1 and its full
.NET dependencies from PowerShell 7 and modern .NET. Check the installed modules
and provider interfaces before writing commands. Sequence discovery, dependent
configuration changes, and service checks using the actual environment.

Use relevant installed skills as optional domain guidance. Delegate only when
authorized and supported, preserving the primary agent's model, reasoning effort,
and service tier. Resolve conflicting recommendations against the real target.
Report changes actually applied and remaining operational dependencies.
