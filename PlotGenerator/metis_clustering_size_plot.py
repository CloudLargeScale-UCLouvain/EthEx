import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    data_file_4 = dir_path + "/../Data/ProcessedData/metis_size_4_size.txt"
    data_file_8 = dir_path + "/../Data/ProcessedData/metis_size_8_size.txt"
    data_file_32 = dir_path + "/../Data/ProcessedData/metis_size_32_size.txt"

    data_file_16 = dir_path + "/../Data/ProcessedData/metis_size_16_size.txt"
    data_file_64 = dir_path + "/../Data/ProcessedData/metis_size_64_size.txt"
    plot_file_16 = dir_path + "/../Data/PlotData/metis_size_cluster_16.pdf"
    plot_file_64 = dir_path + "/../Data/PlotData/metis_size_cluster_64.pdf"
    plot_file_merge = dir_path + "/../Data/PlotData/metis_size_cluster_merge.pdf"



    print("plot size 16")
    result1 = []
    result2 = []
    result3 = []
    result4 = []

    x = []
    with open(data_file_16, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            x.append(int(tmp[0]))
            result1.append(float(tmp[1]))
            result2.append(float(tmp[2]))
            result3.append(float(tmp[3]))
            result4.append(float(tmp[4]))

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(x,result4, color="red", linestyle="-", label = "Max", linewidth=1)
    ax.plot(x,result3, color="black", linestyle="-", label = "Q3", linewidth=1)
    ax.plot(x,result2, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,result1, color="lightgrey", linestyle="-", label = "Q1", linewidth=1)
    
    
    

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Size of clusters\n(logscale)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    #ax.set_ylim(bottom=0, top=100)
    #ax.set_ylim(bottom=10, top=10000)

    #ax.set_yscale('log')
    #ax.yaxis.set_major_locator(plt.LogLocator(base=10, numticks=10))
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='upper right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    #ax2.yaxis.set_major_formatter(formatter1)
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file_16, format = "pdf")

    print("plot size 64")
    result1 = []
    result2 = []
    result3 = []
    result4 = []

    x = []
    with open(data_file_64, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            x.append(int(tmp[0]))
            result1.append(float(tmp[1]))
            result2.append(float(tmp[2]))
            result3.append(float(tmp[3]))
            result4.append(float(tmp[4]))

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(x,result4, color="red", linestyle="-", label = "Max", linewidth=1)
    ax.plot(x,result3, color="black", linestyle="-", label = "Q3", linewidth=1)
    ax.plot(x,result2, color="grey", linestyle="-", label = "Q2", linewidth=1)
    ax.plot(x,result1, color="lightgrey", linestyle="-", label = "Q1", linewidth=1)
    
    
    

    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Size of clusters\n(logscale)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    #ax.set_ylim(bottom=0, top=100)
    #ax.set_ylim(bottom=10, top=10000)

    #ax.set_yscale('log')
    #ax.yaxis.set_major_locator(plt.LogLocator(base=10, numticks=10))
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='upper right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    #ax2.yaxis.set_major_formatter(formatter1)
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
    x = []
    with open(data_file_64, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            x.append(int(tmp[0]))
            result1.append(float(tmp[4]))
    
    with open(data_file_16, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            result2.append(float(tmp[4]))

    with open(data_file_32, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            result3.append(float(tmp[4]))

    with open(data_file_8, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            result4.append(float(tmp[4]))

    with open(data_file_4, 'r') as txt_files:
        for line in txt_files:
            tmp = line.strip().split(",")
            result5.append(float(tmp[4]))

    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)

    ax.plot(x,result5, color="black", linestyle="-", label = "4 clusters", linewidth=1)
    ax.plot(x,result4, color="grey", linestyle="-", label = "8 clusters", linewidth=1)
    ax.plot(x,result2, color="lightgrey", linestyle="-", label = "16 clusters", linewidth=1)
    ax.plot(x,result3, color="blue", linestyle="-", label = "32 clusters", linewidth=1)
    ax.plot(x,result1, color="red", linestyle="-", label = "64 clusters", linewidth=1)
 
    
    ax.set_xlabel("Windows of 1,000,000 transactions")
    ax.set_ylabel("Size of clusters\n(logscale)")
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
    plt.savefig(plot_file_merge, format = "pdf")

if __name__ == "__main__":
   main()