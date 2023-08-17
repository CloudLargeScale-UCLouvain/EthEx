#!/usr/bin/python

import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter
from random import randint

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file_4 = dir_path + "/../Data/ProcessedData/metis_size_4_nb_inter.txt"
    data_file_8 = dir_path + "/../Data/ProcessedData/metis_size_8_nb_inter.txt"
    data_file_32 = dir_path + "/../Data/ProcessedData/metis_size_32_nb_inter.txt"

    data_file_16 = dir_path + "/../Data/ProcessedData/metis_size_16_nb_inter.txt"
    data_file_64 = dir_path + "/../Data/ProcessedData/metis_size_64_nb_inter.txt"

    plot_file_16 = dir_path + "/../Data/PlotData/metis_nb_inter_cluster_16.pdf"
    plot_file_64 = dir_path + "/../Data/PlotData/metis_nb_inter_cluster_64.pdf"
    plot_file_merge = dir_path + "/../Data/PlotData/metis_nb_inter_cluster_merge.pdf"


    print("plot size 16")
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    x = []
    with open(data_file_16, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1])/2, float(tmp[2])/2, float(tmp[3])/2, float(tmp[4])/2]
            x.append(int(tmp[0]))
            data.sort()
            result1.append(data[0])
            result2.append(data[1])
            result3.append(data[2])
            result4.append(data[3])

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(x,result4, color="Red", linestyle="-", label = "Max", linewidth=1)
    ax.plot(x,result3, color="black", linestyle="-", label = "Q3", linewidth=1)
    ax.plot(x,result2, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,result1, color="lightgrey", linestyle="-", label = "Q1", linewidth=1)
    
    
    

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Cross-shard \n transactions proportion (%)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='upper right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file_16, format = "pdf")

    print("plot size 64")

    x = []
    result1 = []
    result2 = []
    result3 = []
    result4 = []

    with open(data_file_64, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1])/2, float(tmp[2])/2, float(tmp[3])/2, float(tmp[4])/2]
            x.append(int(tmp[0]))
            data.sort()
            result1.append(data[0])
            result2.append(data[1])
            result3.append(data[2])
            result4.append(data[3])

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(x,result4, color="Red", linestyle="-", label = "Max", linewidth=1)
    ax.plot(x,result3, color="black", linestyle="-", label = "Q3", linewidth=1)
    ax.plot(x,result2, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,result1, color="lightgrey", linestyle="-", label = "Q1", linewidth=1)
    
    
    

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Cross-shard \n transactions proportion (%)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='upper right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file_64, format = "pdf")

    print("plot merge")
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    result7 = []
    result8 = []
    x = []
    i = 1.2
    with open(data_file_16, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1]), float(tmp[2]), float(tmp[3]), float(tmp[4])]
            x.append(int(tmp[0]))
            data.sort()
            result1.append(data[0])
            result2.append(data[1])
            result3.append(data[2])
            result4.append(data[3])
            i += 0.002
    i = 1.2

    with open(data_file_64, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1]), float(tmp[2]), float(tmp[3]), float(tmp[4])]
            data.sort()
            result5.append(data[0])
            result6.append(data[1])
            result7.append(data[2])
            result8.append(data[3])
            i += 0.004
    i = 1.2

    result5 = []
    with open(data_file_32, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1]), float(tmp[2]), float(tmp[3]), float(tmp[4])]
            data.sort()
            result5.append(data[1])
            i += 0.003
    i = 1.2

    result4 = []
    with open(data_file_8, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1]), float(tmp[2]), float(tmp[3]), float(tmp[4])]
            data.sort()
            result4.append(data[1])
            i += 0.0015
    i = 1.2

    result3 = []
    with open(data_file_4, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            data = [float(tmp[1]), float(tmp[2]), float(tmp[3]), float(tmp[4])]            
            data.sort()
            result3.append(data[1])
            i += 0.0009
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(result6, color="red", linestyle="-", label = "64 clusters", linewidth=1)
    ax.plot(result5, color="blue", linestyle="-", label = "32 clusters", linewidth=1)
    ax.plot(result2, color="lightgrey", linestyle="-", label = "16 clusters", linewidth=1)
    ax.plot(result4, color="grey", linestyle="-", label = "8 clusters", linewidth=1)
    ax.plot(result3, color="black", linestyle="-", label = "4 clusters", linewidth=1)

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Proportion (%) \n ")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='upper left', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file_merge, format = "pdf")
if __name__ == "__main__":
   main()