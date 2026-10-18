"""Independent exact checks for conics, Euclidean formulas and frames."""

import sympy as s


def main():
    count=0
    def check(name, condition):
        nonlocal count
        if not bool(condition):
            raise AssertionError(name)
        count+=1
    x,y,t,u=s.symbols("x y t u", real=True)
    a,b,p=s.symbols("a b p",positive=True)
    check("ellipse parameters",s.trigsimp((a*s.cos(t))**2/a**2+(b*s.sin(t))**2/b**2-1)==0)
    check("hyperbola parameters",s.simplify((a*s.cosh(u))**2/a**2-(b*s.sinh(u))**2/b**2-1)==0)
    check("parabola parameters",s.expand((2*p*t)**2-4*p*(p*t*t))==0)
    check("parabola focus-directrix",s.expand((x-p)**2+y*y-(x+p)**2-(y*y-4*p*x))==0)
    check("shifted ellipse completion",s.expand(9*(x-2)**2+4*(y+1)**2-36-(9*x*x+4*y*y-36*x+8*y+4))==0)
    check("shifted parabola completion",s.expand((y-3)**2-8*(x-1)-(y*y-6*y-8*x+17))==0)
    check("ellipse minor semiaxis",s.sqrt(3**2-2**2)==s.sqrt(5))
    point=s.Point(3,s.Rational(12,5))
    check("ellipse right focal distance",point.distance(s.Point(4,0))==s.Rational(13,5))
    check("ellipse left focal distance",point.distance(s.Point(-4,0))==s.Rational(37,5))
    check("ellipse focal sum",point.distance(s.Point(4,0))+point.distance(s.Point(-4,0))==10)
    point=s.Point(5,s.Rational(8,3))
    check("hyperbola point",point.x**2/9-point.y**2/4==1)
    check("hyperbola tangent",5*point.x-6*point.y==9)
    check("hyperbola derivative",4*point.x/(9*point.y)==s.Rational(5,6))
    rot=s.Matrix([[1,-1],[1,1]])/s.sqrt(2)
    check("rotation orthogonal",s.simplify(rot.T*rot)==s.eye(2))
    v=s.Matrix([x,y]); old=rot*v
    check("rotated ellipse diagonal",s.expand(5*old[0]**2-6*old[0]*old[1]+5*old[1]**2)==2*x*x+8*y*y)
    check("conic exercise 1 focal",16-9==7)
    check("conic exercise 2 focus",-1-3==-4)
    check("conic exercise 3 completion",s.expand(4*(x-2)**2-9*(y+1)**2-36-(4*x*x-9*y*y-16*x-18*y-29))==0)
    check("conic exercise 4 double root",s.factor((x+2)**2-8*x)==(x-2)**2)
    check("focus-origin polar radius",s.simplify(3/(1+s.cos(s.pi/2)/2))==3)
    check("dish focal distance",s.Rational(4**2,16)==1)
    c=s.symbols("c", positive=True)
    check("Heron identity",s.expand(4*a*a*b*b-(a*a+b*b-c*c)**2-
          (a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))==0)
    check("13 14 15 area",s.sqrt(21*8*7*6)==84)
    check("chord length",2*s.sqrt(25-9)==8)
    check("cone slant height",s.sqrt(3**2+4**2)==5)
    check("volume scale",16*s.Rational(3,2)**3==54)
    theta=s.symbols("theta",real=True); r=s.symbols("r",positive=True)
    jac=s.Matrix([r*s.cos(theta),r*s.sin(theta)]).jacobian([r,theta]).det()
    check("polar Jacobian",s.trigsimp(jac)==r)
    check("polar conversion",3*s.cos(2*s.pi/3)==s.Rational(-3,2))
    check("polar conversion y",3*s.sin(2*s.pi/3)==3*s.sqrt(3)/2)
    R=s.Matrix([[0,-1],[1,0]])
    check("active rotation",R*s.Matrix([2,-1])==s.Matrix([1,2]))
    check("passive rotation",R.T*s.Matrix([2,-1])==s.Matrix([-1,-2]))
    check("datum transform",s.Matrix([10,20])+R*s.Matrix([3,4])==s.Matrix([6,23]))
    check("line-plane point",sum(s.Matrix([1,0,2])+s.Rational(3,2)*s.Matrix([1,2,-1]))==6)
    check("plane distance",s.Abs(2*1-2+2*3-1)/s.sqrt(4+1+4)==s.Rational(5,3))
    check("spherical point x",2*s.sin(s.pi/4)*s.cos(s.pi/4)==1)
    check("spherical point z",2*s.cos(s.pi/4)==s.sqrt(2))
    print(f"PASS: {count} exact geometry checks; graph scripts also check sampled implicit residuals.")


if __name__=="__main__":
    main()
