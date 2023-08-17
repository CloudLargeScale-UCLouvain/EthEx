#!/usr/bin/python


import matplotlib.pyplot as plt
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    plot_file = dir_path + "/../Data/PlotData/account_frequency.pdf"
    save_file = dir_path + "/../Data/ProcessedData/frequency.txt"

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
    for x in data:
        y1.append(float(x[1]))
        y2.append(float(x[2]))
        y3.append(float(x[3]))
        y4.append(float(x[4]))
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    
    ax.plot(y4, color="red", linestyle="-", label = "Max")
    ax.plot(y3, color="black", linestyle="-", label = "Q3")
    ax.plot(y2, color="lightgrey", linestyle="-", label = "Q2")
    ax.plot(y1, color="grey", linestyle="-", label = "Q1")
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Frequency\n ")
    ax.grid()
    ax.set_xlim(left=0, right = len(y4))
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