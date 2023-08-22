from sympy import *
x , y, z = symbols('x,y,z')
init_printing(use_unicode=False, wrap_line=False)

expr = x+y+5
eq = Eq(expr, 0)
sol = solve(eq, x)
print(sol)
