#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter


def getEmpty():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/nb_empty_block.csv"
    
    with open(data_file, 'r') as csvfile:
        data = []
        x_graduation = []
        nb_empty = []
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            data.append(row)


        for x in data:
            x_graduation.append(int(x[0]))
            nb_empty.append(floor(float(x[1])))
    return x_graduation, nb_empty 

def getNbTrans():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/nb_trans_block.txt"
    
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
    return x_graduation_result, nb_empty_result

def main():

    x1, result1 = getEmpty()
    x2, result2 = getNbTrans()
    x3 = min(len(x2),len(x1))

    if x3 == len(x2):
        x3 = x2
    else:
        x3 = x1

    dir_path = os.path.dirname(os.path.realpath(__file__))
    plot_file = dir_path + "/../Data/PlotData/nb_empty_block_nb_trans.pdf"

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)

    ax  = plt.subplot(111)
    l1 = ax.plot(x3, result1[0:len(x3)], color="black", linestyle="-", label = "Empty blocks")
    ax.set_xlabel("Windows of 10,000 blocks")
    ax.set_ylabel("Proportion (%)", color="black")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_ylim(bottom=0, top=100)
    ax.set_xlim(left=0, right = x3[-1])
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)

    ax2 = ax.twinx()
    l2 = ax2.plot(x3, result2[0:len(x3)], color="grey", linestyle="-", label = "Transactions")
    ax2.set_ylabel('Transactions', color="grey")
    ax2.yaxis.set_major_formatter(formatter1)

    lns = l1+l2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc='upper left', prop={'size': 6})
    print(ax.get_position())
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")

if __name__ == "__main__":
   main()