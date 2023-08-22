from sympy import *
#init_printing(use_unicode=False, wrap_line=False)
x,y,z = symbols('x,y,z')

a = integrate((sqrt(1+((y**4,8)+(1,(4*y**2))**2))))

#f = integrate(Rational(a, (y,1,2)))

print(a)