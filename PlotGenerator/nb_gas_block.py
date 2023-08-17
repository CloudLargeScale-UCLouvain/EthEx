#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/nb_gas_block.txt"
    plot_file = dir_path + "/../Data/PlotData/nb_gas_block.pdf"
    
    with open(data_file, 'r') as file:
        raw = file.read()
        data = raw.split("\n")
        x_graduation = []
        nb_empty = []
        limit = []
        block_limit = []
        for x in data:
            item = x.split(" ")
            if len(item) == 3:
                x_graduation.append(int(item[0]))
                nb_empty.append(int(item[1]))
                block_limit.append(int(item[2]))
                if(int(item[0]) < 12965000):
                    limit.append(15000000)
                else:
                    limit.append(30000000)
        
        nb_gas_result = []
        limit_result = []
        i = 0
        k = 0
        tmp_result = 0
        tmp_limit = 0
        x_graduation_result = []
        while i < len(nb_empty):
            if k == 10000:
                nb_gas_result.append(tmp_result)
                limit_result.append(tmp_limit)
                x_graduation_result.append(x_graduation[i])
                k =0
                tmp_limit = 0
                tmp_result = 0
            tmp_result += nb_empty[i]
            tmp_limit += limit[i]
            k += 1
            i += 1




        fig = plt.figure()
        fig.set_figwidth(6)
        fig.set_figheight(2)
        ax  = fig.add_subplot(111)
        ax.plot(x_graduation_result, nb_gas_result, color="grey", linestyle="-", label = "Gas")
        ax.plot(x_graduation_result, limit_result, color="black", linestyle="--", label = "Gas limit")
        ax.set_xlabel("Windows of 10,000 blocks")
        ax.set_ylabel("Gas")
        ax.grid()
        ax.set_ylim(bottom=0)
        formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
        ax.xaxis.set_major_formatter(formatter1)
        ax.yaxis.set_major_formatter(formatter1)
        ax.set_xlim(left=0, right = x_graduation_result[-1])
        ax.legend(loc= 'upper left')
        labelx = -0.15
        ax.yaxis.set_label_coords(labelx, 0.5)

        ax2 = ax.twinx()
        ax2.set_ylabel(' \n \n \n ', color="grey")
        ax2.axes.get_yaxis().set_ticks([])
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.tight_layout()
        plt.savefig(plot_file, format = "pdf")
        

if __name__ == "__main__":
   main()