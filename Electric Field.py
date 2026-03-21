import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as const
import scipy.constants as const
from matplotlib.animation import PillowWriter

#Definition of q,r and square plane
q_1 = 1.0
q_2 = -1.0
#distance from q1 to q2 is 0.1M or 10 cm

#charge coordinates
charge1_x1 = 0.50
charge1_y1 = 0.50
charge2_x2 = 0.50
charge2_y2 = 0.60  
n = 100
potential = np.zeros((n,n))


#Create a loop
for i in range (n):
    for j in range (n):
            x = -0.5 + 1/n * i
            y = -0.5 + 1/n * j
            Point_p_x = x
            Point_p_y = y
            #Distance formula
            r1 = np.sqrt((charge1_x1 - Point_p_x)**2 + (charge1_y1 - Point_p_y)**2)
            r2 = np.sqrt((charge2_x2 - Point_p_x)**2 + (charge2_y2 - Point_p_y)**2)
            #Electric potential formula
            phi_1 = (q_1)/(4*np.pi * const.epsilon_0 * r1)
            phi_2 = (q_2)/(4*np.pi * const.epsilon_0 * r2)
            potential[i,j] = (phi_1 + phi_2)

#Show a 2d plot using contour plt.imshow
plt.imshow(potential, extent=[-0.5, 0.5, -0.5, 0.5])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric potential from 2 point charges')
plt.show()


###########Derivatives
#Derivative with respect to x and y

x = 1
N = -15
x_der = np.zeros((n-1,n-1))
y_der = np.zeros((n-1,n-1))
for i in range (n - 1):
    for j in range (n - 1):
            x_der[i,j] = (potential[i + 1, j] - potential[i,j]) / (1/n)
            y_der[i,j] = (potential[j + 1, j] - potential[i,j]) / (1/n)

Electric_field_x = -x_der
Electric_field_y = -y_der

np.meshgrid(Electric_field_x, Electric_field_y)
plt.quiver(potential[i,j], x_der[i,j], y_der[i,j])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quiver plot  of x and y partial derivatives')
plt.show()