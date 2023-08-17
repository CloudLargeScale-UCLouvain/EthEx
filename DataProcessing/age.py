#!/usr/bin/python

import os
import statistics

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/address_from_to.txt"

    save_file = dir_path + "/../Data/ProcessedData/account_age.txt"
    window = 10000
    global_data = []

    with open(data_file, 'r') as txt_files:
        for line in txt_files:
            row = line.strip().split(":")
            if row[1] != "" and row[2] != "":
                tmp = row[1].split(",") + row[2].split(",")
            if row[1] == "" and row[2] != "":
                tmp = row[2].split(",")
            if row[1] != "" and row[2] == "":
                tmp = row[1].split(",")
            tmp = sorted(tmp)
            if tmp[0] == '':
                tmp = tmp[1:]
            global_data.append([row[0], tmp])
    i = 0
    result = [[] for x in range(71537)]
    for account in global_data:
        if i % 100000 == 0:
            print(str(i),"/",str(len(global_data)))
        tmp = [int(account[1][k]) for k in range(len(account[1]))]
        min_window = min(tmp)//window
        for _ in tmp:
            result[min_window].append(age)
        max_window = max(tmp)//window
        min_window = min(tmp)//window
        age = abs(max_window-min_window)
        if age == 0:
            age = 1
        result[min_window].append(age)
        i += 1

    with open(save_file, 'a') as output_file:
        for x in range(len(result)):

            try:
                line = str(x) + "," +str(statistics.mean(result[x])) + "\n"
            except:
                line = str(x) + "," +str(1) + "\n"
            output_file.writelines(line)
    output_file.close()

if __name__ == "__main__":
   main()