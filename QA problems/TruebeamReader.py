# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:00:36 2022

@author: Hung Bui Tien
"""

import numpy as np
import matplotlib.pyplot as plt


simFile = open("FFF/r=0.11/T6C.mesh",'r')
simdat = simFile.readlines()

# read FFF simulation data
posSim = []
simData = []
for line in simdat[21:222]:
    tmp=line.split()
    posSim.append(float(tmp[0]))
    simData.append(float(tmp[1]))
    
posSim = np.array(posSim)
simData = np.array(simData)
simData = 100*simData/simData.max()

# read FFF experiment data
exFile = open("6FFF_Depth10_Size10.txt", 'r')
exdat = exFile.readlines()
exData = []

for line in exdat:
    tmp = line.split()
    exData.append(float(tmp[0]))

exData = np.array(exData)

# read FF simulation data
simFileFF = open("FF/T6f.mesh",'r')
simdatFF = simFileFF.readlines()

posSimFF = []
simDataFF = []
for line in simdatFF[21:222]:
    tmp=line.split()
    posSimFF.append(float(tmp[0]))
    simDataFF.append(float(tmp[1]))

posSimFF = np.array(posSimFF)
simDataFF = np.array(simDataFF)
simDataFF = 100*simDataFF/simDataFF.max()

# plotting
plt.plot(posSim, simData, label='FFF-Simulation')
# plt.plot(posSimFF, simDataFF, label='FF-Simulation')
plt.scatter(posSim,exData, marker='s', color='red', label='FFF-Experiment')
plt.xlabel('Position (cm)')
plt.ylabel('Relative dose (%)')
plt.legend()
plt.grid()
