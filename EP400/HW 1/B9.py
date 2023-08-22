import math

def gamma_riemann(x, n):
    # Define the interval for the Riemann sum
    a = 0.1
    b = 6000
    h = (b - a) / n
    # Define the function to be integrated
    f = lambda t: t**(x)*math.exp(-t)
    # Calculate the Riemann sum
    riemann_sum = 0
    for i in range(n):
        t = a + i * h
        riemann_sum += f(t)
    riemann_sum *= h
    return riemann_sum

# Test the function
x = 1/3
n = 1000
act = math.gamma(x)
approx = gamma_riemann(x, n)

print("Approximation of gamma function at",x,':',approx)
print('Value given by built-in Gamma function: ',act)
print('Approximation error:', ((act-approx)/act)*100)