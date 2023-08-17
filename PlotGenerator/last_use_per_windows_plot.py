#!/usr/bin/python

import matplotlib.pyplot as plt
import os
from matplotlib.ticker import EngFormatter

def sort_directory(list_directory):
    tmp_result = []
    for x in list_directory:
        tmp_result.append(int(x.split(".")[0]))

    tmp = sorted(tmp_result)

    result = []
    for x in tmp:
        result.append(str(x)+".txt")
    return result

def main():
     
     
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_dir = dir_path + "/../Data/ProcessedData/last_use_windows"
    plot_file = dir_path + "/../Data/PlotData/scatter_last_use.pdf"


    dir_list = os.listdir(data_dir)
    dir_list = sort_directory(dir_list)

    file_list = []
    input_index_file = []
    i = 0
    for file in dir_list:
        print(i,"/",len(dir_list))
        if file.split(".")[-1] == "txt":
            print(i,"/",len(dir_list))
            file = data_dir + "/" + file
            file_list.append(file)
            input_index_file.append(i)
            i += 1

    data = []
    i = 0
    for file in file_list:
            if i < 5:
                account_data = []
                print(i,"/",len(dir_list))
                with open(file, 'r') as txt_files:
                    for line in txt_files:
                        tmp = line.split(",")
                        account_data.append([int(tmp[1]), int(tmp[2])])
                        result_data = sorted(account_data, key=lambda x: x[0])
                    separator = len(result_data)//1000
                    k = 0
                    while k < len(result_data)-(separator*999):
                        data.append(result_data[-k])
                        k += 1
                i += 1

    x1 = []
    y1 = []
    for x in data[len(data)-len(data)//100:]:
        x1.append(x[1])
        y1.append(x[0])
    
    print(len(x1))
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.scatter(x1,y1, c="black",s = 10, marker = '^', label = "low activity accounts")
    ax.legend(loc='upper right', prop={'size': 6})
    ax.set_xlabel("Lifetime")
    ax.set_ylabel("Last Use")
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.grid()
    plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")


if __name__ == "__main__":
   main()