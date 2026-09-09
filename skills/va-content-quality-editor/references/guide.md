# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

Install unslop if not present:
```bash
npm install -g unslop
```

Usage patterns:
```bash
# File mode
unslop path/to/draft.md

# Pipe mode
cat draft.md | unslop --stdin --deterministic

# Aggressive mode (strips more patterns)
unslop --aggressive path/to/draft.md
```

What unslop removes:
- Sycophantic openers ("Great question!", "Certainly!", "Absolutely!")
- Stock vocabulary ("leverage", "utilize", "implement", "navigate", "streamline")
- Hedging stacks ("it's worth noting that", "it's important to consider")
- Em-dash overuse (converts em-dashes to cleaner punctuation)
- Filler transitions ("Furthermore,", "Moreover,", "In conclusion,")

What unslop preserves:
- Code blocks, URLs, technical terms
- The author's intended meaning
- Sentence structure (unless pattern-matched)

After unslop, check for:
- Passive voice chains longer than two sentences
- Sentences starting with "There is" or "There are"
- Lists of 5+ items that could be prose
- Headers that restate the paragraph that follows

Quality gates before marking done:
- [ ] No banned openers remain
- [ ] Stock vocabulary removed
- [ ] Reading level appropriate for audience (technical = Grade 10–12)
- [ ] First sentence hooks without clickbait
