# Architecture and technology decisions

[Home](../README.md) · [Contents](../CONTENTS.md)

## Design

The encyclopedia separates mathematical classification from a suggested learning
sequence. The subject map is broad; only finished or actively written material
gets a file. One canonical explanation owns each result. Proof, formula, and
practice indexes link to that explanation.

```text
personal-mathematics-encyclopedia/
  README.md                 entry point and quick start
  INDEX.md                  navigation for available material
  CONTENTS.md               full coverage plan
  CONTRIBUTING.md           contribution and maintenance process
  subjects/
    geometry/
      overview.md
      coordinate-geometry/cartesian-plane.md
  indexes/                  formulas, notation, proofs, practice
  exercises/geometry/       problems, separated from answers
  solutions/geometry/       worked solutions with backlinks
  assets/figures/            tracked PNG and SVG mathematics figures
  notebooks/                optional, portable Jupyter examples
  scripts/                  plot generation and validation
  references/               reading guide and references.bib
  learning/                 learning route, revision guide, progress.csv
  templates/                topic and formula templates
  docs/                     standards, setup, publishing, verification
  .github/workflows/        verification on pushes and pull requests
  myst.yml                  Jupyter Book 2 navigation and metadata
  requirements*.txt         computing and optional publishing dependencies
```

Create future subject directories such as `subjects/linear-algebra/` only when
writing their first useful page. Keep paths lowercase with hyphens. Use stable
topic IDs such as `GEO-CG-001`; do not renumber existing files when adding a topic.

## Technology choices

| Choice | Purpose and constraint |
| --- | --- |
| Markdown and LaTeX | Durable source readable on GitHub and in VS Code |
| Ordinary relative links | Navigation works without a publication server |
| MyST and Jupyter Book 2 | Optional searchable website from the same sources |
| Git and GitHub | Local history, review, remote backup, optional Pages hosting |
| Python, NumPy, Matplotlib | Optional calculations and reproducible plots |
| SymPy | Exact symbolic checks; explanation remains in prose |
| JupyterLab, nbformat, nbclient | Notebook authoring, schema validation, execution |
| SciPy | Optional future numerical work, unnecessary for the first chapter |
| CSV revision tracker | Editable in a text editor or spreadsheet; no learning platform |

The initial book uses ordinary math and headings rather than publisher-specific
theorem directives. **Definition**, **Theorem**, **Assumption**, **Proof**, and
**Example** labels make logical roles explicit on GitHub too.

## Publication boundary

`myst.yml` lists pages that actually exist. `CONTENTS.md` is the subject plan;
it is not an executable site TOC. A new reader should never navigate to an empty
planned chapter. Every published Markdown page belongs in the MyST TOC so links
resolve during strict builds. Code and assets may be linked as downloads.

Jupyter Book 2 uses MyST's document engine. Do not add the legacy Jupyter Book 1
`_config.yml` or `_toc.yml` files. See the official
[installation guide](https://jupyterbook.org/stable/get-started/install/) and
[MyST TOC format](https://mystmd.org/guide/table-of-contents).

## Version and ownership policy

Dependency bounds limit unexpected major upgrades; they are not an exact lock.
Record the tested versions in the verification record. Update deliberately,
rerun checks, and review changed notebook outputs and figures. Do not silently
rewrite personal mastery dates or invent evidence of learning.

There is no selected distribution license. The [reuse policy](reuse-policy.md)
records that decision without choosing permissions on the owner's behalf.
