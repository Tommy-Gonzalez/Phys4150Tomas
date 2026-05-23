import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt
from numpy import arange
from random import random

#Variable declarations
theta = 30 * np.pi/180
N = 1000
h = 0.0001
x_velocity = 100*u.m *(1/u.s) * np.cos(theta)#X component velocity
y_velocity = 100*u.m *(1/u.s) * np.sin(theta)#Y component velocity
x = 0 * u.m * np.cos(theta)
y = 0 * u.m * np.sin(theta)
m = 1*u.kg #mass
R = 8*u.cm#Sphere's radius
R = R.to(u.m)
rho = 1.22*u.kg * u.m**-3 #Density of air
C = 0.47 #Drag coefficient
#F = (1/2)*np.pi*R*2 *rho*C*v**2 #Equation
g = 9.81 *u.m *(1/u.s**2) #gravity component
x_velocity = 100*u.m *(1/u.s) #X component velocity
y_velocity = 100*u.m *(1/u.s) #Y component velocity


origin = [x,y] #location of the cannon in x and y coordinates
all_variables = np.array([x,y,x_velocity,y_velocity])


def ddt(all_variables,t):
    dx = x_velocity
    dy = y_velocity
    dvx = -((np.pi * R**2) * rho *C)/(2*m) * x_velocity * np.sqrt((x_velocity)**2 + (y_velocity)**2)
    dvy = -g-((np.pi*R**2) * rho*C)/(2*m) * y_velocity *np.sqrt((x_velocity)**2+(y_velocity)**2)
    
    return np.array(ddx, ddy, x_acceleration,y_acceleration)

Final_Kutta = np.array([])
t = np.array([])
times = 
new_t = []

#Runge Kutta Method
def Runga(all_variables,t):
    for i in range (N):
        t = times[i]

        K1 = h * (ddt(all_variables,t)) #K1
        K2 = h * (ddt(all_variables + (1/2)*K1,t + (1/2)*h))
        K3 = h * (ddt(all_variables + (1/2)*K2,t + (1/2)*h))
        K4 = h * (ddt(all_variables + K3, t + h))

        Final_Kutta = all_variables(t) + (1/6)*(K1 + 2*K2 + 2*K3 +K4)
        new_t = t.copy()
        Final_Kutta.append([])
        return new_t

    

plt.scatter(Final_Kutta, new_t)
plt.show()
