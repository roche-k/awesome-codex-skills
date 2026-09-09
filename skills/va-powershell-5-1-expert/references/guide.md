# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

## Core Capabilities

### Windows PowerShell 5.1 Specialization
- Strong mastery of .NET Framework APIs and legacy type accelerators
- Deep experience with RSAT modules:
  - ActiveDirectory
  - DnsServer
  - DhcpServer
  - GroupPolicy
- Compatible scripting patterns for older Windows Server versions

### Enterprise Automation
- Build reliable scripts for AD object management, DNS record updates, DHCP scope ops
- Design safe automation workflows (pre-checks, dry-run, rollback)
- Implement verbose logging, transcripts, and audit-friendly execution

### Compatibility + Stability
- Ensure backward compatibility with older modules and APIs
- Avoid PowerShell 7+–exclusive cmdlets, syntax, or behaviors
- Provide safe polyfills or version checks for cross-environment workflows

## Checklists

### Script Review Checklist
- [CmdletBinding()] applied  
- Parameters validated with types + attributes  
- -WhatIf/-Confirm supported where appropriate  
- RSAT module availability checked  
- Error handling with try/catch and friendly error messages  
- Logging and verbose output included  

### Environment Safety Checklist
- Domain membership validated  
- Permissions and roles checked  
- Changes preceded by read-only Get-* queries  
- Backups performed (DNS zone exports, GPO backups, etc.)  

## Example Use Cases
- “Create AD users from CSV and safely stage them before activation”  
- “Automate DHCP reservations for new workstations”  
- “Update DNS records based on inventory data”  
- “Bulk-adjust GPO links across OUs with rollback support”
