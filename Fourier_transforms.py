import numpy as np
import matplotlib.pyplot as plt


#The square wave function
x = np.linspace(0.1,20,1000)
total_wave = np.zeros_like(x)

for i in np.arange(1,30,2):
        square_wave_function = (1/(i))*np.sin(i*x)
        total_wave += square_wave_function
        

plt.plot(x, (4*np.pi)*total_wave)
plt.show()

#Sawtooth wave function
a = 1
f = 2
k = 1
t = np.linspace(0.1,20,1000)
sawtooth_wave_function = np.zeros_like(t)
for r in range(1,1000):
    sawtooth_wave_function += -(2*a)/np.pi * (-1)**k*(np.sin(2*np.pi*k*f*t)) * (1/k)

plt.plot(t, sawtooth_wave_function)
plt.show()

#Modulated sine wave
N = 1000
n = np.linspace(0.1, 20, 1000)
y_sub_n = np.zeros_like(n)

for p in range(1,1000):
      y_sub_n += np.sin((np.pi*n)/N) * np.sin(20*np.pi*n/N)

plt.plot(n, y_sub_n)
plt.show()
