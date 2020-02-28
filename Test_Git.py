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

def SIRSarray(grid,n):

    grid = np.random.choice(a=(-1,0,1), size = (n,n), p = (1/3, 1/3, 1/3))

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
    print("Look at this glidey wee man : ")
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
    ani = matplotlib.animation.FuncAnimation(fig,update,frames=iterations,interval=30)
    plt.show()

def plot(x, y):

    plt.plot(x, y)
    plt.show()

def trial(p1):

    heads = 0

    if random.uniform(0,1) <= p1:
        heads += 1

    return(heads)

def histo(a):

    plt.hist(a, bins = 'auto')
    plt.title("Histogram")
    plt.show()

    return()

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

def SIRS(sweep, SpinArray, p1, p2, p3, n):

    #print(str(h1) + " and" + str(h2) + " and" + str(h3))

    for l in range(n*n):

        #sum = SpinArray[i, (j-1)] + SpinArray[i, (j+1)%n] + SpinArray[(i-1), j] + SpinArray[(i+1)%n, j]

        i = random.choice(list(range(0, n)))
        j = random.choice(list(range(0, n)))


        if SpinArray[i, j] == 0:
            if SpinArray[i, (j-1)%n] == 1 or SpinArray[i, (j+1)%n] == 1 or SpinArray[(i-1)%n, j] == 1 or SpinArray[(i+1)%n, j] == 1:
                if trial(p1) == 1:
                    SpinArray[i, j] = 1


        elif SpinArray[i, j] == 1:
            if trial(p2) == 1:
                SpinArray[i, j] = -1


        elif SpinArray[i, j] == -1:
            if trial(p3) == 1:
                SpinArray[i, j] = 0


    return(SpinArray)

def com(grid, n):
    x = np.array([0,0])
    for i in range(n):
        for j in range(n):
            if grid[i,j] == 1:
                x += [i,j]
    #print(x)
    return(x/np.sum(grid))

def main():
    if len(sys.argv)!=4:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " 'gol', 'golglide' or 'sir' " + "temperature" + "system_size")
        quit()

    else:
        dynamic = (sys.argv[1])
        sweep = int(sys.argv[2])
        n = int(sys.argv[3])


    x = []
    y = []
    t = []

    p1 = 0.5
    p2 = 0.5
    p3 = 0.5

    g = grid(n)

    emptar = np.zeros((sweep,n,n))
    sum = np.zeros((sweep))


    if dynamic == 'gol':
        SpinArray = array(grid,n)
        for i in range(sweep):

            emptar[i] = GoL(sweep, SpinArray, n)

            SpinArray = emptar[i]

            #animate!
            plt.cla()
            im=plt.imshow(SpinArray, animated=True)
            plt.draw()
            plt.pause(0.0001)

        plt.close()

    if dynamic == 'golglide':

        SpinArray = glide(grid,n)

        for i in range(sweep):

            emptar[i] = GoL(sweep, SpinArray, n)

            #centre of mass calculations
            r = com(SpinArray, n)
            x.append(r[0])
            #y.append(r[1])
            t.append(i)

            SpinArray = emptar[i]

            #animate!

        anime(emptar, sweep)
        plt.close()

        #plot displacement vs time for glider
        plot(t, x)

    if dynamic == 'CountDooku':

        time_list = np.zeros(100)
        print(time_list)

        for j in range(100):
            emptar = np.zeros((n,n))
            SpinArray = array(grid,n)
            t = 0
            c = 0
            i = 0

            while t == 0:

                s2 = np.sum(SpinArray)
                emptar = GoL(sweep, SpinArray, n)
                s1 = np.sum(emptar)

                i += 1

                if s2 == s1:
                    c += 1
                else:
                    c = 0

                if c == 5:
                    t = i

                SpinArray = emptar

            time_list[j] = t
        print(time_list)

        histo(time_list)

    if dynamic == 'sir':

        SpinArray = SIRSarray(grid, n)

        for i in range(sweep):

            emptar[i] = SIRS(sweep, SpinArray, p1, p2, p3, n)

            SpinArray = emptar[i]

            #animate!

            plt.cla()
            im=plt.imshow(SpinArray, animated=True)
            plt.draw()
            plt.pause(0.0001)

        plt.close()










    """    for i in range(sweep):

        #emptar[i] = SIRS(sweep, SpinArray, p1, p2, p3, n)

        emptar[i] = GoL(sweep, SpinArray, n)

        #centre of mass calculations
        #r = com(SpinArray, n)
        #x.append(r[0])
        #y.append(r[1])
        #t.append(i)

        SpinArray = emptar[i]

        #animate!

        plt.cla()
        im=plt.imshow(SpinArray, animated=True)
        plt.draw()
        plt.pause(0.0001)

    plt.close()

    histo(sum, sweep)
    #plot displacement vs time for glider
    #plot(t, x)"""
main()
