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

    grid = np.random.choice(a=(0,1), size = (n,n), p = (0.7,0.3))

    return(grid)

def glide(grid,n):

    grid = np.zeros((n,n))

    for i in range(3):
        if i == 0:
            grid[i,0] = 0
            grid[i,1] = 0
            grid[i,2] = 1
        elif i == 1:
            grid[i,0] = 1
            grid[i,1] = 0
            grid[i,2] = 1
        elif i == 2:
            grid[i,0] = 0
            grid[i,1] = 1
            grid[i,2] = 1
    print(grid)

    return(grid)

def anime(data, iterations):
    #data is 3D numpy array
    def update(i):
        screendata = data[i]
        matrix.set_array(screendata)
    screendata = data[0]
    fig, ax = plt.subplots()
    matrix = ax.matshow(screendata, cmap = 'magma')
    ani = matplotlib.animation.FuncAnimation(fig,update,frames=iterations,interval=2)
    plt.show()

def plot(x, y):

    plt.plot(x, y)
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

def com(grid, n):
    x = np.array([0,0])
    for i in range(n):
        for j in range(n):
            if grid[i,j] == 1:
                x += [i,j]
    #print(x)
    return(x/np.sum(grid))

def main():

    sweep = 100
    n = 1000
    x = []
    y = []
    t = []
    g = grid(n)
    emptar = np.zeros((sweep,n,n))

    SpinArray = glide(grid,n)

    for i in range(sweep):

        emptar[i] = GoL(sweep, SpinArray, n)
        r = com(SpinArray, n)
        x.append(r[0])
        y.append(r[1])
        t.append(i)
        SpinArray = emptar[i]

    anime(emptar, sweep)
    plot(t, y)
main()
