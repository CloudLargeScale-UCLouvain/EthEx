#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/global.txt"
    plot_file = dir_path + "/../Data/PlotData/nb_trans_account.pdf"
    result = []
    with open(data_file, 'r') as file:
        raw = file.read()
        data = raw.split("\n")
        for x in data:
            item = x.split(",")
            result.append(len(item)-1)




        fig = plt.figure()
        fig.set_figwidth(6)
        fig.set_figheight(2)
        ax  = fig.add_subplot(1,1,1)
        ax.violinplot(result, showmedians=True)
        ax.set_ylabel("Number of transactions")
        ax.grid()
        ax.set_ylim(bottom=0, top = 100000)
        formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
        ax.xaxis.set_major_formatter(formatter1)
        ax.yaxis.set_major_formatter(formatter1)
        labelx = -0.15
        ax.yaxis.set_label_coords(labelx, 0.5)
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

        plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")
        

if __name__ == "__main__":
   main()