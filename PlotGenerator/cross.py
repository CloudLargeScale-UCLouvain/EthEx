#!/usr/bin/python

import os
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/crossshard_accounts_concat.txt"

    plot_file2 = dir_path + "/../Data/PlotData/cross_cdf.pdf"
    global_data = []
    print("start up")
    with open(data_file, 'r') as txt_files:
        len_file = 0
        for line in txt_files:
            len_file += 1
    with open(data_file, 'r') as txt_files:
        i = 0
        for line in txt_files:
            if i%100_000 == 0:
                print(i,"/",len_file)
            row = line.split(",")
            global_data.append(int(row[1]))
            i += 1
    
    nb_accounts = (len(global_data)//36)*100
    print(len(global_data))
    print(nb_accounts)
    i = 0
    print("sorting")
    result_data = sorted(global_data)
    global_data = 0
    nb_zero = nb_accounts - len(result_data)
    result2 = [0 for i in range(nb_zero)] 
    index = [(i/nb_accounts)*100 for i in range(nb_accounts)]
    print(line)
    print("launch")
    i = 0
    for account in result_data:
        if i%100_000 == 0:
            print(i,"/",len(result_data))
        result2.append(account)
        i += 1
    
    result = []
    index_result = []
    k = 0
    bar = 0
    for i in range(len(result2)):
        if i % 1000 == 0:
            if result2[i] > 1000:
                result.append(1000)
                if index[i]> 89.2 and k == 0:
                    k = 1
                    bar = result[-1]


            else:
                result.append(result2[i])
                if index[i]> 89.2 and k == 0:
                    k = 1
                    bar = result[-1]
            index_result.append(index[i])

#CDF2
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(result,index_result, color="black", linestyle="-", label = "", linewidth=1)
    ax.axvline(x=bar, color='r', linestyle='--')
    ax.set_ylabel("Accounts % \n ")
    ax.set_xlabel("Crossshard transactions")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_ylim(bottom=0, top=105)

    ax.set_xlim(left=0, right = 1200)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file2, format = "pdf")

if __name__ == "__main__":
   main()