#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/PlotData/account_age_distribution.csv"
    plot_file = dir_path + "/../Data/Plot/account_age_distribution.pdf"
    
    with open(data_file, 'r') as csvfile:
        data = []
        age = []
        csvreader = csv.reader(csvfile)
        next(csvreader)
        #Collecting all data
        for row in csvreader:
            data.append(row)


        for x in data:
            age.append(abs(int(x[2])-int(x[1])))
        fig = plt.figure()
        fig.set_figwidth(6)
        fig.set_figheight(2)
        ax  = fig.add_subplot(1,1,1)
        violin_parts = ax.violinplot(age, points=20, widths=0.3,
                     showmeans=True, showextrema=True, showmedians=True)
        ax.set_ylabel("age of accounts")
        for partname in ('cbars','cmins','cmaxes','cmeans','cmedians'):
            vp = violin_parts[partname]
            vp.set_edgecolor("black")
            vp.set_linewidth(1)
        for vp in violin_parts['bodies']:
            vp.set_facecolor("grey")
            vp.set_edgecolor("black")
        ax.grid()
        plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")

if __name__ == "__main__":
   main()