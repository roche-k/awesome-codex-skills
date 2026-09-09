#!/usr/bin/env python3
"""Discover and manage the independently installable skills in this collection."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile


SKILL_ROOT = Path(__file__).resolve().parents[1]
COLLECTION = "https://github.com/roche-k/awesome-codex-skills"
MARKER = ".awesome-codex-skills.json"


class CatalogError(Exception):
    """An actionable catalog, selection, or filesystem error."""


def read_catalog():
    data = json.loads((SKILL_ROOT / "references" / "catalog.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("repository") != COLLECTION:
        raise CatalogError("Unsupported catalog schema or collection")
    entries = data["skills"]
    seen = set()
    for entry in entries:
        name = entry["name"]
        if not re.fullmatch(r"va-[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in seen:
            raise CatalogError(f"Invalid or duplicate catalog name: {name}")
        if entry["path"] != f"skills/{name}":
            raise CatalogError(f"Invalid package path for {name}")
        seen.add(name)
    return entries


def select(entries, names=(), category=None, all_skills=False):
    if category is not None and category not in {entry["category"] for entry in entries}:
        raise CatalogError(f"Unknown category: {category}. Run 'categories' to list choices.")
    aliases = {}
    for entry in entries:
        for key in (entry["name"], entry["name"][3:], entry["source_name"]):
            aliases[key] = entry
    chosen = {}
    for name in names:
        if name not in aliases:
            raise CatalogError(f"Unknown skill: {name}. Run 'search' or 'list' to find its name.")
        entry = aliases[name]
        chosen[entry["name"]] = entry
    if category is not None or all_skills:
        for entry in entries:
            if all_skills or entry["category"] == category:
                chosen[entry["name"]] = entry
    if not chosen:
        raise CatalogError("Choose at least one skill, a category, or --all.")
    return sorted(chosen.values(), key=lambda entry: entry["name"])


def inventory(directory):
    if directory.is_symlink() or not directory.is_dir():
        raise CatalogError(f"Expected a real skill directory: {directory}")
    files = {}
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            raise CatalogError(f"Refusing a symlink inside a skill package: {path}")
        relative = path.relative_to(directory).as_posix()
        if path.is_dir():
            continue
        if not path.is_file():
            raise CatalogError(f"Unsupported file type: {path}")
        if relative != MARKER:
            files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    if "SKILL.md" not in files:
        raise CatalogError(f"Missing SKILL.md: {directory}")
    return files


def managed_files(directory, name):
    if directory.is_symlink():
        raise CatalogError(f"Refusing a symlink destination: {directory}")
    marker = directory / MARKER
    if marker.is_symlink() or not marker.is_file():
        raise CatalogError(f"Unmanaged destination; preserve it manually before replacing: {directory}")
    data = json.loads(marker.read_text(encoding="utf-8"))
    if data.get("collection") != COLLECTION or data.get("name") != name:
        raise CatalogError(f"Destination belongs to another installation: {directory}")
    actual = inventory(directory)
    if actual != data.get("files"):
        raise CatalogError(f"Locally modified skill; preserve your edits before replacing: {directory}")
    return actual


def destination(args):
    if args.dest is not None:
        return args.dest.expanduser().resolve()
    if args.project is not None:
        project = args.project.expanduser().resolve()
        if not project.is_dir():
            raise CatalogError(f"Project directory does not exist: {project}")
        return project / ".agents" / "skills"
    return Path.home() / ".agents" / "skills"


def package_root(args):
    root = args.source.expanduser().resolve() if args.source else SKILL_ROOT.parents[1]
    if not (root / "skills" / "va-skill-catalog" / "SKILL.md").is_file():
        raise CatalogError("A local collection clone is required. Pass --source /path/to/awesome-codex-skills before the command.")
    return root


def install(args, entries):
    selected = select(entries, args.names, args.category, args.all)
    root = package_root(args)
    dest = destination(args)
    source_skills = (root / "skills").resolve()
    resolved_dest = dest.resolve()
    if resolved_dest == source_skills or source_skills in resolved_dest.parents:
        raise CatalogError("The installation destination must be outside the source skills directory.")
    operations = []
    for entry in selected:
        source = root / entry["path"]
        if source.resolve().parent != source_skills or source.is_symlink():
            raise CatalogError(f"Invalid source package: {source}")
        files = inventory(source)
        target = dest / entry["name"]
        if target.exists() or target.is_symlink():
            current = managed_files(target, entry["name"])
            if current != files:
                raise CatalogError(f"A different version is installed at {target}; uninstall its unchanged copy before updating.")
            operations.append((entry, source, target, files, False))
        else:
            operations.append((entry, source, target, files, True))
    # Preflight every selected destination before the first filesystem mutation.
    for entry, source, target, files, changed in operations:
        if not changed:
            print(f"Already installed: {entry['name']} -> {target}")
            continue
        if args.dry_run:
            print(f"Would install: {entry['name']} -> {target}")
            continue
        dest.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=dest) as temporary:
            stage = Path(temporary) / entry["name"]
            shutil.copytree(source, stage)
            # Keep installed copies independent of the source clone and record
            # ownership so uninstall never silently removes local customizations.
            if inventory(stage) != files:
                raise CatalogError(f"Source package changed during installation: {source}")
            (stage / MARKER).write_text(json.dumps({
                "collection": COLLECTION, "name": entry["name"], "files": files,
            }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            if target.exists() or target.is_symlink():
                raise CatalogError(f"Destination appeared during installation: {target}")
            stage.rename(target)
        print(f"Installed: {entry['name']} -> {target}")


def uninstall(args, entries):
    selected = select(entries, args.names)
    dest = destination(args)
    targets = []
    for entry in selected:
        target = dest / entry["name"]
        exists = target.exists() or target.is_symlink()
        if exists:
            managed_files(target, entry["name"])
        targets.append((entry, target, exists))
    for entry, target, exists in targets:
        if not exists:
            print(f"Not installed: {entry['name']} -> {target}")
        elif args.dry_run:
            print(f"Would uninstall: {entry['name']} -> {target}")
        else:
            shutil.rmtree(target)
            print(f"Uninstalled: {entry['name']} -> {target}")


def installed(args, entries):
    dest = destination(args)
    found = False
    for entry in entries:
        target = dest / entry["name"]
        if target.exists() or target.is_symlink():
            found = True
            try:
                managed_files(target, entry["name"])
                state = "managed, unchanged"
            except (CatalogError, ValueError, OSError) as error:
                state = str(error)
            print(f"{entry['name']}\t{state}\t{target}")
    if not found:
        print(f"No collection skills installed in {dest}")


def add_destination(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dest", type=Path, help="Explicit skills directory")
    group.add_argument("--project", type=Path, help="Install under PROJECT/.agents/skills")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Local collection clone, needed only for installation")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("categories", help="List categories and counts")
    listing = sub.add_parser("list", help="List skill names and descriptions")
    listing.add_argument("--category")
    search = sub.add_parser("search", help="Search names, descriptions, and categories")
    search.add_argument("query")
    show = sub.add_parser("show", help="Show a skill's catalog entry")
    show.add_argument("name")
    install_parser = sub.add_parser("install", help="Install selected skills without overwriting local edits")
    install_parser.add_argument("names", nargs="*")
    install_parser.add_argument("--category")
    install_parser.add_argument("--all", action="store_true")
    install_parser.add_argument("--dry-run", action="store_true")
    add_destination(install_parser)
    uninstall_parser = sub.add_parser("uninstall", help="Remove unchanged skills managed by this tool")
    uninstall_parser.add_argument("names", nargs="+")
    uninstall_parser.add_argument("--dry-run", action="store_true")
    add_destination(uninstall_parser)
    installed_parser = sub.add_parser("installed", help="List managed, modified, and conflicting destinations")
    add_destination(installed_parser)
    args = parser.parse_args()
    try:
        entries = read_catalog()
        if args.command == "categories":
            for category, count in sorted(Counter(entry["category"] for entry in entries).items()):
                print(f"{category}\t{count}")
        elif args.command in {"list", "search"}:
            if args.command == "list":
                matches = select(entries, category=args.category, all_skills=args.category is None)
            else:
                query = args.query.casefold()
                matches = [entry for entry in entries if query in " ".join(
                    entry[key] for key in ("name", "source_name", "description", "category")
                ).casefold()]
            for entry in matches:
                print(f"{entry['name']}\t{entry['category']}\t{entry['description']}")
            if not matches:
                print("No matching skills.")
        elif args.command == "show":
            print(json.dumps(select(entries, [args.name])[0], indent=2, ensure_ascii=False))
        elif args.command == "install":
            install(args, entries)
        elif args.command == "uninstall":
            uninstall(args, entries)
        elif args.command == "installed":
            installed(args, entries)
    except (CatalogError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
