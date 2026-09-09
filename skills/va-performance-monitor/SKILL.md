---
name: va-performance-monitor
description: "Analyze supplied metrics, logs, or profiles for performance patterns and anomalies, and specify measurements needed to explain the observed behavior."
---

# Performance Monitor

## Analyze measured performance

Establish the measurement source, time window, workload, units, aggregation, and
sampling method. Compare compatible baselines and distinguish throughput, latency
distributions, utilization, errors, and queueing. Check for missing samples and
changes in workload before interpreting a trend or anomaly.

Trace each conclusion to actual measurements. Separate symptoms from suspected
causes and describe the next measurement that would distinguish hypotheses.
Propose instrumentation at the relevant service or pipeline boundary with useful
labels, retention, and alert conditions tied to the user's operational needs.

Use available monitoring tools only within the authorized scope. This skill does
not start collectors or an observability backend. Write profiler data and test
artifacts to the project's designated test directory, and report measured results
without substituting example targets for observations.
