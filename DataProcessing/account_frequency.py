#!/usr/bin/python

import csv
import os
import multiprocessing
import numpy as np

def read_csv(file):
    data= []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
             data.append(row)
    return data

def freq(tx_file, data):
    tx_set = read_csv(tx_file)
    current_index = int(tx_set[0][0])
    h = 0
    frequency = []
    age_from_creation = []
    futur = []
    window = 1_000_000
    y = 0
    result = []
    for tx in tx_set:
        if y == window:
            frequency_values = np.array(frequency)
            age_from_creation__values = np.array(age_from_creation)
            futur_centrality_values = np.array(futur)
            frequency_quartiles = np.percentile(frequency_values, [25, 50, 75])
            age_from_creation_quartiles = np.percentile(age_from_creation__values, [25, 50, 75])
            futur_quartiles = np.percentile(futur_centrality_values, [25, 50, 75])
            frequency_max = max(frequency)
            futur_max = max(futur)
            age_from_creation_max = max(age_from_creation)
            result.append([frequency_quartiles, frequency_max, age_from_creation_quartiles,age_from_creation_max, futur_quartiles, futur_max, current_index])
            frequency = []
            age_from_creation = []
            futur = []
            h = 0
            current_index = int(tx[0])
            y = 0
        #print(tx[1])
        #print(tx[1][1:-1])
        #print(tx[1][2:-2])
        try:
            frequency.append(float(data.get(int(tx[1][1:-1],0))[1])/window)
            age_from_creation.append(abs(current_index - int(data.get(int(tx[1][1:-1],0))[4]))//window)
            futur.append(abs(int(data.get(int(tx[1][1:-1],0))[5]) - current_index)//window)
            h += 1
        except:
            z = 0
        """ try:
            frequency.append(float(data.get(tx[2])[1]))
            age_from_creation.append(abs(current_index*100000 - int(data.get(tx[2])[4])//100000))
            futur.append(abs(int(data.get(tx[2])[5])//100000 - current_index*100000))
            h += 1
        except:
            z = 0 """
        y += 1
    frequency_values = np.array(frequency)
    age_from_creation__values = np.array(age_from_creation)
    futur_centrality_values = np.array(futur)
    frequency_quartiles = np.percentile(frequency_values, [25, 50, 75])
    age_from_creation_quartiles = np.percentile(age_from_creation__values, [25, 50, 75])
    futur_quartiles = np.percentile(futur_centrality_values, [25, 50, 75])
    frequency_max = max(frequency)
    futur_max = max(futur)
    age_from_creation_max = max(age_from_creation)
    result.append([frequency_quartiles, frequency_max, age_from_creation_quartiles,age_from_creation_max, futur_quartiles, futur_max, current_index])
    return result


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/account_frequency_age.csv"
    save_file = dir_path + "/../Data/ProcessedData/account_frequency_timeToFirst_timeToLast.txt"
    tx_file = dir_path + "/../Data/ProcessedData/transaction_order"
    nb_core = 8
    account_dir = {}
    print("set up")
    with open(data_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        #Collecting all data
        k = 0
        for row in csvreader:
            if (k+1) % nb_core == 0:
                k = 0
            account_dir[int(row[0])] = row
            k += 1
    multiprocessing.freeze_support()

    dir_list = os.listdir(tx_file)
    tmp_list = [int(dir_list[i].split(".")[0]) for i in range(len(dir_list))]
    dir_list = sorted(tmp_list)
    i = 0
    index_list = []
    input_set = []
    k = 0
    with open(save_file, 'w') as output_file:
        line = "index" + "," +"frequency_1"  + "," +"frequency_2"  + "," +"frequency_3" + "," +"frequency_max" + "," +"age_from_creation_1" + "," +"age_from_creation_2" + "," +"age_from_creation_3"+ "," +"age_from_creation_max" + "," +"futur_1" + "," +"futur_2" + "," +"futur_3" + "," +"futur_max" + "\n"
        output_file.writelines(line)
        output_file.close()
    print("processing")
    for file in dir_list:
        file = tx_file + "/" + str(file) + ".csv"
        print("file:",file)
        if file.split(".")[-1] == "csv":
            if k == nb_core:
                account_list = [account_dir for j in range(nb_core)]
                arg_tuples = zip(input_set, account_list, index_list)
                with multiprocessing.Pool(processes=nb_core) as pool: 
                    results = pool.starmap(freq, arg_tuples)
                with open(save_file, 'a') as output_file:
                    for x in results:
                        for result in x:
                            line = str(result[-1])
                            for y in range(len(result)-1):
                                if isinstance(result[y], np.ndarray):
                                    for item in result[y]:
                                        line += "," + str(item)
                                else:
                                    line += "," + str(result[y])
                            line += "\n"
                            output_file.writelines(line)
                output_file.close()
                input_set = []
                index_list = []
                k = 0
                print("----- Finsh:",i,"/",len(dir_list)," -----")
            input_set.append(file)
            index_list.append(i*10)
            k += 1
        i += 1
    account_list = [account_dir for _ in range(nb_core)]
    arg_tuples = zip(input_set, account_list, index_list)
    with multiprocessing.Pool(processes=nb_core) as pool: 
        results = pool.starmap(freq, arg_tuples)
    with open(save_file, 'a') as output_file:
        for x in results:
            for result in x:
                line = str(result[-1])
                for y in range(len(result)-1):
                    for item in result[y]:
                        line += "," + str(item)
                line += "\n"
                output_file.writelines(line)
        output_file.close()

if __name__ == "__main__":
   main()