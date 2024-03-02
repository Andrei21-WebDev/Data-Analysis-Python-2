import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage

class cluster():
    def __init__(self, t, variabile, metoda="complete"):
        self.x = t[variabile].values
        self.h = linkage(self.x, method=metoda)

    def calcul_partitie(self, i=None):
        jonctiuni = self.h.shape[0]
        n = jonctiuni + 1
        if i is None:
            i_max = np.argmax(self.h[1:, 2] - self.h[:(jonctiuni - 1), 2])
            i = jonctiuni - i_max
        else:
            i_max = jonctiuni - i
        self.i = i
        self.threshold = (self.h[i_max, 2] + self.h[i_max + 1, 2]) / 2
        c = np.arange(n)
        for j in range(jonctiuni-i+1):
            i1 = self.h[j, 0]
            i2 = self.h[j, 1]
            c[c==i1] = n+j
            c[c==i2] = n+j
        coduri = pd.Categorical(c).codes
        return np.array(["c"+str(i+1) for i in coduri])