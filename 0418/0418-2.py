#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:30:56 2019

@author: takaakikodama
"""

import matplotlib.pyplot as plt
import numpy as np

def dologistic_growth(k, r, n0, t):
    nt = n0
    dataY=[]
    dataY.append(nt)
    for i in range(t):
        nt= nt+r*nt*(1.0-nt/k)
        dataY.append(nt)
    return(dataY)
dataX=np.empty(0)
dataY=np.empty(0)
for r in np.arange(1,3.01,0.01):
    difX=np.ones(50)*r
    res=dologistic_growth(100.0, r, 1.0, 300)
    difY=res[251:301]
    dataX=np.hstack([dataX,difX])
    dataY=np.hstack([dataY,difY])
plt.plot(dataX,dataY, ".")
plt.xlabel("Value r")
plt.ylabel("Convergence values Nt")
#plt.plot(dataX,dataY, label="r = "+str(r))
plt.savefig('../デスクトップ/Thu1/hw2.png', dpi=300)
plt.show()