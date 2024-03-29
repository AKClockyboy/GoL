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

    return(grid)

def array(grid,n):

    grid = np.random.choice(a=(0,1), size = (n,n), p = (0.5,0.5))

    return(grid)

def SIRSarray(grid,n):

    grid = np.random.choice(a=(-1,0,1), size = (n,n), p = (1/3, 1/3, 1/3))

    return(grid)

def bootstrap():

    yerror = []

    for i in range(len(self.temps)):
        fakecap = []
        fakeenergy = np.zeros([100,1000])
        for j in range(100):
            fakeenergy[j] = sklearn.utils.resample(enr[i],n_samples=1000)
            emean = np.mean(fakeenergy[j])
            N = self.length**2
            T2 = self.temps[i]**2
            esq = np.square(fakeenergy[j])
            emeansq = np.square(emean)
            esqmean = np.mean(esq)
            ccc = (1.0/(N*T2))*(esqmean-emeansq)
            fakecap.append(ccc)
        oof = (np.square(np.mean(fakecap)))
        ouch = (np.mean(np.square(fakecap)))
        yerror.append((np.sqrt(ouch-oof)))
    return()

def SIRSarray_with_imun(grid, n, f):

    grid = np.random.choice(a=(-1,0,1,2), size = (n,n), p = (((1 - f)/3), ((1 - f)/3), ((1 - f)/3), f))

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
    return()

def trial(p1):

    heads = 0

    if random.uniform(0,1) < p1:
        heads += 1

    return(heads)

def histo(a):

    plt.hist(a, bins = 15)
    plt.title("Histogram")
    plt.show()

    return()

def convertion(SpinArray, n):

    immo_no = 0

    for i in range(n):
        for j in range(n):
            if SpinArray[i, j] == 1:
                immo_no += 1

    x = immo_no

    return(immo_no)

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
            printAAARAYreturn(newspin)

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

def SIRSinf(sweep, SpinArray, p1, p2, p3, n, inf):

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
    return(x/np.sum(grid))

def main():

    if len(sys.argv)!=7:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " 'gol', 'golglide', 'CountDooku', 'sir' " + "sweep" + " system_size" + " p1" + " p2" + " p3")
        quit()

    else:
        dynamic = (sys.argv[1])
        sweep = int(sys.argv[2])
        n = int(sys.argv[3])
        p1 = float(sys.argv[4])
        p2 = float(sys.argv[5])
        p3 = float(sys.argv[6])

    g = grid(n)

    emptar = np.zeros((sweep,n,n))

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

        x = []
        y = []
        t = []

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

    if dynamic == 'countdooku':

        time_list = np.zeros(100)

        print(time_list)

        for j in range(100):

            print(j)

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

                #if i > 1500:

                    #break

                if c == 10:

                    t = i

                    break

                SpinArray = emptar



            time_list[j] = t

            np.save('histogram_time', time_list)

        histo(time_list)

    if dynamic == 'sir':
        SpinArray = SIRSarray(grid, n)
        for i in range(sweep):
            emptar[i] = SIRS(sweep, SpinArray, p1, p2, p3, n)
            SpinArray = emptar[i]
        #animate!
        anime(emptar, sweep)
        plt.close()

    if dynamic == 'sirheat':

        SpinArray = SIRSarray(grid, n)

        s = np.zeros((21,21))
        print(s)

        p1 = 1.05

        I1 = 0
        for l in range(21):

            p1 -= 0.05

            p1 = round(p1, 4)

            p3 = -0.05

            for m in range(21):

                p3 += 0.05

                p3 = round(p3, 4)

                print("p1 is: " + str(p1) + " and p2 is : " + str(p3))

                SpinArray = SIRSarray(grid, n)
                I2 = []


                for i in range(sweep):

                    emptar[i] = SIRSinf(sweep, SpinArray, p1, p2, p3, n, I2)

                    SpinArray = emptar[i]

                    if i > 100:

                        I2.append(convertion(SpinArray, n))

                print("L is " + str(l) + " M is " + str(m))

                s[l, m] = (np.mean(I2))/(n*n)

        np.save('av_heatmap',s)

        plt.imshow(s, cmap='plasma', extent = (0, 1, 0, 1))
        plt.colorbar()
        plt.show()

    if dynamic == 'sirvar':

        SpinArray = SIRSarray(grid, n)

        s = np.zeros((21,21))
        print(s)

        p1 = 1.05

        I1 = 0
        for l in range(21):

            p1 -= 0.05
            p1 = round(p1, 3)
            p3 = -0.05

            for m in range(21):

                p3 += 0.05
                p3 = round(p3, 3)
                print("p1 is: " + str(p1) + " p2 is : " + str(p3))
                SpinArray = SIRSarray(grid, n)
                I2 = []


                for i in range(sweep):

                    emptar[i] = SIRSinf(sweep, SpinArray, p1, p2, p3, n, I2)

                    SpinArray = emptar[i]

                    if i > 100:

                        I2.append(convertion(SpinArray, n))

                s[l, m] = np.var(I2)/(n*n)

        np.save('var_heatmap', s)
        plt.imshow(s, cmap='plasma', extent = (0,1,0,1))
        plt.colorbar()
        plt.show()

    if dynamic == 'sirvar2':

        p3 = 0.5
        p2 = 0.5
        p1 = 0.2

        var_list = []
        p1_list = []

        for l in range(30):

            p1 += 0.01

            p1 = round(p1, 3)

            print("p1 is: " + str(p1))

            SpinArray = SIRSarray(grid, n)

            I2 = []

            p1_list.append(p1)

            for i in range(sweep):

                emptar[i] = SIRS(sweep, SpinArray, p1, p2, p3, n)
                SpinArray = emptar[i]

                if i > 100:

                    I2.append(np.mean(convertion(SpinArray, n)))

            var_list.append(np.var(I2)/(n*n))

        np.save('var_cutathome', var_list)
        np.save('p1athome', p1_list)

        plot(p1_list, var_list)

    if dynamic == 'FINALE':

        emptar = np.zeros((sweep,n,n))

        I1 = []

        f_list = []

        f = 0

        for l in range(100):

            f += 0.01
            f = round(f, 3)
            print(f)

            f_list.append(f)

            I2 = []

            for m in range(5):

                c = 0

                AAARAY = SIRSarray_with_imun(grid, n, f)
                #print(AAARAY)

                for i in range(sweep):

                    emptar[i] = SIRSinf(sweep, AAARAY, p1, p2, p3, n, I1)

                    AAARAY = np.array(emptar[i])

                    if i > 100:

                        I2.append(convertion(AAARAY, n))


            I1.append(np.mean(I2)/n*n)

            np.save('FINALEathome', I1)
            np.save('f_listathome', f_list)

        plot(f_list, I1)

main()
