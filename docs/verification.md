# Verification record

[Home](../README.md) · [Verification tools](../CONTRIBUTING.md#verify)

This file records checks run on 2026-10-17 (Asia/Tokyo) for the initial edition
and their limits. Source presence alone does not establish successful execution.

## Expanded edition on 2026-10-18

The repository now contains **28 mathematics chapters across all 25 subject
branches**, approximately **46,500 chapter words**, **140 enumerated practice
problems with explained answers**, and **31 PNG/SVG figure pairs**. There are
53 Markdown/notebook publication pages and 28 personal progress rows. Personal
mastery remains unassessed; the new rows contain no invented study dates.

Observed expansion checks:

- Repository validation passed for all 53 pages and 618 local links.
- The coverage audit passed for 28 substantive chapters, standard topic anatomy,
  unique IDs, explained practice, paired display equations, and figure companions.
- Five mathematical/graph suites passed **320 checks in total**: 37 original
  coordinate checks, 36 added geometry checks, 65 foundations checks, 131 analysis
  checks, and 51 advanced checks. The analysis count includes sampling, figure,
  and structure checks, so the total is not described as 320 formal proofs.
- All new plotting scripts executed. Figures were inspected against their
  equations, axis conventions, parameters, and labels. The dedicated conic suite
  includes focal geometry, reflection, asymptotes, a rotated ellipse, and
  degenerate real loci.
- A strict Jupyter Book build succeeded for **all 53 HTML pages** in temporary
  local storage, and the output was copied to `_build/html`.
- The generated HTML contained 4,182 rendered KaTeX instances and no
  `katex-error` elements in the inspected build.
- Independent subject reviews checked worked answers and assumptions. Corrections
  included finite-rank boundedness, periodic domains, Pascal boundary conventions,
  a zero-coefficient Diophantine case, theorem hypotheses, and consistent complex
  inner products. Deep theorems cited without full proofs remain explicitly labeled.

The scripts are reproducible checks of encoded mathematics and content structure,
not a formal certification of all prose. The book's [coverage record](../COVERAGE.md)
states its compact-reference depth. GitHub Actions repeats the suites and strict
build on each push; consult the repository's Actions page for the current remote run.

The sections below preserve the original setup record from 2026-10-17.

## Scope

The initial edition has one coordinate geometry chapter, twelve exercises with
solutions, a notebook, reference indexes, and the infrastructure for later
subjects. The full subject map is a plan; future mathematics has not been written
or verified.

## Reproduce

```powershell
python scripts/verify_mathematics.py
python scripts/plot_coordinate_geometry.py
python scripts/execute_notebook.py
python scripts/check_repository.py
jupyter-book build --html --strict
git diff --check
```

The repository checker has a deliberately limited Markdown parser appropriate
to this project. It checks local inline links and ATX heading anchors, not every
possible Markdown feature. It does not contact external links. Mathematical
checks validate encoded cases and identities under the chapter's assumptions;
they do not constitute a formal proof of every prose statement.

## Execution results

| Check | Observed result |
| --- | --- |
| Exact mathematical checks | 37 passed, covering chapter examples, CG-01 through CG-12, and general circle, intersection, and perpendicular-foot identities |
| Notebook execution | All 5 code cells ran in a fresh Python kernel; saved outputs contain two plots and no errors |
| Local navigation | All 24 pages passed local path and heading-anchor checks; the checker prints the current link count |
| Content structure | Title/classification plus 16 topic sections; CG-01 through CG-12 occur once in problems and once in solutions |
| Book | Jupyter Book 2 strict HTML build passed for all 24 pages from a temporary local copy; generated HTML copied to `_build/html` |
| Figures | All three PNG figures generated and visually inspected; point labels, dimensions, equal aspect ratios, and equations agree with the chapter |
| Browser inspection | Local chapter opened in Edge; distance and line equations rendered; all three chapter images loaded; no KaTeX error elements found; searching for midpoint returned chapter sections, proof, problems, and solutions |
| Git | Initial local setup completed on 2026-10-17. Prepared for the user-selected `aniltheengh/Mathematics-` repository on 2026-10-18, preserving its existing main history and Python ignore rules; tools, caches, and builds excluded from the upload |

The first direct HTML build on the Google Drive mount failed while npm unpacked
theme dependencies (`EBADF` / write errors). Building the same content in a
temporary local directory succeeded. The supplied
[build helper](../scripts/build_book.py) supports that route. This is a filesystem
workaround, not a change to the mathematical source.

The notebook execution emitted a Windows asyncio/ZeroMQ compatibility warning
but completed successfully. No notebook error output was saved.

## Tested environment

| Tool | Version |
| --- | --- |
| Python | 3.14.3 |
| NumPy | 2.4.2 |
| SymPy | 1.14.0 |
| Matplotlib | 3.10.8 |
| JupyterLab | 4.5.6 |
| nbformat | 5.10.4 |
| nbclient | 0.10.4 |
| ipykernel | 7.2.0 |
| PyYAML | 6.0.3 |
| Jupyter Book | 2.1.7 (installed into ignored `.tools` for local verification) |
| MyST engine | 1.11.0 (reported by the Jupyter Book command) |
| Node.js | 22.16.0 |
| Git | 2.49.0.windows.1 |

The dependency files use compatible version ranges rather than an exact
environment lock. The GitHub workflow targets Python 3.12 and Node.js 24; that
remote workflow has been supplied but has not been run on GitHub in this session.
Future subject chapters, formal proof certification, cross-platform behavior,
and public Pages deployment have not been verified by these local checks.
