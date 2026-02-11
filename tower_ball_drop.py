import sys

h = float(sys.argv[0])
g = float(sys.argv[1])
t = (2*h/g)**0.5
print(t)

def tower_ball_drop(h,g):
    return t == float(sys.argv[(2*h/g)**0.5])
t == tower_ball_drop(10, 9.8)