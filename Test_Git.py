import sys
import numpy as np
import math
import cmath
import scipy
import random
from matplotlib import pyplot as plt
import matplotlib.animation

def grid(n):

    grid = np.zeros((n,n))

def array(grid,n):

    grid = np.random.choice(a=(0,1), size = (n,n), p = (0.5,0.5))
    return(grid)

def glide(grid,n):

    glide = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

    return(glide)

def anime(data, iterations):
    #data is 3D numpy array
    def update(i):
        screendata = data[i]
        matrix.set_array(screendata)
    screendata = data[0]
    fig, ax = plt.subplots()
    matrix = ax.matshow(screendata, cmap = 'magma')
    ani = matplotlib.animation.FuncAnimation(fig,update,frames=iterations,interval=100)
    plt.show()

def GoL(sweep, SpinArray, n):

    newspin = np.copy(SpinArray)

    for i in range(n):
        for j in range(n):
            sum = ((SpinArray[i, (j-1)] + SpinArray[i, (j+1)%n] + SpinArray[(i-1), j] + SpinArray[(i+1)%n, j] + SpinArray[(i-1), (j-1)] + SpinArray[(i-1), (j+1)%n] +  SpinArray[(i+1)%n, (j-1)] + SpinArray[(i+1)%n, (j+1)%n]))

            if SpinArray[i, j]  == 1:
                if (sum < 2) or (sum > 3):
                    newspin[i, j] = 0
                elif sum == 2 or sum == 3:
                    newspin[i,j] = 1

            elif SpinArray[i, j] == 0:
                if sum == 3:
                    newspin[i, j] = 1
                elif sum != 3:
                    newspin[i, j] = 0


    return(newspin)

def main():

    sweep = 10000
    n = 100

    g = grid(n)
    emptar = np.zeros((sweep,n,n))

    SpinArray = array(grid,n)

    for i in range(sweep):

        emptar[i] = GoL(sweep, SpinArray, n)

        SpinArray = emptar[i]

    anime(emptar, sweep)

main()
