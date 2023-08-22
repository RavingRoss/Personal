from sympy import *

U = symbols('U')

expr = U**2

plot(expr,title='Entropy vs. Energy of Slope = 1/T',xlabel='Energy (U[J])',ylabel='Entropy (S[J/K])', xlim=[0,10])
