"""Exact checks for the three guided conic lessons; not a prose proof checker."""
import sympy as s

x, y, u, v, p = s.symbols("x y u v p", real=True)
checks = 0


def equal(left, right=0):
    global checks
    difference = left-right
    if isinstance(difference, s.MatrixBase):
        assert all(s.simplify(entry) == 0 for entry in difference)
    else:
        assert s.simplify(difference) == 0, difference
    checks += 1


def main():
    global checks
    equal((x-p)**2+y*y-(x+p)**2, y*y-4*p*x)
    equal(s.Rational(9, 8)*8, 9)
    equal(3*x*x+4*y*y-6*x-9, 3*(x-1)**2+4*y*y-12)
    equal(x*x+y*y-4*(x+3)**2, -3*((x+4)**2-4-y*y/3))
    for cx, cy, d1, d2 in [(3, s.Rational(12, 5), s.Rational(37, 5), s.Rational(13, 5))]:
        equal(s.sqrt((cx+4)**2+cy**2), d1)
        equal(s.sqrt((cx-4)**2+cy**2), d2)
        equal(d2/(s.Rational(25, 4)-cx), s.Rational(4, 5))
    equal((s.Rational(1, 2)*x+1)**2-x*x-y*y,
          -s.Rational(3, 4)*(x-s.Rational(2, 3))**2-y*y+s.Rational(4, 3))
    equal(1-s.Rational(4, 3)/s.Rational(20, 9), s.Rational(2, 5))
    a, b, m, k = s.symbols("a b m k", nonzero=True, real=True)
    discriminant = (2*m*k/b**2)**2-4*(1/a**2+m*m/b**2)*(k*k/b**2-1)
    equal(discriminant, 4*(a*a*m*m+b*b-k*k)/(a*a*b*b))
    for slope in [s.Rational(4, 5), -s.Rational(4, 5)]:
        contact = s.Matrix([-5*slope, s.Rational(9, 5)])
        equal(contact[0]**2/25+contact[1]**2/9, 1)
        equal(contact[1]-slope*contact[0], 5)
    incident = s.Matrix([s.Rational(35, 37), s.Rational(12, 37)])
    normal = s.Matrix([9, 20])/s.sqrt(481)
    outgoing = incident-2*incident.dot(normal)*normal
    equal(outgoing, s.Matrix([s.Rational(5, 13), -s.Rational(12, 13)]))
    equal(outgoing.dot(outgoing), 1)
    normal = s.Matrix([-1, 1])/s.sqrt(2)
    incident = s.Matrix([-1, 0])
    equal(incident-2*incident.dot(normal)*normal, s.Matrix([0, -1]))
    t = s.symbols("t", real=True)
    param = s.Matrix([p*t*t, 2*p*t])
    tangent = param.diff(t)
    equal(tangent.dot(s.Matrix([-1, t])))
    X, Y = s.symbols("X Y", real=True)
    equal((param+(p*t*t-X)*s.Matrix([-1, t]))[1]-Y,
          p*t**3+(2*p-X)*t-Y)
    equal(s.factor((p*t**3+(2*p-X)*t-Y).subs({p:1, X:3, Y:0})), t*(t-1)*(t+1))
    equal(t**3-3*t-2, (t-2)*(t+1)**2)
    # Squared curvature avoids assumptions about the signs of a, b, and p.
    curve = s.Matrix([a*s.cos(t), b*s.sin(t)])
    first, second = curve.diff(t), curve.diff(t, 2)
    equal(s.det(s.Matrix.hstack(first, second)), a*b)
    equal(first.dot(first), a*a*s.sin(t)**2+b*b*s.cos(t)**2)
    equal(s.det(s.Matrix.hstack(tangent, param.diff(t, 2))), -4*p*p)
    equal(tangent.dot(tangent), 4*p*p*(1+t*t))
    Q = s.Matrix([[5, -3], [-3, 5]])
    ell = s.Matrix([-16, 16])
    center = s.Matrix([1, -1])
    R = s.Matrix([[1, -1], [1, 1]])/s.sqrt(2)
    equal(2*Q*center+ell, s.zeros(2, 1))
    equal(R.T*R, s.eye(2))
    equal(R.det(), 1)
    equal(R.T*Q*R, s.diag(2, 8))
    equal((center.T*Q*center)[0]+ell.dot(center)+8, -8)
    z = center+R*s.Matrix([u, v])
    equal(5*z[0]**2-6*z[0]*z[1]+5*z[1]**2-16*z[0]+16*z[1]+8,
          2*u*u+8*v*v-8)
    H = Q.row_join(ell/2).col_join((ell.T/2).row_join(s.Matrix([[8]])))
    equal(H.det(), -128)
    z = R*s.Matrix([u, v])
    equal((z[0]+z[1])**2-4*z[0]+4*z[1], 2*u*u+4*s.sqrt(2)*v)
    equal(R*s.Matrix([0, -1/s.sqrt(2)]), s.Matrix([s.Rational(1,2), -s.Rational(1,2)]))
    equal(s.Matrix([[0,0,-2*p],[0,1,0],[-2*p,0,0]]).det(), -4*p*p)
    lam, alpha, beta, const = s.symbols("lam alpha beta const", real=True)
    equal(s.Matrix([[lam,0,alpha/2],[0,0,beta/2],[alpha/2,beta/2,const]]).det(),
          -lam*beta*beta/4)
    equal(x*y+x-y-1, (x-1)*(y+1))
    equal(4*x*x+9*y*y-8*x+36*y+31, 4*(x-1)**2+9*(y+2)**2-9)
    equal(x*x-y*y-2*x-4*y-3, (x-1)**2-(y+2)**2)
    equal(1-s.Rational(1,1)/s.Rational(9,4), s.Rational(5,9))
    equal(((1-t*t)/(1+t*t))**2+(2*t/(1+t*t))**2, 1)
    equal((5*(1-t*t)/(1+t*t)).subs(t, s.Rational(1,2)), 3)
    equal((6*t/(1+t*t)).subs(t, s.Rational(1,2)), s.Rational(12,5))
    hyper = s.Matrix([[2,4],[4,2]])
    equal(R.T*hyper*R, s.diag(6,-2))
    hx, hy = s.sqrt(2)-s.sqrt(3), s.sqrt(2)+s.sqrt(3)
    equal(2*hx*hx+8*hx*hy+2*hy*hy-12)
    print(f"PASS: {checks} exact guided-conic identities and worked-answer checks.")


if __name__ == "__main__":
    main()
