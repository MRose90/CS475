# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:03:42 2016

@author: Michael
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    data = np.genfromtxt("1.csv", delimiter=',', dtype=np.float)
    fix11 = []
    fix12 = []
    fix14 = []
    fix21 = []
    fix22 = []
    fix24 = []
    p2Vals = []
    x = []
    for row in data:
        if row[0] == 1:
            fix11.append(row[2])
            x.append(row[1])
        if row[0] == 2:
            fix12.append(row[2])
        if row[0] == 4:
            fix14.append(row[2])
    data = np.genfromtxt("2.csv", delimiter=',', dtype=np.float)        
    for row in data:
        p2Vals.append(row[1])
    for i in range(0,17):
        fix21.append(p2Vals[0])
        fix22.append(p2Vals[1])
        fix24.append(p2Vals[2])
    plt.plot(x,fix11,'r')
    plt.plot(x,fix12,'g')
    plt.plot(x,fix14,'b')
    plt.plot(x,fix21,'c')
    plt.plot(x,fix22,'m')
    plt.plot(x,fix24,'y')
    plt.ylabel("Million Additions/Sec")
    plt.xlabel("Padding")
    l = []
    l.append(mpatches.Patch(color='r',label='Fix 1 - 1 Thread'))
    l.append(mpatches.Patch(color='g',label='Fix 1 - 2 Thread'))
    l.append(mpatches.Patch(color='b',label='Fix 1 - 4 Thread'))
    l.append(mpatches.Patch(color='c',label='Fix 2 - 1 Thread'))
    l.append(mpatches.Patch(color='m',label='Fix 2 - 2 Thread'))
    l.append(mpatches.Patch(color='y',label='Fix 2 - 4 Thread'))
    plt.savefig("plot1.png")
    plt.legend(handles=l)
    plt.savefig("plot2.png")
    plt.clf()
    plt.legend(handles=l)
    plt.savefig("plot3.png")
    
    

if __name__ == '__main__':
    main()
    exit(0)