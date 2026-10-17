"""Check this repository's local navigation, schemas, and content structure.

This intentionally handles the project's ordinary inline Markdown links and
GitHub-style ATX heading anchors, not every extension to Markdown. It does not
contact external websites or validate mathematical proofs.
"""

from collections import Counter
import csv
from datetime import date
from pathlib import Path
import os
import re
from urllib.parse import unquote, urlsplit

import nbformat
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", ".tools", ".cache", "_build", "node_modules", ".myst", "__pycache__"}
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def files():
    for directory, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for name in names:
            yield Path(directory) / name


def without_code(text):
    # Fenced examples can include instructional syntax that isn't a real link.
    text = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


def anchors(text):
    counts = Counter()
    result = set()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", without_code(text)):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        occurrence = counts[slug]
        counts[slug] += 1
        result.add(f"{slug}-{occurrence}" if occurrence else slug)
    return result


def toc_files(entries):
    for entry in entries:
        if "file" in entry:
            yield entry["file"]
        yield from toc_files(entry.get("children", []))


def main():
    errors = []
    sources = {}
    notebooks = []
    all_files = list(files())
    for path in all_files:
        if path.suffix == ".md":
            sources[path.resolve()] = path.read_text(encoding="utf-8")
        elif path.suffix == ".ipynb":
            try:
                notebook = nbformat.read(path, as_version=4)
                nbformat.validate(notebook)
            except Exception as exc:
                errors.append(f"{path.relative_to(ROOT)}: invalid notebook: {exc}")
                continue
            notebooks.append(path)
            sources[path.resolve()] = "\n".join(c.source for c in notebook.cells if c.cell_type == "markdown")
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    if cell.execution_count is None:
                        errors.append(f"{path.name}: code cell {cell.id} has not been executed")
                    if any(o.output_type == "error" for o in cell.outputs):
                        errors.append(f"{path.name}: saved error output in cell {cell.id}")

    link_count = 0
    for source, text in sources.items():
        if "\ufffd" in text:
            errors.append(f"{source.relative_to(ROOT)}: Unicode replacement character")
        for target in LINK.findall(without_code(text)):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            link_count += 1
            destination = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link leaves repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing target {target}")
            elif parsed.fragment and destination in sources:
                if unquote(parsed.fragment) not in anchors(sources[destination]):
                    errors.append(f"{source.relative_to(ROOT)}: missing heading in {target}")

    config = yaml.safe_load((ROOT / "myst.yml").read_text(encoding="utf-8"))
    listed = list(toc_files(config["project"]["toc"]))
    for target in listed:
        if not (ROOT / target).is_file():
            errors.append(f"MyST TOC: missing {target}")
    if len(listed) != len(set(listed)):
        errors.append("MyST TOC: duplicate file entries")
    for path in sources:
        if path.relative_to(ROOT).as_posix() not in listed:
            errors.append(f"MyST TOC: page not listed: {path.relative_to(ROOT)}")

    bib = (ROOT / "references" / "references.bib").read_text(encoding="utf-8")
    keys = re.findall(r"@\w+\s*\{\s*([^,]+),", bib)
    if len(keys) != len(set(keys)) or not keys:
        errors.append("Bibliography: duplicate keys or no entries")
    if bib.count("{") != bib.count("}"):
        errors.append("Bibliography: unbalanced braces")

    allowed = {"not-started", "reviewing", "with-notes", "independent", "needs-practice"}
    with (ROOT / "learning" / "progress.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["topic_id"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Progress: duplicate topic IDs")
    for row in rows:
        if row["status"] not in allowed:
            errors.append(f"Progress: unknown status for {row['topic_id']}")
        if not (ROOT / row["path"]).is_file():
            errors.append(f"Progress: missing topic path for {row['topic_id']}")
        for key in ("last_reviewed", "next_review"):
            if row[key]:
                try:
                    date.fromisoformat(row[key])
                except ValueError:
                    errors.append(f"Progress: invalid {key} for {row['topic_id']}")

    chapter = (ROOT / "subjects/geometry/coordinate-geometry/cartesian-plane.md").read_text(encoding="utf-8")
    if len(re.findall(r"(?m)^## ", chapter)) != 16:
        errors.append("Initial chapter: expected title/classification plus 16 documentation sections")
    for folder in ("exercises", "solutions"):
        text = (ROOT / folder / "geometry/coordinate-geometry.md").read_text(encoding="utf-8")
        exercise_ids = re.findall(r"(?m)^## (CG-\d{2}) ", text)
        if exercise_ids != [f"CG-{i:02d}" for i in range(1, 13)]:
            errors.append(f"{folder}: expected CG-01 through CG-12 exactly once")

    if errors:
        raise SystemExit("FAIL:\n" + "\n".join(errors))
    print(f"PASS: {len(sources)} pages, {link_count} local links, {len(notebooks)} notebook, "
          f"{len(keys)} bibliography entries, {len(rows)} progress row.")
    print("Checked local paths/anchors, TOC coverage, notebook schema/outputs, and chapter structure.")
    print("External URLs and the truth of mathematical prose are outside this check.")


if __name__ == "__main__":
    main()
