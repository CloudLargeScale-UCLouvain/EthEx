#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
import os
from math import floor, inf
import numpy as np
import sys
from matplotlib.ticker import EngFormatter

csv.field_size_limit(sys.maxsize)

def limit_nb_tx(data):
    max = 0
    min = inf
    for x in data:
        if int(x)<min:
            min = int(x) 
        if int(x)>max:
            max = int(x)
    return min,max

def limit_age_tx(data):
    max = 0
    min = inf
    for x in data:
        if int(x)<min:
            min = int(x) 
        if int(x)>max:
            max = int(x)
    return min,max

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/account_frequency_age.csv"
    plot_file = dir_path + "/../Data/PlotData/account_heatmap.pdf"
    

    with open(data_file, 'r') as csvfile:
        data = []
        csvreader = csv.reader(csvfile)
        next(csvreader)
        #Collecting all data
        for row in csvreader:
            data.append(row)
    age_list = []
    nb_tx = []
    for x in data:
        age_list.append(float(x[2]))
        nb_tx.append(int(x[3]))
    
    _ , max_nb_tx = limit_nb_tx(nb_tx)
    _ , max_age_tx = limit_age_tx(age_list)
    x_nb_case = 10
    y_nb_case = 10
    array_size = (x_nb_case,y_nb_case)
    data = np.zeros(array_size)

    x_scale = max_nb_tx/x_nb_case
    y_scale = max_age_tx/y_nb_case

    for i in range(len(nb_tx)):
        x = floor(nb_tx[i]/x_scale)
        if x >=10:
            x = 9
        y = floor(age_list[i]/y_scale)
        if y >= 10:
            y = 9
        data[x][y] = data[x][y] + 1
    
    
    fig = plt.figure()
    ax  = fig.add_subplot(1,1,1)
    ax.set_ylabel('age of account')
    ax.set_xlabel('nb transaction')
    
    formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
    ax.xaxis.set_major_formatter(formatter1)
    ax.yaxis.set_major_formatter(formatter1)
    plt.imshow(data, cmap='gray',origin='lower')
    plt.savefig(plot_file,  bbox_inches='tight', format = "pdf")

    plt.show()
if __name__ == "__main__":
   main()