#!/usr/bin/python

import csv
import os
import numpy as np

def read_csv(file):
    data= []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
             data.append(row)
    return data


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    account_file = dir_path + "/../Data/ProcessedData/global.txt"
    window = 1_000_000

    print("load account_data")
    account_data = []
    with open(account_file, 'r') as txt_files:
        for line in txt_files:

            tmp = line.strip().split(":")
            tmp_trans = []
            if tmp[1] != "to":
                tmp_trans += tmp[1].split(",")
            if tmp[2] != "from":
                tmp_trans += tmp[2].split(",")
            
            tmp_int_trans = []
            for x in tmp_trans:
                if x != "":
                    tmp_int_trans.append(int(x)//window)
            tmp_int_trans = sorted(tmp_int_trans)
            first = tmp_int_trans[0]
            last = tmp_int_trans[-1]
            if first == last:
                frequency = 1
            else:
                tmp = first
                cpt = []
                for x in tmp_int_trans:
                    if x not in cpt:
                        cpt.append(x)
                frequency = min(len(cpt)/(last - first),1)
            account_data.append([first, frequency])
    print("process")
    for window in range(0, 700):
        print(window, "/", 700)
        tmp_list = []
        for x in account_data:
            if x[0] == window:
                tmp_list.append(x[1])

        if len(tmp_list) > 1:
            #print(tmp_list)
            tmp_list_value = np.array(tmp_list)
            tmp_list_quartiles = np.percentile(tmp_list_value, [25, 50, 75])
            last_use_max = max(tmp_list)
            with open(dir_path + "/../Data/ProcessedData/frequency.txt", 'a') as txt_files:
                #line = str(window) + "," + str(tmp_list_quartiles[0]) + "," + str(statistics.mean(tmp_list_value)) + "," + str(tmp_list_quartiles[2]) + "," + str(last_use_max) + "\n"
                line = str(window) + "," + str(tmp_list_quartiles[0]) + "," + str(tmp_list_quartiles[1]) + "," + str(tmp_list_quartiles[2]) + "," + str(last_use_max) + "\n"

                txt_files.write(line)

if __name__ == "__main__":
   main() 