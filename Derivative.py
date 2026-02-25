import matplotlib.pyplot as plt
import numpy as np
x = 1
N = -15

def x_plus_delta(x, delta):
    r = x+delta
    return r

def f(x):
    y = x*(x-1)
    return y

print(f(x))
delta_vals = []
for N in range (-2, -16, -2):
    delta = 10**N
    #The line below this one prints the derivative of the function x(x-1)
    print((f(x_plus_delta(x, delta)) - f(x))/delta)
    delta_vals.append(delta)
print(delta_vals)
print(delta)
plt.plot(delta_vals, (f(x_plus_delta(x, np.array(delta_vals))) - f(x))/np.array(delta_vals))
plt.show()

#My program is off by a few decimals as opposed to the analytical 
#derivative

#store the errors in a list, plot the errors from an array. error =
#1 - delta f(x)

derivative_error = 1 - f(x_plus_delta(x, np.array(delta_vals)) - f(x))/np.array(delta_vals)
plt.plot(delta_vals, np.abs(derivative_error))
plt.xscale("log")
plt.yscale("log")
plt.show()
