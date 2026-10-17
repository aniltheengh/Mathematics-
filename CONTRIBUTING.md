# Contribution and maintenance guide

[Home](README.md) · [Standards](docs/documentation-standard.md)

## Add one useful topic

1. Choose its canonical subject and check the subject map for overlap.
2. Copy [the topic template](templates/topic-template.md) into that subject.
   Give it a stable ID, descriptive filename, explicit prerequisites, and actual content.
3. Write the mathematics first. State hypotheses, prove central results, and
   include both a calculation and a conceptual exercise with explained answers.
4. Add credible sources to [the reading guide](references/README.md) and
   [BibTeX database](references/references.bib). Add original plots when useful.
5. Link the new topic from `INDEX.md`, the subject overview, `CONTENTS.md`,
   relevant indexes, and `myst.yml`. Do not create links to future files.
6. Add a progress row with `not-started` mastery. Only the learner changes it.
7. Run the relevant verification commands below, inspect the diff, then commit.

## Verify

```powershell
python scripts/check_repository.py
python scripts/verify_mathematics.py
python scripts/plot_coordinate_geometry.py
python scripts/execute_notebook.py
jupyter-book build --html --strict
git diff --check
git diff
```

The book command requires the optional publication dependencies. The repository
checker checks local paths and heading anchors, notebook schema and saved error
outputs, TOC coverage, bibliography structure, and progress values. It does not
check external link availability or prove mathematical statements. The symbolic
checker covers the first chapter's worked results and exercises. Future topics
need their own checks and human review.

GitHub Actions runs repository checks, mathematical checks, notebook execution,
and a strict book build. It does not deploy the site. A failed check should be
fixed before merging.

## Maintenance rhythm

After each study session, update only the relevant progress row with an honest
result. Monthly, repair broken navigation, reconcile formula entries with their
chapter, and review difficult topics. Before a dependency upgrade, record tested
versions and rerun the notebook and book build. Preserve stable paths; when a
topic moves, update every incoming link in the same commit.

For a mathematical correction, record the faulty claim, counterexample or
correct argument, affected examples and formulas, and the verification performed.
Commit the correction as a focused change. Avoid deleting useful history or
reformatting unrelated chapters with it.
