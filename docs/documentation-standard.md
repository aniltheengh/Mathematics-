# Mathematical documentation standard

[Home](../README.md) · [Topic template](../templates/topic-template.md)

## Logical roles

- **Definition:** fixes the meaning of a term; it is not proved.
- **Assumption:** states the domain, hypotheses, coordinate conventions, and units.
- **Theorem / proposition:** a claim under stated hypotheses; supply a proof or an
  exact source and label a missing proof honestly.
- **Derivation:** explains how a formula follows from earlier results. Identify
  any division, limiting operation, or squaring that needs a condition.
- **Intuition:** a mental picture or analogy, explicitly separated from proof.
- **Example:** one concrete use; it is not evidence for a universal statement.
- **Approximation:** use `\approx`, explain rounding, tolerance, and units.

Define every symbol before use, or locally in a compact notation table. Use
`\mathbb{R}` for real numbers, `\in` for membership, and `\subseteq` for inclusion.
Specify whether a result is about points, vectors, functions, or numbers.

## Required topic anatomy

Use the title and classification followed by the 16 topic sections in the template
(the 17 items in the project brief count the title/classification as the first item).
A section may explain that a computational
example or engineering application is unnecessary; it should not contain fake
content merely to fill the template. Keep proofs close to statements. Every
topic has prerequisites, a numerical example, a reasoning exercise, solutions or
direct solution links, mistakes, cross-references, sources, and revision status.

## Mathematics and units

State real versus complex domains, nonzero denominators, positivity conditions,
branch choices, convergence assumptions, differentiability, and independence
where applicable. Include vertical-line and degenerate cases when teaching lines
and circles. A physical coordinate diagram must identify its length unit and
use compatible scales. Never add metres to seconds or use a Euclidean distance
formula on a time-versus-temperature graph.

Keep exact fractions and radicals until the final numerical approximation.
Check answers by substitution or an independent argument. A symbolic computation
checks the encoded expression under its assumptions; it does not replace a
mathematical proof or certify unencoded claims.

## Links and figures

Use descriptive relative Markdown links. Use plain lowercase heading names for
stable anchor targets. If a heading changes, update incoming links. Give figures
descriptive alt text, axes, units where relevant, equal aspect for geometric
lengths, and source code. Commit generated teaching figures and compact notebook
outputs so mathematics is visible without installing software.

## Sources and originality

Write explanations and examples in original words. Cite a verified title,
author or organization, section, and stable URL; add a BibTeX entry where useful.
Never fabricate page numbers, quotations, DOIs, editions, or theorems. Separate
sources supporting the current chapter from recommended future reading.
Do not commit copyrighted textbook PDFs. See the [bibliography](../references/README.md).

## Completion and review

Publication status and learner mastery are separate. A written chapter can be
unassessed for the learner. Before marking a topic written, check conditions,
derivations, arithmetic, solution links, notation, figure labels, references,
and an example outside the easiest special case. Record verification limits.
