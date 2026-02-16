import numpy as np
import matplotlib.pyplot as plt
import argparse
############
parser = argparse.ArgumentParser(description = "Deltoid Curve")
parser.add_argument('color', type = str, help = 'This changes the color')
parser.add_argument('Number_of_points', type = int, help = 'This is the upper limit')
args=parser.parse_args()
theta = np.linspace(0, 2*np.pi, args.Number_of_points)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta) 
plt.plot(x,y, color = args.color)
plt.show()
