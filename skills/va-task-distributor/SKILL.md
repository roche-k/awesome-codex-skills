---
name: va-task-distributor
description: "Design a task assignment strategy for actual workers with dependencies, priorities, capacity limits, ownership, and recovery behavior."
---

# Task Distributor

## Distribute bounded work

Identify task inputs and outputs, dependencies, deadlines, and actual worker
capabilities. Separate indivisible operations from independent partitions.
Match work to capacity using known resource limits rather than invented load
metrics. Explain ordering, fairness, and starvation tradeoffs where relevant.

Specify one owner per mutable output, how completion is acknowledged, how failed
work is retried or reassigned, and how duplicate execution is made harmless.
Break dependency cycles explicitly before scheduling. Keep dependent steps in order.

For a design request, present the strategy in the response or requested artifact.
For an authorized execution request, use only available collaboration mechanisms
and inherit the primary agent's model, reasoning effort, and service tier. This
skill itself does not supply a scheduler, worker pool, or queue.
