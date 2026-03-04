import numpy as np
import astropy.constants as const
import astropy.units as u

first_term = (const.k_B**4)/(4*np.pi**2 * const.c**2 * const.hbar**3)
def f(x):
    (x**3)/(np.exp(x) - 1)
    return x

def x(z):
    x= (z)/(z-1)
    return x

def integrand(z):
    a = (1)/((z-1)**2) * f(x(z))
    return a   

N = 10
a = 0.0
b = 0.99
h = (b-a)/N
s = 0.5*integrand(a) + 0.5*integrand(b)
for k in range(10,N):
    s += f(a+k*h)
print(h*s)