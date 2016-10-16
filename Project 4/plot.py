# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:03:42 2016

@author: Michael
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def onlyPop(inp, output):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    temp = []
    prec = []
    grain = []
    deer = []
    vel = []
    x = []
    xCount = 0;
    for row in data:
        deer.append(row[0])
        vel.append(row[1])
        grain.append(row[2])
        temp.append(row[3])
        prec.append(row[4])
        x.append(xCount)
        xCount+= 1
    plt.plot(x,deer,'r')
    plt.plot(x,vel,'g')
    plt.ylabel("Values")
    plt.xlabel("Months Since Start of Simulation")
    l = []
    l.append(mpatches.Patch(color='r',label='Deer (Pop.)'))
    l.append(mpatches.Patch(color='g',label='Velociraptors (Pop.)'))
    plt.legend(handles=l)
    plt.savefig(output)
    plt.clf()

def graphNoGrain(inp, output):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    temp = []
    prec = []
    grain = []
    deer = []
    vel = []
    x = []
    xCount = 0;
    for row in data:
        deer.append(row[0])
        vel.append(row[1])
        grain.append(row[2])
        temp.append(row[3])
        prec.append(row[4])
        x.append(xCount)
        xCount+= 1
    plt.plot(x,deer,'r')
    plt.plot(x,vel,'g')
    plt.plot(x,temp,'c')
    plt.plot(x,prec,'m')
    plt.ylabel("Values")
    plt.xlabel("Months Since Start of Simulation")
    l = []
    l.append(mpatches.Patch(color='r',label='Deer (Pop.)'))
    l.append(mpatches.Patch(color='g',label='Velociraptors (Pop.)'))
    l.append(mpatches.Patch(color='c',label='Temperature (F)'))    
    l.append(mpatches.Patch(color='m',label='Precipitation (In)'))
    plt.legend(handles=l)
    plt.savefig(output)
    plt.clf()
    
def graph(inp, output):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    temp = []
    prec = []
    grain = []
    deer = []
    vel = []
    x = []
    xCount = 0;
    for row in data:
        deer.append(row[0])
        vel.append(row[1])
        grain.append(row[2])
        temp.append(row[3])
        prec.append(row[4])
        x.append(xCount)
        xCount+= 1
    plt.plot(x,deer,'r')
    plt.plot(x,vel,'g')
    plt.plot(x,grain,'b')
    plt.plot(x,temp,'c')
    plt.plot(x,prec,'m')
    plt.ylabel("Values")
    plt.xlabel("Months Since Start of Simulation")
    l = []
    l.append(mpatches.Patch(color='r',label='Deer (Pop.)'))
    l.append(mpatches.Patch(color='g',label='Velociraptors (Pop.)'))
    l.append(mpatches.Patch(color='b',label='Grain Height (In)'))
    l.append(mpatches.Patch(color='c',label='Temperature (F)'))    
    l.append(mpatches.Patch(color='m',label='Precipitation (In)'))
    plt.legend(handles=l)
    plt.savefig(output)
    plt.clf()

def main():
    graph("out.csv","6 years.png")
    graph("out2.csv","100 years.png")
    graphNoGrain("out2.csv","100y NoGrain.png")
    onlyPop("out2.csv","100y OnlyPop.png")
    

if __name__ == '__main__':
    main()
    exit(0)