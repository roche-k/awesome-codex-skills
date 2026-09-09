# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

## Core Capabilities

### AD Security Posture Assessment
- Analyze privileged groups (Domain Admins, Enterprise Admins, Schema Admins)
- Review tiering models & delegation best practices
- Detect orphaned permissions, ACL drift, excessive rights
- Evaluate domain/forest functional levels and security implications

### Authentication & Protocol Hardening
- Enforce LDAP signing, channel binding, Kerberos hardening
- Identify NTLM fallback, weak encryption, legacy trust configurations
- Recommend conditional access transitions (Entra ID) where applicable

### GPO & Sysvol Security Review
- Examine security filtering and delegation
- Validate restricted groups, local admin enforcement
- Review SYSVOL permissions & replication security

### Attack Surface Reduction
- Evaluate exposure to common vectors (DCShadow, DCSync, Kerberoasting)
- Identify stale SPNs, weak service accounts, and unconstrained delegation
- Provide prioritization paths (quick wins → structural changes)

## Checklists

### AD Security Review Checklist
- Privileged groups audited with justification  
- Delegation boundaries reviewed and documented  
- GPO hardening validated  
- Legacy protocols disabled or mitigated  
- Authentication policies strengthened  
- Service accounts classified + secured  

### Deliverables Checklist
- Executive summary of key risks  
- Technical remediation plan  
- PowerShell or GPO-based implementation scripts  
- Validation and rollback procedures
