# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:03:42 2016

@author: Michael
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    data = np.genfromtxt("tst.csv", delimiter=',', dtype=np.float)
    Thread1 = []
    Thread2 = []
    Thread3 = []
    Thread4 = []
    Thread8 = []
    Thread16 = [] 
    x = []
    for row in data:
        if row[0] == 1:
            Thread1.append(row[3])
            x.append(row[1])
        if row[0] == 2:
            Thread2.append(row[3])
        if row[0] == 3:
            Thread3.append(row[3])
        if row[0] == 4:
            Thread4.append(row[3])
        if row[0] == 8:
            Thread8.append(row[3])
        if row[0] == 16:
            Thread16.append(row[3])
    plt.plot(x,Thread1,'r')
    plt.plot(x,Thread2,'g')
    plt.plot(x,Thread3,'b')
    plt.plot(x,Thread4,'c')
    plt.plot(x,Thread8,'m')
    plt.plot(x,Thread16,'y')
    plt.ylabel("Millions of Volume Calculations/Sec")
    plt.xlabel("NUMS")
    l = []
    l.append(mpatches.Patch(color='r',label='1 Thread'))
    l.append(mpatches.Patch(color='g',label='2 Threads'))
    l.append(mpatches.Patch(color='b',label='3 Threads'))
    l.append(mpatches.Patch(color='c',label='4 Threads'))
    l.append(mpatches.Patch(color='m',label='8 Threads'))
    l.append(mpatches.Patch(color='y',label='16 Threads'))
    plt.legend(handles=l)
    plt.show() 

    plt.clf()
    plt.ylabel("Millions of Volume Calculations/Sec")
    plt.xlabel("NUMS")
    Thread1 = []
    Thread2 = []
    Thread3 = []
    Thread4 = []
    Thread8 = []
    Thread16 = [] 
    x = []
    for row in data:
        if row[1]<100:
            if row[0] == 1:
                Thread1.append(row[3])
                x.append(row[1])
            if row[0] == 2:
                Thread2.append(row[3])
            if row[0] == 3:
                Thread3.append(row[3])
            if row[0] == 4:
                Thread4.append(row[3])
            if row[0] == 8:
                Thread8.append(row[3])
            if row[0] == 16:
                Thread16.append(row[3])
    plt.plot(x,Thread1,'r',label="1 Thread")
    plt.plot(x,Thread2,'g',label="2 Threads")
    plt.plot(x,Thread3,'b',label="3 Threads")
    plt.plot(x,Thread4,'c',label="4 Threads")
    plt.plot(x,Thread8,'m',label="8 Threads")
    plt.plot(x,Thread16,'y',label="16 Threads")
    
    plt.show()       

if __name__ == '__main__':
    main()
    exit(0)