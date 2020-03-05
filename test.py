import sys
import numpy as np
import math
import cmath
import scipy
import random
from matplotlib import pyplot as plt

import matplotlib.animation

data = np.load('av_inf_with_f.npy', 'r')
print(data)

### BOOTSTRAP
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
