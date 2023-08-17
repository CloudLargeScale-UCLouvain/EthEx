#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor
from matplotlib.ticker import EngFormatter, ScalarFormatter
import matplotlib.ticker as ticker
import statistics
import numpy as np
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file1 = dir_path + "/../Data/ProcessedData/prop_account.txt"
    data_file2 = dir_path + "/../Data/ProcessedData/smart_contract_number_list.csv"
    plot_file = dir_path + "/../Data/PlotData/prop_account_creation.pdf"
    
    with open(data_file1, 'r') as file:
        raw = file.read()
        data1 = raw.split("\n")

    with open(data_file2, 'r') as csvfile:
        data2 = []
        csvreader = csv.reader(csvfile)
        next(csvreader)
        #Collecting all data
        for row in csvreader:
            data2.append(row)

    y1 = []
    y2 = []
    for k in range(min([len(data1),len(data2)])):
        if int(data2[k][1])<int(data1[k]):
            y1.append(int(data2[k][1]))
            y2.append((int(data1[k]) - int(data2[k][1])))

    y3 = []
    for k in range(len(y1)):
        y3.append(y1[k]+y2[k])   
    result1 = []
    result2 = []
    k = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(len(y3)):
        if k == 100:
            k = 0
            result1.append(tmp1)
            result2.append(tmp2)
            tmp1 = 0
            tmp2 =0
        k+=1
        tmp1 += y1[i]
        tmp2 += y3[i]
    result1.append(tmp1)
    result2.append(tmp2)


    print("SCA", sum(result1))
    print("EOA", sum(result2))
    print("EOA=", 67865097/307336589*100) #Extract manually
    print("SCA=", 3281955/16885670*100) #Extract manually
    x = [k for k in range(len(result1))]    
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(x, result2, color="grey", linestyle="-", label = "EOA", linewidth=1)
    ax.plot(x, result1, color="black", linestyle="-", label = "SCA", linewidth=1)

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Accounts created\n(logscale)")
    ax.grid()
    ax.set_xlim(left=0, right = 700)
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    ax.set_yscale('log')
    ax.yaxis.set_major_locator(plt.LogLocator(base=10, numticks=5))
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