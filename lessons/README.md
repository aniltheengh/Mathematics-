# Guided mathematics lessons

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

The sequence contains **12 guided lessons, 64 learning stages,
96 additional exercises with explained answers, and 24 new PNG/SVG figure pairs**.

| Order | Lesson | Main work | Stages | Problems |
| ---: | --- | --- | ---: | ---: |
| 1 | [Proof workshop: turn a claim into a justified argument](foundations/proof-workshop.md) | Quantifiers, complete proofs, and counterexamples | 5 | 8 |
| 2 | [Algebra and functions: preserve meaning through every transformation](foundations/algebra-and-functions.md) | Domains, inequalities, composition, and inverses | 5 | 8 |
| 3 | [Trigonometry and vectors: rotation, phase, and mechanical projections](foundations/trigonometry-and-vectors.md) | Rotations, phase, forces, and projections | 6 | 8 |
| 4 | [Conics I: from a geometric constraint to an equation](geometry/conics-focus-to-equation.md) | Focal definitions, exact equations, and cone sections | 6 | 8 |
| 5 | [Linear maps, bases, and least squares](analysis/linear-algebra-and-least-squares.md) | Bases, rank, projection, QR, and conditioning | 5 | 8 |
| 6 | [Calculus from limits to models](analysis/calculus-from-limits-to-models.md) | Limits, rates, accumulation, and approximation error | 5 | 8 |
| 7 | [Conics II: tangents, normals, curvature, and reflection](geometry/conics-tangents-and-reflection.md) | Tangency, reflected rays, curvature, and normal contacts | 6 | 8 |
| 8 | [Conics III: classify every real quadratic without guessing](geometry/conics-matrices-and-classification.md) | Principal axes, real existence, rank, and degeneracy | 7 | 8 |
| 9 | [Differential equations: models, modes, and stability](analysis/differential-equations-and-stability.md) | Oscillators, forcing, stability, and heat modes | 5 | 8 |
| 10 | [From base rates to evidence: a guided probability and inference lesson](advanced/probability-and-inference.md) | Base rates, variance, likelihood, and intervals | 4 | 8 |
| 11 | [Approximation and optimization: decide what an error means](advanced/approximation-and-optimization.md) | Sensitivity, roots, gradient descent, and KKT certificates | 5 | 8 |
| 12 | [Spaces and convergence: what does it mean to get close?](advanced/spaces-and-convergence.md) | Uniform and integral error, projection, completeness, and weak limits | 5 | 8 |

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
