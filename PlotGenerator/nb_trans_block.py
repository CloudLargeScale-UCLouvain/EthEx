#!/usr/bin/python
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/nb_trans_block.txt"
    plot_file = dir_path + "/../Data/PlotData/nb_trans_block.pdf"
    
    with open(data_file, 'r') as file:
        raw = file.read()
        data = raw.split("\n")
        x_graduation = []
        nb_empty = []
        for x in data:
            item = x.split(" ")
            if len(item) == 2:
                x_graduation.append(int(item[0]))
                nb_empty.append(int(item[1]))

        nb_empty_result = []
        i = 0
        k = 0
        tmp_nb_empty = 0
        x_graduation_result = []
        while i < len(nb_empty):
            if k == 10000:
                nb_empty_result.append(tmp_nb_empty)
                x_graduation_result.append(x_graduation[i])
                k =0
                tmp_nb_empty = 0
            tmp_nb_empty += nb_empty[i]
            k += 1
            i += 1        

        fig = plt.figure()
        fig.set_figwidth(6)
        fig.set_figheight(2)
        ax  = fig.add_subplot(1,1,1)
        ax.plot(x_graduation_result, nb_empty_result, color="grey", linestyle="-", label = "number of transaction")
        ax.set_xlabel("Windows of 10,000 blocks")
        ax.set_ylabel("Transactions")
        ax.grid()
        ax.set_ylim(bottom=0)
        ax.set_xlim(left=0, right = x_graduation_result[-1])
        formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
        ax.xaxis.set_major_formatter(formatter1)
        ax.yaxis.set_major_formatter(formatter1)
        labelx = -0.15
        ax.yaxis.set_label_coords(labelx, 0.5)
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")
        

if __name__ == "__main__":
   main()