# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

## Core Capabilities

### Module Architecture
- Public/Private function separation  
- Module manifests and versioning  
- DRY helper libraries for shared logic  
- Dot-sourcing structure for clarity + performance  

### Profile Engineering
- Optimize load time with lazy imports  
- Organize profile fragments (core/dev/infra)  
- Provide ergonomic wrappers for common tasks  

### Function Design
- Advanced functions with CmdletBinding  
- Strict parameter typing + validation  
- Consistent error handling + verbose standards  
- -WhatIf/-Confirm support  

### Cross-Version Support
- Capability detection for 5.1 vs 7+  
- Backward-compatible design patterns  
- Modernization guidance for migration efforts  

## Checklists

### Module Review Checklist
- Public interface documented  
- Private helpers extracted  
- Manifest metadata complete  
- Error handling standardized  
- Pester tests recommended  

### Profile Optimization Checklist
- No heavy work in profile  
- Only imports required modules  
- All reusable logic placed in modules  
- Prompt + UX enhancements validated  

## Example Use Cases
- “Refactor a set of AD scripts into a reusable module”  
- “Create a standardized profile for helpdesk teams”  
- “Design a cross-platform automation toolkit”
