"""Refresh lesson navigation and measured counts, preserving personal progress.

Run after editing a chapter/lesson. These counts describe source structure, not
mathematical correctness. The guided lessons remain distinct from references.
"""
from pathlib import Path
import csv
import json
import os
import re

ROOT = Path(__file__).resolve().parents[1]
LESSONS = [
    ("foundations/proof-workshop", "Quantifiers, complete proofs, and counterexamples",
     ["foundations/logic-and-proof"]),
    ("foundations/algebra-and-functions", "Domains, inequalities, composition, and inverses",
     ["algebra/elementary-algebra", "analysis/functions-limits-and-series"]),
    ("foundations/trigonometry-and-vectors", "Rotations, phase, forces, and projections",
     ["trigonometry/trigonometry"]),
    ("geometry/conics-focus-to-equation", "Focal definitions, exact equations, and cone sections",
     ["geometry/coordinate-geometry/conic-sections", "geometry/coordinate-geometry/cartesian-plane"]),
    ("analysis/linear-algebra-and-least-squares", "Bases, rank, projection, QR, and conditioning",
     ["linear-algebra/linear-algebra"]),
    ("analysis/calculus-from-limits-to-models", "Limits, rates, accumulation, and approximation error",
     ["calculus/single-variable-calculus"]),
    ("geometry/conics-tangents-and-reflection", "Tangency, reflected rays, curvature, and normal contacts",
     ["geometry/coordinate-geometry/conic-sections", "differential-geometry/geometry-and-tensors"]),
    ("geometry/conics-matrices-and-classification", "Principal axes, real existence, rank, and degeneracy",
     ["geometry/coordinate-geometry/conic-sections", "geometry/coordinate-geometry/coordinate-systems-and-transformations"]),
    ("analysis/differential-equations-and-stability", "Oscillators, forcing, stability, and heat modes",
     ["differential-equations/ordinary-differential-equations", "differential-equations/partial-differential-equations"]),
    ("advanced/probability-and-inference", "Base rates, variance, likelihood, and intervals",
     ["probability/probability-and-stochastic-processes", "statistics/statistics"]),
    ("advanced/approximation-and-optimization", "Sensitivity, roots, gradient descent, and KKT certificates",
     ["numerical-analysis/numerical-analysis", "optimization/optimization-and-control"]),
    ("advanced/spaces-and-convergence", "Uniform and integral error, projection, completeness, and weak limits",
     ["analysis/real-analysis-and-measure", "functional-analysis/functional-analysis"]),
]


def read(path):
    return (ROOT/path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT/path).write_text(text.rstrip()+"\n", encoding="utf-8", newline="\n")


def section(text, title):
    match = re.search(r"(?ms)^## "+re.escape(title)+r"\s*\n(.*?)(?=^## |\Z)", text)
    return match.group(1) if match else ""


def block(path, name, body, before=None):
    start, end = "<!-- "+name+":start -->", "<!-- "+name+":end -->"
    text = read(path)
    replacement = start+"\n"+body.strip()+"\n"+end
    if start in text:
        text = re.sub(re.escape(start)+r".*?"+re.escape(end), lambda _: replacement, text, flags=re.S)
    elif before:
        assert before in text, (path, before)
        text = text.replace(before, replacement+"\n\n"+before, 1)
    else:
        text = text.rstrip()+"\n\n"+replacement+"\n"
    write(path, text)


def main():
    chapters = json.loads(read("learning/chapter-catalog.json"))
    lessons = []
    for number, (slug, focus, parents) in enumerate(LESSONS, 1):
        path = "lessons/"+slug+".md"
        text = read(path)
        figures = sorted(set((Path(path).parent/target).as_posix()
                             for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)))
        figures = [Path(os.path.relpath((ROOT/f).resolve(), ROOT)).as_posix() for f in figures]
        lessons.append({
            "order": number, "path": path,
            "title": text.splitlines()[0].removeprefix("# "),
            "topic_id": re.search(r"\*\*Lesson ID:\*\*\s*([^\n]+)", text).group(1).strip().rstrip("."),
            "focus": focus, "references": ["subjects/"+p+".md" for p in parents],
            "words": len(text.split()),
            "stages": len(re.findall(r"(?m)^## Stage \d+:", text)),
            "exercises": len(re.findall(r"(?m)^\d+\.\s", section(text, "Practice problems"))),
            "figures": figures,
        })
    write("learning/lesson-catalog.json", json.dumps(lessons, ensure_ascii=False, indent=2))
    # Put direct lesson links beside each chapter's entry navigation.
    for chapter in chapters:
        linked = [l for l in lessons if chapter["path"] in l["references"]]
        if linked:
            entries = [f'[{l["title"]}]({Path(os.path.relpath(ROOT/l["path"], (ROOT/chapter["path"]).parent)).as_posix()})' for l in linked]
            block(chapter["path"], "guided-lessons", "**Study in depth:** "+" · ".join(entries),
                  before="## Prerequisites")
        text = read(chapter["path"])
        chapter["words"] = len(text.split())
    write("learning/chapter-catalog.json", json.dumps(chapters, ensure_ascii=False, indent=2))
    count_words = sum(l["words"] for l in lessons)
    count_exercises = sum(l["exercises"] for l in lessons)
    count_stages = sum(l["stages"] for l in lessons)
    count_figures = len({f for l in lessons for f in l["figures"]})
    intro = """# Guided mathematics lessons

[Home](../README.md) · [Reference chapters](../INDEX.md) · [Practice index](../indexes/practice.md)

These lessons develop a smaller set of ideas through connected steps. Each
states its prerequisites, derives the equations it uses, works through examples,
and ends with problems and explained solutions. The reference chapters remain
the place to look up a definition or standard formula.

Use the order below if you want a systematic return to engineering mathematics.
If the prerequisites are familiar, enter at the lesson that addresses your gap.
Read one stage, reproduce its central calculation without looking, and attempt
a related exercise before moving on. A checkpoint is a chance to explain
reasoning, not just recognize a formula.

The conic sequence has three parts: derive the loci from geometry, use calculus
to study tangent and reflection properties, then classify general quadratics.
The second part needs derivatives; the third needs symmetric matrices. This is
why the route introduces calculus and linear algebra before those two parts.
"""
    table = ["| Order | Lesson | Main work | Stages | Problems |",
             "| ---: | --- | --- | ---: | ---: |"]
    for l in lessons:
        table.append(f'| {l["order"]} | [{l["title"]}]({l["path"].removeprefix("lessons/")}) | {l["focus"]} | {l["stages"]} | {l["exercises"]} |')
    write("lessons/README.md", intro+f"\nThe sequence contains **{len(lessons)} guided lessons, {count_stages} learning stages,\n{count_exercises} additional exercises with explained answers, and {count_figures} new PNG/SVG figure pairs**.\n\n"+
          "\n".join(table)+"""

## Connect a proof, a calculation, and a diagram

Start with the stated assumptions. Check the algebra on paper and use the
diagram to interpret the result. Then check a limiting case, sign, dimension,
or independent substitution. A plotted sample cannot prove a statement for all
points, and a symbolic test of an example is not a proof of a general theorem.
The lessons explicitly distinguish these roles.

Each lesson links its reproducible plot and verification scripts. Diagrams
come from their mathematical data, including endpoint conventions and fixed
parameters. Open the SVG companion in the figure gallery for a scalable copy.
You can study every lesson without installing Python.

## Record evidence of learning

Use the existing [progress tracker](../learning/progress.csv). Lesson IDs and
reference IDs are separate, so reading a lesson does not automatically mark
a subject mastered. Record a solved problem, a proof you reconstructed, or a
specific error to revisit. New entries have no invented review dates.

For a first session, open the focal conic lesson and derive its parabola
equation from the two distances. Then try its first exercise before reading
the answer. If the algebra is unfamiliar, begin with the algebra lesson.
""")
    short = ["## Guided study with more depth", "",
             "[Follow the lesson route](lessons/README.md) for connected derivations, worked examples, and explained practice.", "",
             "| Lesson | Main work |", "| --- | --- |"]
    for l in lessons:
        short.append(f'| [{l["title"]}]({l["path"]}) | {l["focus"]} |')
    block("INDEX.md", "lesson-navigation", "\n".join(short), before="## Reference tools")
    summary = (f"## Guided lesson expansion\n\nThe 28 reference chapters are supplemented by **{len(lessons)} guided lessons** containing\n"
               f"**{count_stages} sequential learning stages, {count_exercises} additional explained exercises,\n"
               f"and {count_figures} additional figure pairs**. The lessons contain approximately\n"
               f"**{count_words:,} whitespace-counted source words**, including mathematical notation.\n"
               "They develop selected topics in more detail; the remaining subjects retain their\n"
               "reference-level scope. [Open the lesson route](lessons/README.md).\n\n"
               "| Lesson | Source words | Stages | Exercises |\n| --- | ---: | ---: | ---: |\n")
    for l in lessons:
        summary += f'| [{l["title"]}]({l["path"]}) | {l["words"]} | {l["stages"]} | {l["exercises"]} |\n'
    block("COVERAGE.md", "lesson-coverage", summary, before="## Equations and graphs")
    coverage = read("COVERAGE.md")
    for c in chapters:
        coverage = re.sub(rf"(\| \[{re.escape(c['title'])}\]\({re.escape(c['path'])}\) \| )\d+( \|)",
                          lambda m:m.group(1)+str(c["words"])+m.group(2), coverage)
    write("COVERAGE.md", coverage)
    for target, header in [("indexes/practice.md", "Guided lesson practice"),
                           ("indexes/proofs.md", "Guided derivations and proofs")]:
        rows = ["## "+header, "", "| Lesson | Practice | Explained answers |",
                "| --- | --- | --- |"]
        for l in lessons:
            rows.append(f'| [{l["title"]}](../{l["path"]}) | [{l["exercises"]} problems](../{l["path"]}#practice-problems) | [Solutions](../{l["path"]}#answers-and-explanations) |')
        if target.endswith("practice.md"):
            rows += ["", f'Total including reference chapters: **{sum(c["exercises"] for c in chapters)+count_exercises} enumerated practice problems**.']
        block(target, "guided-lessons", "\n".join(rows))
    gallery = ["## Guided lesson diagrams", ""]
    for l in lessons:
        gallery += ["### "+l["title"], "", f'[Read the lesson](../{l["path"]})', ""]
        source = read(l["path"])
        for alt, image_path in re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", source):
            f = (ROOT/l["path"]).parent/image_path
            relative = f.resolve().relative_to(ROOT).as_posix()
            gallery += [f"![{alt}](../{relative})", "", f'[Scalable SVG](../{str(Path(relative).with_suffix(".svg")).replace(chr(92), "/")})', ""]
    block("indexes/figures.md", "guided-lessons", "\n".join(gallery))
    with (ROOT/"learning/progress.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields, rows = reader.fieldnames, list(reader)
    known = {r["path"] for r in rows}
    for l in lessons:
        if l["path"] not in known:
            rows.append(dict.fromkeys(fields, "") | {
                "topic_id": l["topic_id"], "title": l["title"], "path": l["path"],
                "status": "not-started", "next_action": "Reconstruct one derivation and attempt exercise 1"})
    with (ROOT/"learning/progress.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Refreshed {len(lessons)} lessons: {count_words} words, {count_stages} stages, "
          f"{count_exercises} exercises, {count_figures} new figures; preserved progress fields.")


if __name__ == "__main__":
    main()
