#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/smart_contract_list.csv"
    plot_file = dir_path + "/../Data/PlotData/nb_smart_contract.pdf"
    
    with open(data_file, 'r') as csvfile:
        data = []
        csvreader = csv.reader(csvfile)
        next(csvreader)
        #Collecting all data
        for row in csvreader:
            data.append(row)

        result_x = []
        result_y = []
        for row in data:
            result_x.append(int(row[1]))
        result_x = sorted(result_x)
        result_y = [k for k in range(len(result_x))]
        fig = plt.figure()
        fig.set_figwidth(6)
        fig.set_figheight(2)
        ax  = fig.add_subplot(1,1,1)
        ax.plot(result_x, result_y, color="grey", linestyle="-", label = "\% of Empty block")

        ax.set_xlabel("Windows of 10,000 blocks")
        ax.set_ylabel("Number of Smart contract")
        ax.grid()
        formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
        ax.xaxis.set_major_formatter(formatter1)
        ax.set_ylim(bottom=0)
        ax.set_xlim(left=0, right = result_x[-1])
        labelx = -0.15
        ax.yaxis.set_label_coords(labelx, 0.5)
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")

if __name__ == "__main__":
   main()