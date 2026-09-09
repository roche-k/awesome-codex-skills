# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

## Healthy Backlog Standards

A healthy backlog means:
- Top 2 sprints are detailed, estimated, and sprint-ready
- Next 2-3 sprints are roughly estimated with clear intent
- Everything beyond is directional, not detailed
- No zombie stories older than 90 days without a decision
- Each item has: owner, priority, acceptance criteria, definition of done

## Grooming Session Structure (60-90 min, every sprint)

### Part 1: Backlog Hygiene (20 min)
- Archive or delete stories >90 days old without action
- Flag stories in "ready" for 3+ sprints — why aren't they being built?
- Merge duplicate stories
- Ensure priorities reflect current strategy, not last quarter's

### Part 2: Story Refinement (40 min)
For each candidate story (top 5-8 per session):
1. Read the story aloud — does everyone understand it?
2. Acceptance criteria — are they specific and testable?
3. Questions / unknowns — what do we need to know before building?
4. Dependencies — does this block or get blocked by something?
5. Estimate — relative sizing (t-shirt or story points)

### Part 3: Priority Review (10-20 min)
- Do top items reflect current priorities?
- Did anything change this week that should reorder the backlog?
- Are there items to promote from "next" to "now"?

## Estimation Methods

### Story Points (Fibonacci: 1, 2, 3, 5, 8, 13, 21)
- Relative sizing, not time
- 1 = trivially small; 13+ = too big, break it down
- 21 = epic, not a story

### T-Shirt Sizing (XS, S, M, L, XL)
- Faster, less precise
- Good for roadmap-level estimation
- Convert to points when sprint-ready

### Planning Poker Rules
- Everyone votes simultaneously (prevent anchoring)
- Outliers explain their reasoning
- Re-vote after discussion if needed
- Don't average — reach consensus

## Story Readiness Checklist (Definition of Ready)

A story is sprint-ready when:
- [ ] Acceptance criteria are clear and testable
- [ ] Design is available (if UI work)
- [ ] Dependencies identified and resolved
- [ ] Estimated by the team
- [ ] Fits within one sprint
- [ ] Test scenarios drafted

## Backlog Categories

- **Now** — sprint-ready, estimated, detailed
- **Next** — roughly defined, next 2-3 sprints
- **Later** — directional intent, not detailed
- **Icebox** — parked, revisit quarterly
- **Won't Do** — explicitly rejected, with reason noted

## Output Format

Deliver:
- Groomed backlog assessment
- Stories ready for sprint vs. needs more work
- Items recommended for archival
- Refinement agenda for next session
