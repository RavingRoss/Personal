from sympy import *

R,T,b,z,a,v = symbols('R,T,b,z,a,v')

init_printing(use_unicode=False, wrap_line=False, use_latex='mathjax')

eq = (R/(v-b))+((R*T)/(v-b)**2)*z**2+((2*a)/(v**3))*z**2
simp = nsimplify(eq)
EQ = Eq(simp, 0)
EQ

sol = solve(EQ, v)
print(sol)

