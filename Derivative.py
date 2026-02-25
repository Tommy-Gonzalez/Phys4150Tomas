import matplotlib.pyplot as plt
x = 1
N = -15

def x_plus_delta(x, delta):
    r = x+delta
    return r

def f(x):
    y = x*(x-1)
    return y

print(f(x))
    
for N in range (-2, -16, -2):
    delta = 10**-N
    print(f(x_plus_delta(x, delta)) - f(x)/delta)
    N+1

plt.plot(f(x_plus_delta(x, delta)) - f(x)/delta)
plt.show()