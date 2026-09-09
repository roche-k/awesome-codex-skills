---
name: va-skill-catalog
description: "Browse, search, install, and uninstall the Codex skills in this collection. Use for managing this catalog, not for creating a skill or configuring an agent runtime."
---

# Agent Installer

## Use the catalog

Run the bundled `scripts/catalog.py` with Python 3.9 or later. Paths below are
relative to this skill's directory; resolve them from the actual installed path.
The bundled `references/catalog.json` supports discovery without network access.

```sh
python3 scripts/catalog.py categories
python3 scripts/catalog.py list --category 02-language-specialists
python3 scripts/catalog.py search 'C++'
python3 scripts/catalog.py show cpp-pro
```

## Install and remove

Use a local clone of `roche-k/awesome-codex-skills` as the package source.
When running this skill from that clone, the script discovers it automatically.
For an independently installed catalog, pass `--source /path/to/awesome-codex-skills`.
If no clone is available, obtain its location from the user or clone the private
repository through an already authenticated GitHub connection when authorized.
Do not fall back to Claude agent downloads or assume anonymous access works.

```sh
python3 scripts/catalog.py --source /path/to/awesome-codex-skills install cpp-pro
python3 scripts/catalog.py --source /path/to/awesome-codex-skills install --category 02-language-specialists --dry-run
python3 scripts/catalog.py --source /path/to/awesome-codex-skills install python-pro --project /path/to/project
python3 scripts/catalog.py installed
python3 scripts/catalog.py uninstall cpp-pro --dry-run
python3 scripts/catalog.py uninstall cpp-pro
```

The default destination is `~/.agents/skills`. `--project PATH` selects
`PATH/.agents/skills`; `--dest PATH` selects an explicit directory, including
`${CODEX_HOME:-$HOME/.codex}/skills` for installations using that location.
Use the scope requested by the user. An explicit request to install or uninstall
already authorizes that operation. Listing and searching do not install anything.

The installer refuses unmanaged or locally changed destinations. An unchanged
installation can be repeated. To update a managed skill, uninstall its unchanged
copy and install the new version. Preserve local edits before replacing a skill.
Use `--all` only for a requested full-collection installation; many overlapping
skills can crowd discovery, so selection by capability is usually more useful.

Report the selected names and destination with the actual command result. Skills
become available through `$va-<name>` or matching requests after discovery; if a
new skill is missing, restart the Codex session.
