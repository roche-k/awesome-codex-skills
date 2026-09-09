#!/usr/bin/env python3
"""Build independently installable Codex skills from the pinned agent sources."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "https://github.com/VoltAgent/awesome-claude-code-subagents"
COLLECTION = "https://github.com/roche-k/awesome-codex-skills"
REVISION = "3097abe2d0d1e83a9023c7a8d054c00aace24990"
CATALOG = "va-skill-catalog"

CATEGORY_WORKFLOWS = {
    "01": [
        "Locate the existing feature boundaries, entry points, and contracts affected by the request.",
        "Implement through the project's existing components and interfaces; include relevant failure and compatibility paths.",
        "Exercise the changed behavior and report the result with the affected file paths.",
    ],
    "02": [
        "Establish the language, compiler or runtime version, build entry point, and existing conventions.",
        "Implement against those versions and the actual ownership, error-handling, and concurrency model.",
        "Build or run the production entry point before selecting focused behavioral checks.",
    ],
    "03": [
        "Identify the target environment, current configuration, credentials available, and intended change scope.",
        "Use the existing infrastructure and deployment mechanisms; account for state, dependencies, and recovery.",
        "Check the affected service or configuration and distinguish a proposed change from one actually applied.",
    ],
    "04": [
        "Establish the review, testing, or remediation scope and trace the relevant production data flow.",
        "Prioritize reproducible correctness and security issues; connect each finding to its trigger and impact.",
        "For a review, report findings with file locations. For requested fixes, implement and verify the affected behavior.",
    ],
    "05": [
        "Identify the actual data sources, schemas, ownership, processing stages, and acceptance criteria.",
        "Work through the existing pipeline or model interfaces, accounting for missing data, leakage, and reproducibility.",
        "Evaluate against observed data and an appropriate baseline; report uncertainty and limitations.",
    ],
    "06": [
        "Reproduce the developer workflow using the project's real commands and supported environments.",
        "Improve the requested tool or document at its existing integration point with actionable error paths.",
        "Exercise the documented commands and explain any environment requirements that remain.",
    ],
    "07": [
        "Establish the domain constraints, actual platform or provider, and supported interfaces.",
        "Apply the relevant domain guidance to the requested artifact or implementation.",
        "Check current primary sources for external contracts or rules and distinguish evidence from assumptions.",
    ],
    "08": [
        "Identify the audience, business decision, available evidence, and requested deliverable.",
        "Apply the relevant framework to that evidence, separating observed results from hypotheses.",
        "Deliver concrete recommendations or the requested content with tradeoffs and unresolved assumptions.",
    ],
    "09": [
        "Identify the actual task boundaries, available capabilities, dependencies, and ownership.",
        "Choose sequencing and handoffs supported by the current environment.",
        "Present the requested coordination result and distinguish proposed work from completed execution.",
    ],
    "10": [
        "Define the question, evidence requirements, scope, and relevant time period.",
        "Collect and evaluate sources or supplied data with traceable provenance and appropriate methods.",
        "Synthesize findings with citations, uncertainty, conflicting evidence, and the decision they inform.",
    ],
}

# These source agents depend on Claude's installer or orchestration environment.
# Their workflows are authored for Codex instead of translating runtime names.
OVERRIDES = {
    "agent-installer": (
        "Browse, search, install, and uninstall the Codex skills in this collection. Use for managing this catalog, not for creating a skill or configuring an agent runtime.",
        """## Use the catalog

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
""",
    ),
    "design-bridge": (
        "Translate a supplied DESIGN.md or visual design specification into concrete Codex implementation guidance while preserving its colors, typography, components, and responsive behavior.",
        """## Translate the supplied design

Use the design document, site, or reference already specified by the user. Read
the local document or retrieve the named source with an available tool. Ask for
a source only when it is missing; a particular design catalog is optional.

Extract the source's visual atmosphere, color roles and exact values, typefaces,
weights, sizes, spacing, layout grid, component states, elevation, and responsive
rules. Distinguish specified values from inferred ones and keep missing values
visible instead of inventing a brand rule.

Express the result as reusable tokens and concrete component instructions that
fit the project's existing frontend. Include a color-role table when it helps.
Preserve the reference's hierarchy and responsive behavior; a screenshot is
evidence, not a substitute for working components.

Deliver the translation in the response or in the user-requested file. If the
request includes implementation, implement it in the actual frontend. Report
what was visually checked and any remaining fidelity gaps. Related UI or
frontend skills are optional guidance, not assumed running agents.
""",
    ),
    "scientific-literature-researcher": (
        "Search scientific literature and synthesize experimental evidence from published studies, including methods, sample sizes, results, limitations, and source attribution.",
        """## Find and evaluate studies

Define the research question, population or system, interventions or exposures,
outcomes, and eligible study designs as relevant. Use available literature search,
web retrieval, or user-provided papers. A connected paper-search MCP can help, but
no particular server, API, subscription, or structured field is assumed available.

Prefer primary studies and inspect full text when the requested detail requires
it. Record the title, authors, publication date, DOI or source URL, study design,
sample size, methods, outcome definitions, effect estimates, uncertainty, and
limitations that are actually reported. Mark unavailable fields as missing.

Compare methods before combining results. Evaluate bias, confounding, statistical
power, preregistration where applicable, and consistency across studies. Do not
treat a provider's quality score as a substitute for methodological assessment.
Separate abstract-only evidence, preprints, and peer-reviewed full-text findings.

Return a traceable evidence table or synthesis appropriate to the request, cite
each factual conclusion, and explain contradictory results and evidence gaps.
Report only searches and papers actually examined. Do not install an MCP server
or change global configuration merely to activate this skill.
""",
    ),
    "agent-organizer": (
        "Break an explicitly requested coordinated task into bounded subtasks matched to available capabilities, with ownership, dependencies, and a concrete execution order.",
        """## Organize the work

Start from the user's outcome and inspect the capabilities actually available.
Separate tasks only when their inputs and outputs are concrete. Assign each task
an owner, relevant files or responsibility, dependencies, and a completion test.
Keep dependent work sequential and parallelize only independent bounded work.

Use subagents only when delegation is authorized and the environment exposes it.
Preserve the primary agent's model, reasoning effort, and service tier unless the
user explicitly requests different settings. Pass requirements and necessary
artifacts, not unrelated private context. If delegation is unavailable, execute
the same dependency order in the current session.

Keep coordination in the response unless a written artifact is requested. Report
actual assignments and results; an installed skill is guidance, not a running
worker or a transport service.
""",
    ),
    "multi-agent-coordinator": (
        "Plan or carry out authorized coordination of multiple workers with explicit sequencing, file ownership, handoffs, and failure handling.",
        """## Coordinate actual workers

Identify the actual worker roster, shared task, dependencies, and resource limits.
For each handoff specify the input, output, recipient, and completion condition.
Choose a sequential pipeline for dependent work or fan-out/fan-in for independent
work. Give shared files one owner or use separate output paths to avoid collisions.

Use only the collaboration tools and shared storage exposed by the environment.
There is no message bus, worker pool, RPC endpoint, or queue created by installing
this skill. Delegate only when authorized, inheriting the primary agent's model,
reasoning effort, and service tier unless the user requests otherwise.

Define bounded retries, cancellation, failure propagation, and recovery for each
handoff. Treat unusable output as a failed dependency instead of silently assuming
success. Reconcile results against the requested outcome. Present plans in the
response unless the user asks for a file, and distinguish plans from executed work.
""",
    ),
    "codebase-orchestrator": (
        "Coordinate a requested repository-wide refactor by mapping dependencies, prioritizing concrete risks, and sequencing changes through the repository's actual interfaces.",
        """## Coordinate the requested refactor

Map the affected entry points, initialization, registration, build dependencies,
and ownership boundaries. Rank observed security flaws and behavioral bugs ahead
of architecture, performance, and style preferences. Explain each change using
the affected behavior and files, rather than a general code-purity score.

Preserve the user's requested logic placement and existing authorized scope.
Make changes through the real framework and compile/link its production structure
before designing behavioral tests. Use bounded searches for large repositories
and report unavailable evidence or tools without inventing replacement services.

Continue reversible authorized work without repeated approval gates. Ask only
when an actual missing decision or an action beyond the existing authorization
blocks progress. Present the concrete diff and verification results. Write a
separate refactor plan or metadata file only when requested.
""",
    ),
    "context-manager": (
        "Organize context and shared state for an existing workflow, including provenance, naming, ownership, handoffs, and recovery after interruption.",
        """## Manage the actual context

Identify the decisions, requirements, artifacts, and current state needed by the
next step. Reuse existing context and storage conventions. Keep one canonical
owner for each mutable fact, attach source paths to evidence, and distinguish
confirmed decisions from assumptions or superseded information.

For a handoff, include the outcome, current status, relevant paths, constraints,
completed checks, and next dependency. Limit context to what the recipient needs.
Keep sensitive information out of unnecessary copies. Define when stale state
must be refreshed and how an interrupted workflow resumes without repeating work.

This skill does not supply a context API, database, cache server, or persistent
memory service. Use the session's actual capabilities. Store new context files
only when they are part of the user's requested deliverable.
""",
    ),
    "error-coordinator": (
        "Analyze recurring failures and cascades across supplied logs or worker outputs, and derive evidence-based recovery and failure-propagation rules.",
        """## Trace failure propagation

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
""",
    ),
    "it-ops-orchestrator": (
        "Coordinate IT operations spanning PowerShell, Windows infrastructure, Azure, Microsoft 365, and security using the available tools and authorized target environment.",
        """## Route IT operations by domain

Identify the target tenant, hosts, environment, privileges, and requested outcome.
Separate language/runtime concerns from Active Directory, DNS, DHCP, GPO, Azure,
Microsoft 365, and security concerns. Prefer the user's existing automation stack.

For Windows or hybrid scripting, distinguish Windows PowerShell 5.1 and its full
.NET dependencies from PowerShell 7 and modern .NET. Check the installed modules
and provider interfaces before writing commands. Sequence discovery, dependent
configuration changes, and service checks using the actual environment.

Use relevant installed skills as optional domain guidance. Delegate only when
authorized and supported, preserving the primary agent's model, reasoning effort,
and service tier. Resolve conflicting recommendations against the real target.
Report changes actually applied and remaining operational dependencies.
""",
    ),
    "knowledge-synthesizer": (
        "Extract recurring lessons and contradictions from supplied logs, transcripts, or workflow history, with traceable evidence and clearly bounded conclusions.",
        """## Synthesize observed patterns

Define the input set and observation period. Group related events or decisions,
retain source locations, and distinguish repeated evidence from duplicate records.
Compare successful and failed cases before claiming a general pattern.

For each finding, explain the supporting observations, counterexamples, applicable
conditions, and uncertainty. Separate correlation from causation. Prefer a narrow
actionable lesson over a universal rule unsupported by the input.

Return the requested synthesis with citations to the supplied artifacts. Do not
claim access to cross-session memory or an organization-wide knowledge service.
Persist a knowledge document only when the user requests that artifact.
""",
    ),
    "performance-monitor": (
        "Analyze supplied metrics, logs, or profiles for performance patterns and anomalies, and specify measurements needed to explain the observed behavior.",
        """## Analyze measured performance

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
""",
    ),
    "task-distributor": (
        "Design a task assignment strategy for actual workers with dependencies, priorities, capacity limits, ownership, and recovery behavior.",
        """## Distribute bounded work

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
""",
    ),
    "workflow-orchestrator": (
        "Design or implement a requested workflow or state machine with explicit transitions, dependency ordering, failure handling, and compensation behavior.",
        """## Define an executable workflow

Identify the existing execution framework, inputs, states, transitions, terminal
conditions, and ownership of side effects. Specify transition guards and outputs.
Model failure and cancellation paths alongside successful execution.

For operations that can repeat, define idempotency and deduplication. Bound retries
and explain which failures need compensation, a forward repair, or manual input.
Identify which state survives interruption and how execution resumes consistently.

Implement through the repository's actual registration and runtime mechanisms
when requested. Compile or load that production structure before behavioral
tests. Otherwise deliver the requested state-machine description. Do not imply
that installing this skill starts an engine or authorizes external side effects.
""",
    ),
}


def normalized_name(name):
    if name == "agent-installer":
        return CATALOG
    result = "va-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if len(result) >= 64 or not re.fullmatch(r"va-[a-z0-9]+(?:-[a-z0-9]+)*", result):
        raise ValueError(f"Invalid skill name: {name}")
    return result


def read_agent(path):
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", raw, re.S)
    if not match:
        raise ValueError(f"Missing frontmatter in {path}")
    front, body = match.groups()
    # Upstream includes unquoted descriptions with colons, so it is not always
    # valid YAML. Read only its known top-level scalar fields, then emit strict
    # JSON-quoted YAML scalars for Codex.
    fields = {}
    key = None
    for line in front.splitlines():
        field = re.match(r"^([a-z][a-z_-]*):\s*(.*)$", line)
        if field:
            key, value = field.groups()
            fields[key] = value
        elif key and line.strip():
            fields[key] += " " + line.strip()
    name = fields.get("name", "").strip().strip("\"'")
    description = fields.get("description", "").strip()
    if description.startswith(('"', "'")) and description[-1:] == description[:1]:
        description = description[1:-1]
    description = re.sub(r"^[>|][-+]?\s*", "", description)
    description = re.split(r"(?:\\n|\n)|<example>|Examples?:", description, maxsplit=1)[0]
    description = description.replace("Use this agent when", "Use when")
    description = description.replace("Invoke this agent", "Use this skill")
    description = description.replace("Claude Code", "Codex")
    description = re.split(r"\s+Triggers on:", description, maxsplit=1)[0]
    description = " ".join(description.split())
    if not name or not description:
        raise ValueError(f"Missing name or description in {path}")
    return name, description, body.strip(), raw


def remove_sections(body):
    lines = []
    excluded_level = None
    excluded_tail = False
    for line in body.splitlines():
        heading = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading:
            level, title = len(heading[1]), heading[2]
            if excluded_level is not None and level <= excluded_level:
                excluded_level = None
            if re.search(r"communication protocol|integration with other agents", title, re.I):
                excluded_level = level
        if re.match(r"^Integration with other agents:\s*$", line, re.I):
            excluded_tail = True
        if excluded_level is None and not excluded_tail:
            lines.append(line)
    return "\n".join(lines)


def domain_guide(body):
    body = remove_sections(body)
    body = re.sub(r"\AYou are\b.*?(?:\n\s*\n|\Z)", "", body, count=1, flags=re.S)
    body = re.sub(r"(?im)^When invoked:\s*\n(?:\d+\.[^\n]*\n?)+", "", body)
    body = re.sub(
        r"(?im)^(?:(?:Delivery|Completion) (?:notification|message(?: format)?|announcement|report|summary)|"
        r"Final report):[^\n]*\n\s*"
        r"(?:```[^\n]*\n[\s\S]*?```|[\"\u201c][^\n]+[\"\u201d])", "", body,
    )

    def clean_code(match):
        code = match[0]
        if '"requesting_agent"' in code or '"agent"' in code:
            return ""
        return code

    body = re.sub(r"```[^\n]*\n[\s\S]*?```", clean_code, body)
    body = re.sub(
        r"(?im)^(?:Progress tracking|Status reporting|Final status update|"
        r"Progress update|Progress monitoring):\s*$", "", body,
    )
    body = re.sub(r"(?im)^.*(?:query|request|consult).*context[- ]manager[^\n]*\n?", "", body)
    body = body.replace("Claude Code subagents", "optional specialist skills")
    body = body.replace("Claude Code", "Codex")
    body = body.replace(".claude/", ".agents/")
    body = body.replace("WebFetch", "available web retrieval")
    body = body.replace("WebSearch", "available web search")
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return (
        "# Domain guide\n\n"
        "Apply the relevant sections to the actual request. This adapted source is\n"
        "a menu of domain considerations, not a requirement to perform every item.\n"
        "Source version numbers and numeric targets are historical examples; use the\n"
        "project's real versions and agreed acceptance criteria. Check current primary\n"
        "documentation before relying on external APIs, standards, or provider behavior.\n"
        "Tool labels describe operations and do not grant unavailable tools or services.\n\n"
        + body + "\n"
    )


def skill_document(name, description, source_name, category, body):
    title = source_name.replace("-", " ").title()
    if source_name in OVERRIDES:
        return f"---\nname: {name}\ndescription: {json.dumps(description)}\n---\n\n# {title}\n\n{OVERRIDES[source_name][1]}"
    workflow = CATEGORY_WORKFLOWS[category[:2]]
    numbered = "\n".join(f"{i}. {step}" for i, step in enumerate(workflow, 1))
    invoked = re.search(r"(?im)^When invoked:\s*\n((?:\d+\.[^\n]*\n?)+)", body)
    focus = []
    if invoked:
        for line in invoked[1].splitlines():
            step = re.sub(r"^\d+\.\s*", "", line).strip()
            if step and not re.search(r"context[- ]manager|other agents|dispatch|delegate", step, re.I):
                focus.append(step.replace("Claude Code", "Codex"))
    focus_text = ""
    if focus:
        focus_text = "\n## Task-specific focus\n\n" + "\n".join("- " + step for step in focus) + "\n"
    return f"""---
name: {name}
description: {json.dumps(description)}
---

# {title}

Use this skill for the capability described above and keep the user's requested
scope, logic placement, and existing project conventions. Read the relevant
sections of [the domain guide](references/guide.md) for detailed considerations;
select the checks that affect this task instead of treating the guide as a
mandatory full-project checklist.

## Workflow

{numbered}
{focus_text}
## Applying the guidance

Use only tools and services actually available in the session. This skill is
instructional guidance; it does not create a subagent, grant tool permissions,
select a model, or supply a context-manager service. Related specialists are
optional; this skill works independently.

Treat source performance numbers, coverage percentages, and version examples as
context, not verified results or universal acceptance gates. Preserve the user's
test and artifact rules. Report only observed outcomes and disclose checks that
could not run. Produce the requested deliverable without creating extra planning
or status files unless the user requests them.
"""


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "source" / "categories")
    parser.add_argument("--output", type=Path, default=ROOT / "skills")
    args = parser.parse_args()
    files = sorted(p for p in args.source.glob("*/*.md") if p.name != "README.md")
    if not files:
        parser.error("No agent sources found")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    entries = []
    documents = {}
    names = set()
    for path in files:
        source_name, description, body, raw = read_agent(path)
        name = normalized_name(source_name)
        if name in names:
            raise ValueError(f"Duplicate generated name: {name}")
        names.add(name)
        if source_name in OVERRIDES:
            description = OVERRIDES[source_name][0]
        if source_name == "content-quality-editor":
            description = "Edit requested prose for clarity, precision, tone, and unnecessary AI-style phrasing. Use when the user asks for editorial review or rewriting."
        if len(description) > 1024:
            raise ValueError(f"Description exceeds 1024 characters: {source_name}")
        category = path.parent.name
        folder = args.output / name
        documents[folder / "SKILL.md"] = skill_document(name, description, source_name, category, body)
        if source_name not in OVERRIDES:
            documents[folder / "references" / "guide.md"] = domain_guide(body)
        display = "Skill Catalog" if name == CATALOG else source_name.replace("-", " ").title()
        short = f"{display}: specialized Codex guidance"
        short = short if len(short) <= 64 else short[:61].rstrip() + "..."
        documents[folder / "agents" / "openai.yaml"] = (
            "interface:\n"
            f"  display_name: {json.dumps(display)}\n"
            f"  short_description: {json.dumps(short)}\n"
            f"  default_prompt: {json.dumps('Use $' + name + ' to help with the following task.')}\n"
        )
        documents[folder / "LICENSE.txt"] = license_text
        entries.append({
            "name": name,
            "source_name": source_name,
            "description": description,
            "category": category,
            "path": f"skills/{name}",
            "source": f"categories/{category}/{path.name}",
            "source_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        })
    catalog = {"schema_version": 1, "repository": COLLECTION, "upstream": UPSTREAM,
               "upstream_revision": REVISION, "skills": entries}
    documents[args.output / CATALOG / "references" / "catalog.json"] = json.dumps(catalog, indent=2) + "\n"
    for path, value in documents.items():
        write(path, value)
    counts = Counter(entry["category"] for entry in entries)
    print(f"Generated {len(entries)} Codex skills in {len(counts)} categories at {args.output}")


if __name__ == "__main__":
    main()
