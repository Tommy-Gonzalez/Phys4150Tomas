import argparse
import numpy as np

def Spaceship_Travel(x, v, c):
    denominator_term = (v**2/c**2)
    gamma = 1/(np.sqrt(1 - denominator_term))
    length_contraction = x/ gamma
    return gamma, length_contraction

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Spaceship Travel')
    parser.add_argument('x', type = float, help = 'This is the amount of light years')
    parser.add_argument('v', type = float, help = 'This is the velocity')
    parser.add_argument('c', type = int, help = 'This is the speed of light')
    args = parser.parse_args()

    gamma, length_contracted = Spaceship_Travel(args.x, args.v, args.c)

    print("The length contracted is: ", length_contracted)
