#!/usr/bin/python
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/PlotData/processed_data/account_tx/global.txt"
    plot_file = dir_path + "/../Data/PlotData/lifetime_cdf2.pdf"


    save_file = dir_path + "/../Data/ProcessedData/account_age.txt"
    window = 1_000_000
    global_data = []
    print("start up")
    with open(data_file, 'r') as txt_files:
        len_file = 0
        for line in txt_files:
            len_file += 1
    with open(data_file, 'r') as txt_files:
        i = 0
        tmp = []
        for line in txt_files:
            if i% 100_000 == 0  :
                print(i,"/",len_file)

            row = line.strip().split(":")
            if row[1] != "to":
                tmp += [int(x) for x in row[1].split(",") if x != '']
                age_min = tmp[0]
                age_max = tmp[-1]
            else: 
                age_min = 1_000_000_000_000_000
                age_max = -1
            if row[2] != "from":
                tmp_from = [int(x) for x in row[2].split(",") if x != '']
                age_min = min(age_min,tmp_from[0])
                age_max = max(age_max,tmp_from[-1])
                tmp += tmp_from

            if len(tmp) >= 1:
                age = age_min//1_000_000 - age_max//1_000_000
            else:
                age = 1
            if age < 0:
                age = -age
            if age == 0:
                age = 1
            global_data.append([int(row[0][1:-1], 0), age])
            i += 1
    i = 0
    print("sorting")
    result_data = sorted(global_data, key=lambda x: x[1])
    result_cpt = 0
    result = [0]
    result2 = [0]
    index = [0]
    print("launch")
    test = 0
    for account in result_data:
        print(i,"/",len(result_data))
        result_cpt += account[1]
        result.append(result_cpt)
        result2.append(account[1])
        index.append((i/len(result_data))*100 )
        i += 1
        if account[1] == 1:
            test += 1
    print(test/len(result2))

#CDF2
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(2)
    ax  = fig.add_subplot(1,1,1)
    ax.plot(result2,index, color="black", linestyle="-", label = "Lifetime", linewidth=1)
    ax.set_ylabel("Accounts %")
    ax.set_xlabel("Lifetime (windows)")
    ax.grid()
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.set_ylim(bottom=0, top=100)
    ax.set_xlim(left=0, right = 700)
    labelx = -0.15
    ax.yaxis.set_label_coords(labelx, 0.5)
    ax.legend(loc='lower right', prop={'size': 6})

    ax2 = ax.twinx()
    ax2.set_ylabel(' \n \n \n ', color="grey")
    ax2.axes.get_yaxis().set_ticks([])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.savefig(plot_file, format = "pdf")

if __name__ == "__main__":
   main()