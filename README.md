# Personal Mathematics Encyclopedia

**GitHub repository:** [aniltheengh/Mathematics-](https://github.com/aniltheengh/Mathematics-)

A permanent mathematics reference for an engineering graduate rebuilding fluency,
from arithmetic to advanced university mathematics. Read a topic to recover an
idea, follow its proof to understand why it works, and solve a problem to find
out whether you can use it independently.

**Start here:** [Master navigation](INDEX.md) · [Full subject map](CONTENTS.md) ·
[Conic sections](subjects/geometry/coordinate-geometry/conic-sections.md) · [Coverage](COVERAGE.md)

**Study in depth:** [Twelve guided lessons](lessons/README.md), including a
three-part conic sequence, develop the reference material through connected
derivations, worked examples, and additional diagrams.

## What is ready

This edition contains **28 written mathematics chapters across 25 subject branches**,
from arithmetic and proof to calculus, conic sections, differential equations,
probability, numerical methods, topology, tensors, and functional analysis.
Each chapter includes definitions, conditions, exact equations, worked examples,
proofs or derivations, exercises, explained answers, and references. Graphs are
generated from their stated equations, with an optional executed notebook.
The [coverage record](COVERAGE.md) explains the compact-reference depth and
distinguishes proofs developed here from deeper results stated with references.

| Need | Open |
| --- | --- |
| Recover a forgotten idea | [Chapter and section navigation](INDEX.md) |
| Study an idea step by step | [Guided lessons with deeper derivations](lessons/README.md) |
| Look up a formula with its conditions | [Formula index](indexes/formulas.md) |
| Decode a symbol | [Notation](indexes/notation.md) |
| Understand why a result holds | [Proof and derivation index](indexes/proofs.md) |
| Test your understanding | [Practice index](indexes/practice.md) |
| Plan a manageable return to mathematics | [Learning route](learning/learning-path.md) |
| Record your own progress | [Revision method](learning/revision-guide.md) |
| Find a source | [Bibliography](references/README.md) |
| Inspect the graphs | [Figure gallery](indexes/figures.md) |

## Read without installing anything

Open Markdown files in GitHub or in VS Code's Markdown preview. Mathematics uses
`$...$` inline and `$$...$$` on separate lines. All core explanations, diagrams,
proofs, and solutions are available without Python. The notebook also contains
saved outputs for viewing without a running kernel.

For a first session, read through the chapter's worked example on distance and
midpoint, then try exercise CG-01 before looking at its solution.

## Optional Python tools

Use Python 3.11 or later. From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/check_repository.py
.\.venv\Scripts\python.exe scripts/verify_mathematics.py
.\.venv\Scripts\python.exe scripts/plot_coordinate_geometry.py
.\.venv\Scripts\python.exe scripts/execute_notebook.py
.\.venv\Scripts\python.exe -m jupyterlab notebooks/coordinate-geometry.ipynb
```

For the expanded book, also run `python scripts/verify_book_content.py`,
`python scripts/verify_geometry.py`, `python scripts/verify_foundations.py`,
`python scripts/verify_analysis.py`, and `python scripts/verify_advanced.py`.
The explicit interpreter path avoids changing PowerShell's execution policy.
The guided lessons add four subject suites named
<code>scripts/verify_lessons_foundations.py</code>,
<code>scripts/verify_lessons_geometry.py</code>,
<code>scripts/verify_lessons_analysis.py</code>, and
<code>scripts/verify_lessons_advanced.py</code>, plus the structural audit
<code>scripts/verify_guided_lessons.py</code>. Their corresponding plot scripts
reproduce all lesson diagrams. Run
<code>python scripts/refresh_learning_catalogs.py</code> after editing lesson
content to refresh measured counts and navigation while preserving progress.
NumPy, SymPy, Matplotlib, and Jupyter support the initial example. SciPy is
reserved for later numerical mathematics and is listed separately in
[requirements-optional.txt](requirements-optional.txt).

## Optional searchable book

This project uses Jupyter Book **2** and MyST, configured in [myst.yml](myst.yml).
Install [requirements-book.txt](requirements-book.txt) into the same environment,
then follow [Publishing](docs/publishing.md). Publishing uses Node.js as well as
Python. The first build downloads the book theme and needs internet access.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-book.txt
.\.venv\Scripts\python.exe scripts/build_book.py
.\.venv\Scripts\python.exe -m http.server 8765 --bind 127.0.0.1 --directory _build/html
```

Open `http://127.0.0.1:8765` for the static preview. The helper builds in local
temporary storage because the first direct build encountered dependency-write
errors on this Google Drive filesystem. On a regular local working copy,
`jupyter-book build --html --strict` and `jupyter-book start` are also available.

## How the encyclopedia grows

Subjects have one canonical home; other fields link to that explanation.
New topics begin with the [topic template](templates/topic-template.md).
Proofs remain next to their statements, and the indexes point to them rather
than repeating them. Add folders only when they contain useful content.

- [Architecture and technology decisions](docs/architecture.md)
- [Mathematical and editorial standards](docs/documentation-standard.md)
- [Contributing and maintenance](CONTRIBUTING.md)
- [Git and GitHub instructions](docs/git-and-github.md)
- [Verification record](docs/verification.md)

The project repository is [aniltheengh/Mathematics-](https://github.com/aniltheengh/Mathematics-).
The local working copy uses that repository as `origin`. Website publication is
optional and is described separately in the publishing guide. No public license
has been selected; see [reuse policy](docs/reuse-policy.md) before reusing the work.
