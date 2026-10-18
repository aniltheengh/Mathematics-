"""Audit guided-lesson delivery independently of symbolic example checks."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def section(text, title):
    match = re.search(r"(?ms)^## "+re.escape(title)+r"\s*\n(.*?)(?=^## |\Z)", text)
    return match.group(1) if match else ""


def main():
    catalog = json.loads((ROOT/"learning/lesson-catalog.json").read_text(encoding="utf-8"))
    errors, ids, figures = [], [], set()
    words = stages = exercises = 0
    for lesson in catalog:
        path = ROOT/lesson["path"]
        text = path.read_text(encoding="utf-8")
        size = len(text.split())
        stage_count = len(re.findall(r"(?m)^## Stage \d+:", text))
        practice = re.findall(r"(?m)^(\d+)\.\s", section(text, "Practice problems"))
        answers = re.findall(r"(?m)^(\d+)\.\s", section(text, "Answers and explanations"))
        expected = [str(i) for i in range(1, len(practice)+1)]
        if size < 1800:
            errors.append(f"{path.name}: below 1800-word depth threshold ({size})")
        if stage_count < 4:
            errors.append(f"{path.name}: fewer than four sequential stages")
        if len(practice) < 8 or practice != expected or answers != expected:
            errors.append(f"{path.name}: need at least eight matching numbered problems/answers")
        identifier = re.search(r"\*\*Lesson ID:\*\*\s*([^\n]+)", text)
        if not identifier or identifier.group(1).strip().rstrip(".") != lesson["topic_id"]:
            errors.append(f"{path.name}: lesson ID mismatch")
        ids.append(lesson["topic_id"])
        if "\\(" in text or "\\)" in text:
            errors.append(f"{path.name}: use GitHub-compatible dollar math delimiters")
        if text.count("$$") % 2:
            errors.append(f"{path.name}: unpaired display delimiter")
        image_paths = {(path.parent/image).resolve() for image in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)}
        if len(image_paths) < 2:
            errors.append(f"{path.name}: fewer than two diagrams")
        for image in image_paths:
            if not image.is_file() or not image.with_suffix(".svg").is_file():
                errors.append(f"{path.name}: missing PNG/SVG pair: {image.name}")
        figures.update(image_paths)
        if (size, stage_count, len(practice)) != (lesson["words"], lesson["stages"], lesson["exercises"]):
            errors.append(f"{path.name}: catalog stale; run refresh_learning_catalogs.py")
        words += size
        stages += stage_count
        exercises += len(practice)
    if len(catalog) != 12 or len(ids) != len(set(ids)):
        errors.append("Expected twelve unique delivered guided lessons")
    if Counter(l["path"].split("/")[1] for l in catalog) != dict.fromkeys(["foundations", "geometry", "analysis", "advanced"], 3):
        errors.append("Expected three lessons in each of the four delivered sequences")
    if errors:
        raise SystemExit("FAIL:\n"+"\n".join(errors))
    print(f"PASS: {len(catalog)} guided lessons; {words} source words; {stages} stages; "
          f"{exercises} explained problems; {len(figures)} PNG/SVG pairs.")
    print("Structure and catalog audit only; examples have separate mathematical checks.")


if __name__ == "__main__":
    main()
