#!/usr/bin/python
import os
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/last_use_vector.txt"

    plot_file2 = dir_path + "/../Data/PlotData/last_use_vector_cdf2.pdf"

    plot_file1 = dir_path + "/../Data/PlotData/last_use_vector_scatter.pdf"
    print("start up")
    with open(data_file, 'r') as txt_files:
        i = 0
        data = []
        for line in txt_files:
            data.append(line.split(","))
    result = [0]
    index = [0]
    print("launch")
    test = 0
    tmp = 0
    
    for account in data:
        tmp = float(account[0])
        print(i,"/",len(data))
        result.append(tmp)
        index.append((i/len(data))*100 )
        i += 1
#CDF2
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(result,index, color="black", linestyle="-", label = "vector", linewidth=1)
    ax.set_ylabel("Accounts %")
    ax.set_xlabel("Vector average last_use x nb_access")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_ylim(bottom=0, top=100)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file2, format = "pdf")

    
#Scatter plot

    x1 = []
    y1 = []
    for x in data:
        if float(x[1]) > 1:
            x1.append(float(x[1]))
            y1.append(float(x[2]))


    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.scatter(x1,y1, c="black",s = 5, marker = '^', label = "low activity accounts")
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Number of access")
    ax.set_ylabel("Average Last use")
    ax.set_ylim(bottom=0)
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
    plt.savefig(plot_file1, format = "pdf")
    
if __name__ == "__main__":
   main()