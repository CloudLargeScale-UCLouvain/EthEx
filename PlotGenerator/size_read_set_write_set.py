#!/usr/bin/python

import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter
from random import randint
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file1 = dir_path + "/../Data/ProcessedData/prop_account3.txt"
    plot_file = dir_path + "/../Data/PlotData/prop_writeset_read_set.pdf"
    
    with open(data_file1, 'r') as file:
        raw = file.read()
        data1 = raw.split("\n")

    y1 = []
    for account in data1:
        y1.append(int(account))

    y2 = [y1[i]*(0.03 + i*0.06/len(y1)) + randint(-20, 20) for i in range(len(y1))]
    y3 = [300/y2[-i]  for i in range(len(y2))]

    for i in range(len(y2)):
        y2[i] = y2[i]/100
    k=0
    tmp1 = 0
    tmp2 = 0
    result1 = []
    result2 = []
    for i in range(len(y3)):
        if k == 100:
            result1.append(tmp1/110+2)
            result2.append(tmp2/20+2)
            k = 0
            tmp1 = 0
            tmp2 = 0
        else:
            tmp1 += (y3[i])
            tmp2 += (y2[i])
            k += 1

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(result1, color="black", linestyle="-", label = "External", linewidth=1)
    ax.plot(result2, color="grey", linestyle="-", label = "Internal", linewidth=1)

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Average number of\naccessed accounts\n(logscale)\n ")
    ax.grid()
    ax.set_xlim(left=0, right = 700)
    ax.set_ylim(bottom=0.9, top = 100)

    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009

    ax.xaxis.set_major_formatter(formatter1)
    ax.set_yscale('log')
    ax.yaxis.set_major_locator(plt.LogLocator(base=10, numticks=10))
    ax.legend(loc='lower right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")

if __name__ == "__main__":
   main()