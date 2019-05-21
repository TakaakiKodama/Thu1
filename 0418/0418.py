#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:34:00 2019

@author: takaakikodama
"""
import matplotlib.pyplot as plt

def dologistic_growth(k, r, n0, t):
    nt = n0
    dataX=[]
    dataY=[]
    dataX.append(0)
    dataY.append(nt)
    for i in range(t):
        nt= nt+r*nt*(1.0-nt/k)
        dataX.append(i+1)
        dataY.append(nt)  
    plt.xlabel("Time t")
    plt.ylabel("population size Nt")
    plt.plot(dataX,dataY, label="r = "+str(r))

n=10
step=3/n
for r in range(n+1):
    dologistic_growth(100.0, r*step, 1.0, 20)
plt.legend()

plt.savefig('../デスクトップ/Thu1/prep.png', dpi=300)
plt.show()

ptn=[0.6,1.8,2.7]
for r in ptn:
    dologistic_growth(100.0, r, 1.0, 20)
plt.legend()

plt.savefig('../デスクトップ/Thu1/hw1.png', dpi=300)
plt.show()