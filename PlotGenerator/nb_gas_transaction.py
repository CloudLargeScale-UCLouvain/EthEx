#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file2 = dir_path + "/../Data/ProcessedData/nb_gas_transaction2.txt"
    data_file1 = dir_path + "/../Data/ProcessedData/nb_gas_transaction.txt"
    plot_file = dir_path + "/../Data/PlotData/nb_gas_transaction.pdf"
    
    with open(data_file1, 'r') as file:
        raw = file.read()
        data = raw.split("\n")
        nb_gas1 = []
        i = 0
        k = 0
        tmp = 0
        for x in data:
            if k == 100:
                k = 0
                nb_gas1.append(tmp/100)
                tmp = 0
            if i <= 70000:
                tmp += float(x)
                k += 1
                i += 1
        nb_gas1.append(tmp/100)
    with open(data_file2, 'r') as file:
        raw = file.read()
        data = raw.split("\n")
        nb_gas2 = []
        i = 0
        k = 0
        tmp = 0
        for x in data:
            if k == 100:
                k = 0
                nb_gas2.append(tmp/100)
                tmp = 0
            if i <= 70000:
                tmp +=float(x)
                k += 1
                i += 1
        nb_gas2.append(tmp/100)       


    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(nb_gas1, color="black", linestyle="-", label = "External")
    ax.plot(nb_gas2, color="gray", linestyle="-", label = "Internal")
    
    ax.legend(loc='upper right', prop={'size': 6})

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Gas\n(logscale)")
    
    ax.grid()
    ax.set_xlim(left=0, right = 700)
    ax.set_ylim(bottom=10000, top = 1_000_000)
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    ax.set_yscale('log')
    ax.yaxis.set_major_locator(plt.LogLocator(base=10, numticks=5))
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='upper right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")

if __name__ == "__main__":
   main()