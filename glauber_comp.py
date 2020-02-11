import numpy as np
import math
import cmath
import scipy
import sys
import random
from matplotlib import pyplot as plt
from random import seed
import matplotlib.animation
import csv
import time

# animated display
def anime(data,iterations):
    #data is 3D numpy array
    def update(i):
        screendata = data[i]
        matrix.set_array(screendata)
    screendata = data[0]
    fig, ax = plt.subplots()
    matrix = ax.matshow(screendata, cmap='magma')
    ani = matplotlib.animation.FuncAnimation(fig,update,frames=iterations,interval=100)
    plt.show()

def plotter():

    y,x = np.loadtxt('mag_data.txt', delimiter = ',', unpack=True)

    plt.plot(x,y, label='Magnetism vs Temperature')
    plt.xlabel('Temp')
    plt.ylabel('Magnetism')
    plt.title('Magnetism vs Temperature')
    plt.legend()
    plt.show()


    y,x = np.loadtxt('eng_data.txt', delimiter = ',', unpack=True)

    plt.plot(x,y, label='Energy vs Temperature')
    plt.xlabel('Temp')
    plt.ylabel('Energy')
    plt.title('Energy vs Temperature')
    plt.legend()
    plt.show()

    y,x = np.loadtxt('sus_data.txt', delimiter = ',', unpack=True)

    plt.plot(x,y, label='Susceptibility vs Temperature')
    plt.xlabel('Temp')
    plt.ylabel('Susceptibility ')
    plt.title('Susceptibility vs Temperature')
    plt.legend()
    plt.show()

    y,x = np.loadtxt('cap_data.txt', delimiter = ',', unpack=True)

    plt.plot(x,y, label='Heat Capacity vs Temperature')
    plt.xlabel('Temp')
    plt.ylabel('Heat Capacity')
    plt.title('Heat Capacity vs Temperature')
    plt.legend()
    plt.show()

def susceptability(mag, t):

    sus = (1/t)*(np.var(mag))

    return(sus)

def heatcap(e, t):

    cap = (1/(t*t))*(np.var(e))

    return(cap)

def magnitisation(SpinArray):

    mag = np.sum(SpinArray)

    return(mag)

def array(n):

    SpinArray = np.random.choice(a=(-1,1), size = (n,n), p = (0.5,0.5))

    return(SpinArray)

def eng(SpinSum, rho):

    DeltaE = 2*rho*SpinSum

    return(DeltaE)

def totaleng(n, SpinArray):
    tot = 0
    for i in range(n):
        for j in range(n):
            tot += -1*(SpinArray[i][j]*(SpinArray[(i+1)%n][j] + SpinArray[i][(j+1)%n]))
    return(tot)

def SpinSum(x,y,SpinArray,n):

    SpinSum = SpinArray[(x+1)%n][y] + SpinArray[(x-1)%n][y] + SpinArray[x][(y+1)%n] + SpinArray[x][(y-1)%n]

    return(SpinSum)

def trial(DeltaE, temperature):

    heads = 0

    if random.uniform(0,1) <= math.exp(-DeltaE/temperature):
        heads += 1

    return(heads)

def glauber(SpinArray, n, sweep, magnet, energy, temperature, sus):

    for i in range(n*n):

        x = random.choice(list(range(0, n)))
        y = random.choice(list(range(0, n)))


        rho = SpinArray[x][y] #particle being chosen at random

        DeltaE = eng(SpinSum(x,y,SpinArray,n), rho)


        if sweep > 100:
            if sweep%10 == 0:
                magnet.append(magnitisation(SpinArray))
                energy.append(totaleng(n, SpinArray))



        heads = trial(DeltaE, temperature)

        if DeltaE <= 0:
            rho = -1*rho
        else:
            if heads == 1:
                rho = -1*rho
            else:
                rho = rho

        SpinArray[x][y] = rho

    return(SpinArray)

def kawasaki(SpinArray, n, sweep, magnet, energy, temperature, sus):

    for i in range(n*n):

        x = random.choice(list(range(0, n)))
        y = random.choice(list(range(0, n)))

        a = random.choice(list(range(0, n)))
        b = random.choice(list(range(0, n)))

        while a==x and b==y:

            x = random.choice(list(range(0, n)))
            y = random.choice(list(range(0, n)))


        rho = SpinArray[x][y] #particle being chosen at random
        nu = SpinArray[a][b]

        if rho != nu:

            DeltaE = (eng(SpinSum(a,b,SpinArray,n), nu) + eng(SpinSum(x,y,SpinArray,n), rho))

            if sweep>100:
                if sweep%10 == 0:
                    magnet.append(magnitisation(SpinArray))
                    energy.append(totaleng(n, SpinArray))


            if (x-a == 1 and y-b == 0) or (x-a == 0 and y-b ==1):

                DeltaE += 2

            heads = trial(DeltaE,temperature)

            if DeltaE <= 0:
                rho = -1*rho
                nu = -1*nu
            else:
                if heads == 1:
                    rho = -1*rho
                    nu = -1*nu
                else:
                    rho = rho
                    nu = nu

            SpinArray[x][y] = rho


    return(SpinArray)

def main():

    # Read name of varibles from command line

    if len(sys.argv)!=4:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " 'g' or 'k' " + "temperature" + "system_size")
        quit()

    else:
        dynamic = (sys.argv[1])
        temperature = float(sys.argv[2])
        n = int(sys.argv[3])


    temperature_list = []
    average_magnet_list=[]
    average_energy_list = []
    average_sus_list = []
    average_cap_list = []


    f = open('mag_data.txt','w')
    g = open('eng_data.txt','w')
    h = open('sus_data.txt','w')
    k = open('cap_data.txt','w')


    for i in range(10):

        magnet = []
        energy = []
        sus = []
        cap = []


        SpinArray = array(n)

        sweep = 1000
        iterations = n*n
        emptar = np.zeros((sweep,n,n))

        if dynamic == 'g':
            for i in range(sweep):
                emptar[i] = glauber(SpinArray, n, sweep, magnet, energy, temperature, sus)

        else:
            for i in range(sweep):
                emptar[i] = kawasaki(SpinArray, n, sweep, magnet, energy, temperature, sus)




        average_magnet_list.append(abs(np.mean(magnet)))
        average_energy_list.append(np.mean(energy))
        sus.append(susceptability(magnet, temperature))
        cap.append(heatcap(energy, temperature))


        average_sus_list.append(np.mean(sus))
        average_cap_list.append(np.mean(cap))


        print("energy is: " + str(np.mean(energy)))
        print("magnetisation is: " + str(np.mean(magnet)))
        print("cap is: " + str(np.mean(cap)))


        temperature_list.append(temperature)

        temperature = temperature+0.2

        #anime(emptar, sweep)

    for a,b in zip(average_magnet_list,temperature_list):
        f.write("%s,%s\n" % (a,b))
    f.close()

    for c,d in zip(average_energy_list,temperature_list):
        g.write("%s,%s\n" % (c,d))
    g.close()

    for e,f in zip(average_sus_list,temperature_list):
        h.write("%s,%s\n" % (e,f))
    h.close()

    for n,m in zip(average_cap_list,temperature_list):
        k.write("%s,%s\n" % (n,m))
    k.close()


    plotter()


main()
