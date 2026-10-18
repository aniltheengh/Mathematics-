"""Audit chapter coverage, anatomy, practice and reproducible figure pairs.

This is a structural audit, not a proof checker. Mathematical identities and
worked answers have separate verification scripts and mathematical review.
"""
from collections import Counter
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]


def section(text,title):
    match=re.search(r"(?ms)^## "+re.escape(title)+r"\s*\n(.*?)(?=^## |\Z)",text)
    return match.group(1) if match else ""


def main():
    catalog=json.loads((ROOT/"learning/chapter-catalog.json").read_text(encoding="utf-8"))
    errors=[]; words=0; exercises=12; figures=set()
    ids=[]
    for chapter in catalog:
        path=ROOT/chapter["path"]
        text=path.read_text(encoding="utf-8")
        size=len(text.split()); words+=size
        if size<1000:errors.append(f"{path.name}: chapter below 1000-word reference threshold")
        if len(re.findall(r"(?m)^## ",text))<16:
            errors.append(f"{path.name}: missing standard topic sections")
        idmatch=re.search(r"\*\*Topic ID:\*\*\s*([^\n]+)",text)
        if not idmatch:errors.append(f"{path.name}: no topic ID")
        else:ids.append(idmatch.group(1).strip().rstrip("."))
        if chapter["path"].endswith("/cartesian-plane.md"):
            pass  # Its 12 separately linked exercises are checked by check_repository.py.
        else:
            practice=section(text,"Practice problems")
            answers=section(text,"Answers and explanations")
            count=len(re.findall(r"(?m)^\d+\.\s",practice))
            if count<4:errors.append(f"{path.name}: fewer than four enumerated practice problems")
            if not answers:errors.append(f"{path.name}: missing explained answers")
            exercises+=count
        # Display delimiters must pair. Exact TeX rendering is checked in the book build/browser.
        if text.count("$$")%2:errors.append(f"{path.name}: unpaired display-math delimiter")
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)",text):
            figure=(path.parent/target).resolve()
            figures.add(figure)
            if not figure.is_file():errors.append(f"{path.name}: missing {target}")
            elif figure.suffix==".png" and not figure.with_suffix(".svg").is_file():
                errors.append(f"{path.name}: no SVG companion for {target}")
    if len(catalog)!=28 or set(c["group"] for c in catalog)!=set(range(1,26)):
        errors.append("Catalog must cover all 25 subject branches with 28 chapters")
    duplicates=[k for k,v in Counter(ids).items() if v>1]
    if duplicates:errors.append(f"Duplicate chapter IDs: {duplicates}")
    if errors:raise SystemExit("FAIL:\n"+"\n".join(errors))
    print(f"PASS: {len(catalog)} chapters, 25 branches, {words} chapter words, {exercises} practice problems, {len(figures)} linked figures.")
    print("Structural audit only: mathematical proof scope remains explicit within each chapter.")


if __name__=="__main__":
    main()
