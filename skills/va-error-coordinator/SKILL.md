---
name: va-error-coordinator
description: "Analyze recurring failures and cascades across supplied logs or worker outputs, and derive evidence-based recovery and failure-propagation rules."
---

# Error Coordinator

## Trace failure propagation

Establish the observation window and correlate actual errors by timestamp,
operation, dependency, and identifier. Separate the initiating failure from
downstream symptoms. Cite representative records and state gaps in the evidence.

Classify errors by retryability and effect on state. Propose bounded retries only
for recoverable operations, with idempotency and duplicate-side-effect handling.
Describe when to stop, compensate, isolate a dependency, or return a partial result.
Use observed recurrence to justify changes; do not invent incident counts.

Implement recovery changes when requested through the real service or workflow
interfaces. Otherwise present the analysis and recovery rules in the response.
This skill does not run a recovery engine or provide an inter-agent error API.
