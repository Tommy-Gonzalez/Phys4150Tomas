#Exercise 2.4
## A spaceship travels from Earth in a straight line 
## at relativistic speed v to another planet x light years away.
import argparse
import numpy as np
#Light years = x
#1 light year = 9460730472580800 meters
x = 9460730472580800
c =  (3*10**8)
v = 0.99*c
delta_t = float()
gamma = 1/(np.sqrt(v**2/c**2))

length_contraction = gamma / x
print("The length contraction of a spaceship")
print("given that the distance is 10 light years away")
print("(in meters = 9460730472580800) is: ", length_contraction)