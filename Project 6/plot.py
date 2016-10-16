# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:03:42 2016

@author: Michael
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def Local(inp, output,output2):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    Mult = []
    MultAdd = []
    x = []
    for row in data:
        Mult.append(row[2]*10)
        MultAdd.append(row[3]*10)
        x.append(row[1])
    plt.plot(x,Mult,'b')
    plt.plot(x,MultAdd,'g')
    plt.ylabel("GigaFlops")
    plt.xlabel("Local Size")
    l = []
    l.append(mpatches.Patch(color='b',label='Multiplication'))
    l.append(mpatches.Patch(color='g',label='Multiplication and Addition'))
    plt.xlim(8,512)    
    plt.savefig(output)
    plt.clf()
    plt.legend(handles=l)
    plt.savefig(output2)
    plt.clf()

def Global(inp, output,output2):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)

    Mult = []
    MultAdd = []
    x = []
    for row in data:
        Mult.append(row[2]*10)
        MultAdd.append(row[3]*10)
        x.append(row[0])
    plt.plot(x,Mult,'b')
    plt.plot(x,MultAdd,'g')
    plt.ylabel("GigaFlops")
    plt.xlabel("Global Size")
    l = []
    l.append(mpatches.Patch(color='b',label='Multiplication'))
    l.append(mpatches.Patch(color='g',label='Multiplication and Addition'))   
    plt.savefig(output)
    plt.clf()
    plt.legend(handles=l)
    plt.savefig(output2)
    plt.clf()
    
def Redux(inp, output,output2):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    redux = []
    x = []
    for row in data:
        redux.append(row[4])
        x.append(row[0])
    plt.plot(x,redux,'b')
    plt.ylabel("GigaFlops")
    plt.xlabel("Array Size")
    l = []
    l.append(mpatches.Patch(color='b',label='Reduction'))
    plt.savefig(output)
    plt.clf()
    plt.legend(handles=l)
    plt.savefig(output2)
    plt.clf()

def main():
    Redux("global.csv","plot.png","leg.png")
    Local("local.csv","plot2.png","leg2.png")
    Global("global.csv","plot3.png","leg3.png")

if __name__ == '__main__':
    main()
    exit(0)