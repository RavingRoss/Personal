from sympy import *
import matplotlib as plt
init_printing()

#x,n = symbols('x n') #Declaring the variables
x,n,i = symbols('x,n,i')

simp = simplify(exp((2*i*x))*exp((-i*n*x)/3))
eq = integrate(simp, x)
real = integrate(simp, (x, (-3*pi), (3*pi)))
#expr = simplify(eq)

#print(eq)
pprint(real)