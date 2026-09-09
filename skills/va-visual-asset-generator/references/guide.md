# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

Asset type checklist:
- App icons: 1024×1024px, transparent background, simple shape, works at 16px
- Favicons: 32×32px or 64×64px, high contrast, recognizable silhouette
- OG images: 1200×630px, includes project name, no small text
- Logos: SVG preferred, wordmark variant included
- Social banners: 1500×500px (Twitter/X), 1128×191px (LinkedIn)

Prompt engineering principles:
- Lead with style adjectives before subject
- Include lighting, medium, color palette in every prompt
- Avoid photorealistic for UI assets — prefer flat, vector-style, or isometric
- Specify "isolated on transparent background" for icons

Install prompt-to-asset if not present:
```bash
npm install -g prompt-to-asset
```

Fallback: if MCP is unavailable, output a detailed prompt the user can paste into any image generation interface.
