#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter
 
def main():
    data1 = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/interaction_graph"
    plot_file = dir_path + "/../Data/PlotData/plot/centrality_degree.pdf"
    plot_file2 = dir_path + "/../Data/PlotData/plot/clustering_coef.pdf"
    plot_file3 = dir_path + "/../Data/PlotData/plot/connextion_account.pdf"
    dir_list = os.listdir(data_file)
    tmp_list = [int(dir_list[i].split(".")[0]) for i in range(len(dir_list))]
    dir_list = sorted(tmp_list)

    for file in dir_list:
        file = data_file + "/" + str(file) + ".csv"
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                data1.append(row)


    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    for item in data1:
        y1.append(float(item[1]))
        y2.append(float(item[2]))
        y3.append(float(item[3]))
        y4.append(float(item[4]))
        y5.append(floor(float(item[4])))
        y6.append(floor(float(item[5])))
        y7.append(floor(float(item[6])))
    x = [i for i in range(len(y1))]
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(x,y1, color="black", linestyle="-", label = "Q1", linewidth=1)
    ax.plot(x,y2, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,y3, color="lightgrey", linestyle="-", label = "Q3", linewidth=1)
    ax.set_xlabel("Windows of 10,000 transactions")
    ax.set_ylabel("Centrality degree")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_yscale('log')
    ax.set_xlim(left=0, right = len(y1))
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(x,y4, color="black", linestyle="-", label = "All active accounts", linewidth=1)

    ax.set_xlabel("Windows of 10,000 transactions")
    ax.set_ylabel("Clustering Coeficient")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_ylim(bottom=0, top=0.3)
    ax.set_xlim(left=0, right = len(y1))
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(plot_file2,  bbox_inches='tight', format = "pdf")

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(x,y5, color="black", linestyle="-", label = "Q1", linewidth=1)
    ax.plot(x,y6, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,y7, color="lightgrey", linestyle="-", label = "Q3", linewidth=1)
    ax.set_xlabel("Windows of 10,000 transactions")
    ax.set_ylabel("Connexion per account")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_xlim(left=0, right = len(y1))
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(plot_file3,  bbox_inches='tight', format = "pdf")
if __name__ == "__main__":
   main()
