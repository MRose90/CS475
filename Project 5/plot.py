# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:03:42 2016

@author: Michael
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def speedup(inp, output,output2):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    minMul = 0
    minMulC = 0
    minMulSIMD = 0
    minMulSpeedup = 500
    maxMul = 0
    maxMulC = 0
    maxMulSIMD = 0
    maxMulSpeedup = 0
    minSum = 0
    minSumC = 0
    minSumSIMD = 0
    minSumSpeedup = 500
    maxSum = 0
    maxSumC = 0
    maxSumSIMD = 0
    maxSumSpeedup = 0
    MulSpeedup = []
    SumSpeedup = []
    x = [];
    for row in data:
        if row[1]/row[3] > maxMulSpeedup:
            maxMul = row[0]
            maxMulSpeedup = row[1]/row[3]
            maxMulC = row[3]
            maxMulSIMD = row[1]
        if row[1]/row[3] < minMulSpeedup:
            minMul = row[0]
            minMulSpeedup = row[1]/row[3]
            minMulC = row[3]
            minMulSIMD = row[1]
        if row[2]/row[4] > maxSumSpeedup:
            maxSum = row[0]
            maxSumSpeedup = row[2]/row[4]
            maxSumC = row[4]
            maxSumSIMD = row[2]
        if row[2]/row[4] < minSumSpeedup:
            minSum = row[0]
            minSumC = row[4]
            minSumSIMD = row[2]
            minSumSpeedup = row[2]/row[4]
        MulSpeedup.append(row[1]/row[3])
        SumSpeedup.append(row[2]/row[4])
        x.append(row[0])
    plt.plot(x,MulSpeedup,'b')
    plt.plot(x,SumSpeedup,'g')
    plt.ylabel("Speedup")
    plt.xlabel("Array Size")
    l = []
    l.append(mpatches.Patch(color='b',label='Multiplication Speedup'))
    l.append(mpatches.Patch(color='g',label='Reduction Speedup'))
    plt.savefig(output)
    plt.clf()
    plt.legend(handles=l)
    plt.savefig(output2)
    plt.clf()
    print("Min Multiplication Speedup: ", minMul, " ",minMulC," ",minMulSIMD," ",minMulSpeedup)
    print("Max Multiplication Speedup: ", maxMul, " ",maxMulC," ",maxMulSIMD," ",maxMulSpeedup)
    print("Min Redux Speedup: ", minSum, " ",minSumC," ",minSumSIMD," ",minSumSpeedup)
    print("Max Redux Speedup: ", maxSum, " ",maxSumC," ",maxSumSIMD," ",maxSumSpeedup)    
    print("Average Multiplication Speedup: " , np.average(MulSpeedup))
    print("Average Redux Speedup: " , np.average(SumSpeedup))
    #copy for CSV if needed
    print(",Size,Non-SIMD,SIMD,Speedup")
    print("Smallest Multiplication Speedup,", minMul, ",",minMulC,",",minMulSIMD,",",minMulSpeedup)
    print("Largest Multiplication Speedup,", maxMul, ",",maxMulC,",",maxMulSIMD,",",maxMulSpeedup)
    print("Smallest Reduction Speedup,", minSum, ",",minSumC,",",minSumSIMD,",",minSumSpeedup)
    print("Largest Reduction Speedup,", maxSum, ",",maxSumC,",",maxSumSIMD,",",maxSumSpeedup) 

def graph(inp, output,output2):
    data = np.genfromtxt(inp, delimiter=',', dtype=np.float)
    sumSIMDMulSum = []
    sumMul = []
    sumSIMDMul = []
    sumMulSum = []
    x = [];
    for row in data:
        sumSIMDMul.append(row[1])
        sumSIMDMulSum.append(row[2])
        sumMul.append(row[3])
        sumMulSum.append(row[4])
        x.append(row[0])
    plt.plot(x,sumSIMDMul,'b')
    plt.plot(x,sumSIMDMulSum,'g')
    plt.plot(x,sumMul,'r')
    plt.plot(x,sumMulSum,'c')
    plt.ylabel("Million Multiplications Per Second")
    plt.xlabel("Array Size")
    l = []
    l.append(mpatches.Patch(color='b',label='SIMD SSE Array Mult'))
    l.append(mpatches.Patch(color='g',label='SIMD SSE Array Mult And Redux'))
    l.append(mpatches.Patch(color='r',label='Array Mult'))
    l.append(mpatches.Patch(color='c',label='Array Mult And Redux'))  
    plt.savefig(output)
    plt.clf()
    plt.legend(handles=l)
    plt.savefig(output2)
    plt.clf()

def main():
    graph("1.csv","plot.png","leg.png")
    speedup("1.csv","plot2.png","leg2.png")
    

if __name__ == '__main__':
    main()
    exit(0)