# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

## The 4 Risk Categories (VUBF)

### Value Risk
Will customers want this? Will it solve a real problem?
- "Users will pay for this"
- "This solves a problem users actually have"
- "Users will switch from their current solution"

### Usability Risk
Can customers figure out how to use it?
- "Users will understand the onboarding"
- "The interface is intuitive without training"
- "Users can complete the core task in under 2 minutes"

### Business Viability Risk
Can we build a sustainable business around this?
- "Our CAC will be below $X"
- "Enterprises will buy this, not just use the free tier"
- "The margin after infrastructure costs is positive"

### Feasibility Risk
Can we actually build it?
- "We can get the data we need"
- "The latency will be acceptable"
- "We can build this with our current team in the timeline"

## Prioritization Grid

Map each assumption on 2 axes:
- **X-axis**: Importance to the idea succeeding (Low → High)
- **Y-axis**: Evidence we have right now (Strong → Weak)

| Quadrant | Action |
|---|---|
| High importance + Weak evidence | **Test immediately** — highest priority |
| Low importance + Weak evidence | Test eventually |
| High importance + Strong evidence | Monitor |
| Low importance + Strong evidence | Ignore for now |

## For Each Priority Assumption, Define

1. The assumption stated clearly
2. The riskiest version of this assumption
3. The cheapest/fastest experiment to test it
4. What "validated" looks like (success metric)
5. What "invalidated" means for the product direction

## Assumption Extraction Process

When given a product idea or feature:
1. Ask: What must be true for this to succeed?
2. Extract assumptions across all 4 VUBF categories
3. Score each: Importance (H/M/L) × Evidence (H/M/L)
4. Rank and identify the top 3-5 to test first
5. Suggest the cheapest experiment for each

## Output Format

Deliver:
- Assumption table: Assumption | Category | Importance | Evidence | Priority
- Top 3-5 assumptions to test with specific experiment suggestions
- Decision rules: what result validates vs. invalidates each assumption
