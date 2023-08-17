#!/usr/bin/python

import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    plot_file = dir_path + "/../Data/PlotData/account_futur.pdf"
    plot_file2 = dir_path + "/../Data/PlotData/account_age.pdf"
    plot_file3 = dir_path + "/../Data/PlotData/account_lifetime.pdf"

    save_file = dir_path + "/../Data/ProcessedData/account_frequency_timeToFirst_timeToLast_2.txt"

    data =[]
    with open(save_file, 'r') as txt_files:
        k = 0
        for line in txt_files:
            if k > 0:
                data.append(line.strip().split(","))
            k += 1
    
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    y10 = []
    y11 = []
    tmp_y = []
    tmp_x = []
    y12 = []
    for x in data:
        y1.append(float(x[-4]))
        y2.append(float(x[-3]))
        y3.append(float(x[-2]))
        if float(x[-1]) <= len(data) - int(x[0])//1000000:
            y11.append(float(x[-1]))
        else:
            y11.append(len(data) - int(x[0])//1000000)

        y4.append(float(x[5]))
        y5.append(float(x[6]))
        y6.append(float(x[7]))
        tmp_y.append(float(x[8]))

        y7.append(y1[-1] + y4[-1])
        y8.append(y2[-1] + y7[-1])
        y9.append(y3[-1] + y6[-1])
    for i in range(len(tmp_y)):
        if tmp_y[i] > i:
            y10.append(i)
        else:
            y10.append(tmp_y[i])

    for i in range(len(y11)):
        y12.append(y11[i] + y10[i])
    
#=======================================futur

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(y11, color="red", linestyle="-", label = "Max")
    ax.plot(y3, color="black", linestyle="-", label = "Q3")
    ax.plot(y2, color="lightgrey", linestyle="-", label = "Q2")
    ax.plot(y1, color="grey", linestyle="-", label = "Q1")
    
    
    
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Future\n (logscale)")
    ax.grid()
    ax.set_ylim(bottom=0)
    ax.set_xlim(left=0, right = len(y4))
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.set_yscale('log')

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")




#=======================================age

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(y10, color="red", linestyle="-", label = "Max")
    ax.plot(y6, color="black", linestyle="-", label = "Q3")
    ax.plot(y5, color="lightgrey", linestyle="-", label = "Q2")
    ax.plot(y4, color="grey", linestyle="-", label = "Q1")
    
    
    ax.legend(loc='upper left', prop={'size': 6})
    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Age\n(logscale)")
    ax.grid()
    ax.set_xlim(left=0, right = len(y4))
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.set_yscale('log')

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file2, format = "pdf")

#=======================================Lifetime
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(y12, color="red", linestyle="-", label = "Max")
    ax.plot(y9, color="black", linestyle="-", label = "Q3")
    ax.plot(y8, color="lightgrey", linestyle="-", label = "Q2")
    ax.plot(y7, color="grey", linestyle="-", label = "Q1")
   
    
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Lifetime (windows)\n (logscale)")
    ax.grid()
    #ax.set_ylim(bottom=0)
    ax.set_xlim(left=0, right = len(y4))
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    #ax.set_yscale('log')

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    #ax2.yaxis.set_major_formatter(formatter1)
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file3, format = "pdf")
if __name__ == "__main__":
   main()