import numpy as np
import matplotlib.pyplot as plt
import argparse
############
parser = argparse.ArgumentParser(description = "Polar plot")
parser.add_argument('r',type = int, help = 'r component')
theta = np.linspace(0, 10*np.pi, args.Number_of_points)
r = theta**2
args=parser.parse_args()
parser.add_argument('theta', type = int, help = 'theta component')
parser.add_argument('Number_of_points', type = float, help = 'This is the upper limit')
x = r*np.cos(theta)
y = r*np.sin(theta)


plt.plot(r, theta = args.Number_of_points)
plt.show()