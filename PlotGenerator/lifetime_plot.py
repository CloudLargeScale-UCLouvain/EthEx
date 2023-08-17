#!/usr/bin/python


import csv
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    plot_file = dir_path + "/../Data/PlotData/account_lifetime.pdf"
    save_file = dir_path + "/../Data/ProcessedData/account_age.txt"

    data =[]
    with open(save_file, 'r') as txt_files:
        for line in txt_files:
            data.append(line.strip().split(","))
    
    result = []
    for x in data:
        if float(x[1])>1:
            result.append(float(x[1]))
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(result, color="grey", linestyle="-", label = "Average frequency")
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Windows of 10,000 transactions")
    ax.set_ylabel("Linfetime (windows)")
    ax.grid()
    ax.set_ylim(bottom=0, top= max(result) + 1)
    ax.set_xlim(left=0)
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.grid()
    plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")

if __name__ == "__main__":
   main()