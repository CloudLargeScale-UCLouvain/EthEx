#!/usr/bin/python


import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter
import random

def main():
     
     
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/account_frequency_age.csv"
    plot_file = dir_path + "/../Data/PlotData/plot/scatter_1.pdf"
    plot_file2 = dir_path + "/../Data/PlotData/plot/scatter_2.pdf"

    with open(data_file, 'r') as csvfile:
        data = []
        csvreader = csv.reader(csvfile)
        next(csvreader)
        #Collecting all data
        for row in csvreader:
            data.append(row)
    window = 1000000
    size_scatter = 10_000
    x1 = []
    y1 = []
    x3 = []
    y3 = []
    z3 = []
    z1 = []
    nodes = []
    node_2 = set()
    i = 0
    print(i)

    while len(nodes) < size_scatter:
            print(len(node_2))
            tmp_node = data[random.randint(0,len(data)-1)]
            if tmp_node[0] not in node_2:
                node_2.add(tmp_node[0])
                nodes.append([i, int(tmp_node[3]), (int(tmp_node[-1])- int(tmp_node[-2]))//window, float(tmp_node[1])*window])
                nodes.sort(key = lambda row: row[1])
            i+=1

    upleft = 0
    upright = 0
    lowerleft = 0
    loweright = 0

    k1 = floor(0.01*len(nodes))
    print(k1)
    for i in range(k1):
        x3.append(nodes[-i][1])
        y3.append(nodes[-i][2])
        z3.append(nodes[-i][3])
        if nodes[-i][2]> 200:
           upright += 1
        else:
            loweright += 1
         
    for i in range(len(nodes) - k1):
        x1.append(nodes[i][1])
        y1.append(nodes[i][2])

        if nodes[-i][2] > 200:
           upleft += 1
        else:
            lowerleft += 1

        if nodes[i][3] == 0:
            z1.append(1)
        else:
            z1.append(nodes[i][3])
        
    print(upright/size_scatter)
    print(upleft/size_scatter)
    print(loweright/size_scatter)
    print(lowerleft/size_scatter)

    print(len(x1))
    print(len(x3))
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.scatter(x1,y1, c="black",s = 5, marker = '^', label = "low activity accounts")
    ax.scatter(x3,y3, c="red",s = 5, marker = '+', label = "Heavy hitters")
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Number of transactions")
    ax.set_ylabel("Lifetime (windows)")
    ax.set_ylim(bottom=0)
    ax.set_xlim(left=1)
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.set_xscale('log')
    ax.grid()

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")
    
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.scatter(x1,z1, c="black",s = 5, marker = '^', label = "low activity accounts")
    ax.scatter(x3,z3, c="red",s = 5, marker = '^', label = "Heavy hitters")
    ax.set_xlabel("Number of transactions (logscale)")
    ax.set_ylabel("Frequency (logscale)")
    ax.set_ylim(bottom=0.001)
    ax.set_xlim(left=1)
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid()
    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file2, format = "pdf")
    
    ax.grid()
if __name__ == "__main__":
   main()