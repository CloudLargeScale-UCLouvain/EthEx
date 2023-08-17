#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter
import statistics
from random import randint
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file1 = dir_path + "/../Data/ProcessedData/prop_account_EOA.txt"
    plot_file = dir_path + "/../Data/PlotData/prop_account_active.pdf"
    data_file2 = dir_path + "/../Data/ProcessedData/prop_account_SCA.txt"
    
    with open(data_file1, 'r') as file:
        raw = file.read()
        data1 = raw.split("\n")

    y1 = []
    for account in data1:
        y1.append(int(account))

    with open(data_file2, 'r') as file:
        raw = file.read()
        data2 = raw.split("\n")

    y2 = []
    for account in data2:
        y2.append(int(account))
    
    result1 = []
    result2 = []
    k = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(len(y2)):
        if k == 100:
            k = 0
            result1.append(tmp1)
            result2.append(tmp2)
            tmp1 = 0
            tmp2 =0
        k+=1
        tmp1 += y1[i]
        tmp2 += y2[i]
    result1.append(tmp1 - tmp2)
    result2.append(tmp2)

    print("SCA", sum(result2))
    print("EOA", sum(result1))
    x = [k for k in range(len(result1))]    
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(x,result1, color="grey", linestyle="-", label = "EOA", linewidth=1)
    ax.plot(x,result2, color="black", linestyle="-", label = "SCA", linewidth=1)
    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Active accounts\n(logscale)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)

    ax.set_yscale('log')
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='lower left', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")

if __name__ == "__main__":
   main()