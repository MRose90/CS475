# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:03:42 2016

@author: Michael
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    data = np.genfromtxt("DC.csv", delimiter=',', dtype=np.float)
    DC = []
    DF = []
    SC = []
    SF = []
    DC1 = []
    DF1 = []
    SC1 = []
    SF1 = []
    x = []
    for row in data:
            DC.append(row[1])
            DC1.append(row[2]/1000000)
            x.append(row[0])
    data = np.genfromtxt("DF.csv", delimiter=',', dtype=np.float)        
    for row in data:
            DF.append(row[1])
            DF1.append(row[2]/1000000)
    data = np.genfromtxt("SF.csv", delimiter=',', dtype=np.float)        
    for row in data:
            SF.append(row[1])
            SF1.append(row[2]/1000000)
    data = np.genfromtxt("SC.csv", delimiter=',', dtype=np.float)        
    for row in data:
            SC.append(row[1])
            SC1.append(row[2]/1000000)
    plt.plot(x,DC,'r')
    plt.plot(x,DF,'g')
    plt.plot(x,SC,'b')
    plt.plot(x,SF,'c')
    plt.ylabel("Steps/Sec")
    plt.xlabel("Threads")
    l = []
    l.append(mpatches.Patch(color='r',label='Dynamic Coarse'))
    l.append(mpatches.Patch(color='g',label='Dynamic Fine'))
    l.append(mpatches.Patch(color='b',label='Static Coarse'))
    l.append(mpatches.Patch(color='c',label='Static Fine'))
    plt.savefig("plot1.png")
    plt.clf()
    plt.legend(handles=l)
    plt.savefig("plot2.png")
    

if __name__ == '__main__':
    main()
    exit(0)