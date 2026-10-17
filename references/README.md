# References and reading guide

[Home](../README.md) · [BibTeX database](references.bib)

Use original explanations in the encyclopedia and consult reliable sources for
verification and further study. This bibliography records sources, not ownership
of their text or images. No external textbook files are bundled.

## Sources for the initial material

| Key | Source and locator | Use |
| --- | --- | --- |
| `openstax-coordinate` | Jay Abramson and contributors, *College Algebra 2e*, [§2.1, The Rectangular Coordinate Systems and Graphs](https://openstax.org/books/college-algebra-2e/pages/2-1-the-rectangular-coordinate-systems-and-graphs) | Coordinate pairs, distance, midpoint |
| `openstax-linear` | OpenStax, *College Algebra 2e*, [§4.1, Linear Functions](https://openstax.org/books/college-algebra-2e/pages/4-1-linear-functions) | Slope and line models |
| `ams-msc2020` | AMS / Mathematical Reviews and zbMATH, [MSC2020](https://mathscinet.ams.org/mathscinet/msc/msc2020.html) | Research classification informing the educational subject map |
| `jupyterbook-guide` | Jupyter Book contributors, [Jupyter Book 2 guide](https://jupyterbook.org/stable/) | Optional publication tooling |
| `myst-toc` | MyST contributors, [Table of Contents](https://mystmd.org/guide/table-of-contents) | Book navigation configuration |
| `myst-pages` | MyST contributors, [Deploy to GitHub Pages](https://mystmd.org/guide/deployment-github-pages) | Optional publication procedure |

The circle derivation and point-to-line proof are supplied in full in the
[chapter](../subjects/geometry/coordinate-geometry/cartesian-plane.md#derivations-and-proofs),
using Pythagoras and elementary algebra. They do not rely on an inaccessible
external proof or an invented reference page.

## Recommended next reading

These are suggestions for future chapters, not claims that all their contents
were consulted or implemented here.

- Gilbert Strang, [MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/):
  vectors, matrices, orthogonality, and projections.
- OpenStax, [Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1):
  a free route into functions, limits, derivatives, and integrals.
- Richard Hammack, [Book of Proof](https://richardhammack.github.io/BookOfProof/):
  logic and proof writing for the transition toward rigorous mathematics.

## Add a source

Record author or responsible organization, exact title, edition if verified,
chapter or section if used, stable URL, and what claim it supports. Add a unique
BibTeX key in `references.bib`. Do not invent a year, ISBN, DOI, or page range.
If a source cannot be checked, mark it unverified instead of citing precise details.

Core topic pages use ordinary Markdown links so citations remain usable on
GitHub. The book also loads the BibTeX file for future MyST citation support;
the reading guide stays the human-readable source list.
