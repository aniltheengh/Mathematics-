"""Independent exact checks for the chapter and all twelve exercise answers.

SymPy's geometric objects provide checks independent of the printed arithmetic.
These checks supplement, rather than replace, the prose proofs.
"""

import sympy as sp
from sympy import Circle, Line, Point, Rational, Segment


def main():
    passed = 0

    def check(label, condition):
        nonlocal passed
        if not bool(condition):
            raise AssertionError(label)
        passed += 1

    x, y = sp.symbols("x y", real=True)
    a, b = Point(1, 2), Point(7, 10)
    check("Chapter distance", a.distance(b) == 10)
    check("Chapter midpoint", Segment(a, b).midpoint == Point(4, 6))
    line = Line(a, b)
    check("Chapter slope", line.slope == Rational(4, 3))
    check("Chapter implicit line", sp.expand(line.equation(x, y).subs(y, (4*x + 2)/3)) == 0)
    check("Chapter perpendicular", line.is_perpendicular(Line(a, a + Point(4, -3))))
    circle = Circle(Point(2, -1), 3)
    check("Chapter circle expansion", sp.expand(circle.equation(x, y) - (x*x + y*y - 4*x + 2*y - 4)) == 0)
    check("Chapter circle intersections", set(circle.intersection(Line(Point(0, -1), Point(1, -1))))
          == {Point(-1, -1), Point(5, -1)})

    a, b = Point(-2, 1), Point(4, 9)
    check("CG-01 distance", a.distance(b) == 10)
    midpoint = Segment(a, b).midpoint
    check("CG-01 midpoint", midpoint == Point(1, 5))
    check("CG-01 halves", a.distance(midpoint) == midpoint.distance(b) == 5)
    line2 = Line(Point(1, -2), Point(5, 6))
    check("CG-02 slope", line2.slope == 2)
    check("CG-02 line", line2.contains(Point(0, -4)) and line2.contains(Point(2, 0)))
    vertical = Line(Point(-3, 5), Point(-3, -2))
    check("CG-03 vertical", vertical.contains(Point(-3, 100)))
    check("CG-03 perpendicular", vertical.is_perpendicular(Line(Point(0, 5), Point(1, 5))))
    first = Line(Point(0, 8), Point(4, 0))
    second = Line(Point(1, 0), Point(0, -1))
    check("CG-04 intersection", first.intersection(second) == [Point(3, 2)])
    base = Line(Point(0, -3), Point(2, 1))
    coincident = Line(Point(1, -1), Point(3, 3))
    parallel = Line(Point(0, Rational(-7, 2)), Point(1, Rational(-3, 2)))
    check("CG-05 coincident", base.equals(coincident))
    check("CG-05 distinct parallel", base.is_parallel(parallel) and base.intersection(parallel) == [])
    c6 = Circle(Point(3, -2), 5)
    check("CG-06 expansion", sp.expand(c6.equation(x, y) - (x*x + y*y - 6*x + 4*y - 12)) == 0)
    check("CG-06 intersections", set(c6.intersection(Line(Point(0, -2), Point(1, -2))))
          == {Point(-2, -2), Point(8, -2)})
    c7 = Circle(Point(0, 0), 5)
    sloping = Line(Point(0, 1), Point(1, 2))
    check("CG-07 intersections", set(c7.intersection(sloping)) == {Point(-4, -3), Point(3, 4)})
    p = Point(4, 1)
    l8 = Line(Point(2, 1), Point(6, -2))  # 3x+4y-10=0
    check("CG-08 distance", l8.distance(p) == Rational(6, 5))
    check("CG-08 foot", l8.projection(p) == Point(Rational(82, 25), Rational(1, 25)))
    a9, b9 = Point(100, 50), Point(400, 450)
    check("CG-09 spacing", a9.distance(b9) == 500)
    check("CG-09 midpoint", Segment(a9, b9).midpoint == Point(250, 250))
    check("CG-09 radius", Point(250, 250).distance(a9) == Point(250, 250).distance(b9) == 250)
    completed = (x + 1)**2 + (y - 2)**2
    check("CG-10 point locus identity", sp.expand(completed - (x*x + y*y + 2*x - 4*y + 5)) == 0)
    check("CG-10 empty locus identity", sp.expand(completed + 1 - (x*x + y*y + 2*x - 4*y + 6)) == 0)
    check("CG-10 nonnegative sum", completed.is_nonnegative is True)
    bisector = sp.expand((x + 2)**2 + y*y - ((x - 4)**2 + y*y))
    check("CG-11 locus", sp.solve(bisector, x) == [1])
    check("CG-11 converse", bisector.subs(x, 1) == 0)
    segment = Segment(Point(0, 0), Point(1, 0))
    p12 = Point(3, 4)
    check("CG-12 infinite line distance", Line(segment.p1, segment.p2).distance(p12) == 4)
    check("CG-12 segment distance", segment.distance(p12) == 2 * sp.sqrt(5))

    # Symbolic identities verify the general expressions under the stated domains.
    aa, bb, cc, x0, y0 = sp.symbols("a b c x0 y0", real=True)
    q, s = aa*aa + bb*bb, aa*x0 + bb*y0 + cc
    hx, hy = x0 - aa*s/q, y0 - bb*s/q
    check("General foot membership (q nonzero)", sp.simplify(aa*hx + bb*hy + cc) == 0)
    check("General squared distance (q nonzero)",
          sp.simplify((x0-hx)**2 + (y0-hy)**2 - s*s/q) == 0)
    u, v, w = sp.symbols("u v w", real=True)
    check("General circle completion", sp.expand(
        (x + u/2)**2 + (y + v/2)**2 - (u*u + v*v)/4 + w
        - (x*x + y*y + u*x + v*y + w)) == 0)
    a1, b1, c1, a2, b2, c2 = sp.symbols("a1 b1 c1 a2 b2 c2", real=True)
    det = a1*b2 - a2*b1
    ix, iy = (b1*c2 - b2*c1)/det, (c1*a2 - c2*a1)/det
    check("General intersection first line (D nonzero)", sp.simplify(a1*ix+b1*iy+c1) == 0)
    check("General intersection second line (D nonzero)", sp.simplify(a2*ix+b2*iy+c2) == 0)
    print(f"PASS: {passed} exact checks; chapter examples, CG-01 through CG-12, and general identities.")
    print("General rational identities assume the nonzero denominators stated in the chapter.")


if __name__ == "__main__":
    main()
