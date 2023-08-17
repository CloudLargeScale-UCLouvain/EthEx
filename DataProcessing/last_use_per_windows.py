#!/usr/bin/python

import csv
import os

def sort_directory(list_directory):
    tmp_result = []
    for x in list_directory:
        tmp_result.append(int(x.split(".")[0]))

    tmp = sorted(tmp_result)

    result = []
    for x in tmp:
        result.append(str(x)+".csv")
    return result
def read_csv(file):
    data= []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
             data.append(row)
    return data

def find_place(index,data):
    i = 0
    while i < len(data):
        if data[i] >= index:
            return data[i-1]
        i+= 1
    return -1


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tx_file = dir_path + "/../Data/ProcessedData/transaction_order"
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
            account_data.append([tmp[0], tmp_int_trans])
    dir_list = os.listdir(tx_file)
    dir_list = sort_directory(dir_list)
    file_list = []
    input_index_file = []
    i = 0
    for file in dir_list:
        print(i,"/",len(dir_list))
        if file.split(".")[-1] == "csv":
            print(i,"/",len(dir_list))
            file = tx_file + "/" + file
            file_list.append(file)
            input_index_file.append(i)
            i += 1
    
    index = 0
    for file in file_list:
                print(index,"/",len(file_list))
                data = read_csv(file)
                account_set = set()
                tmp_last_use = []
                tmp_cpt = 0
                for x in data:
                    account_set.add(int(x[1][1:-1],0))
                    account_set.add(int(x[2][1:-1],0))
                
                for x in account_data:
                    if int(x[0][1:-1],0) in account_set:
                        place = find_place(index, x[1])
                        if place > 0 and place-index < 0:
                            tmp_last_use.append([int(x[0][1:-1],0), index - place, x[1][-1] - x[1][0]])
                            tmp_cpt += 1
                if tmp_last_use != []:
                    result_data = sorted(tmp_last_use, key=lambda x: x[1])
                    with open(dir_path + "/../Data/ProcessedData/last_use_windows/" + str(file.split("/")[-1].split(".")[0]) + ".txt", 'a') as txt_files:
                        for x in result_data:
                            line = str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "\n"
                            txt_files.write(line)
                index +=1

if __name__ == "__main__":
   main() 