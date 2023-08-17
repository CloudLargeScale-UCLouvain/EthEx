#!/usr/bin/python

import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/last_use.txt"
    plot_file = dir_path + "/../Data/PlotData/last_use.pdf"

    result1 = []
    result2 = []
    result3 = []
    result4 = []

    x = []
    with open(data_file, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            x.append(int(tmp[0]))
            result1.append(float(tmp[1]))
            result2.append(float(tmp[2]))
            result3.append(float(tmp[3]))
            result4.append(float(tmp[4]))

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(x,result4, color="red", linestyle="-", label = "Max", linewidth=1)
    ax.plot(x,result3, color="black", linestyle="-", label = "Q3", linewidth=1)
    ax.plot(x,result2, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,result1, color="lightgrey", linestyle="-", label = "Q1", linewidth=1)
    
    
    

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Last use\n(logscale)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)

    ax.set_yscale('log')
    ax.set_xlim(left=0, right = 700)
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