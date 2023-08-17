#!/usr/bin/python
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = dir_path + "/../Data/ProcessedData/last_use_vector.txt"
    print("start up")
    with open(data_file, 'r') as txt_files:
        i = 0
        data = []
        for line in txt_files:
            data.append(line.split(","))
    result = [0]
    index = [0]
    print("launch")
    tmp = 0
    
    for account in data:
        tmp = float(account[0])
        print(i,"/",len(data))
        result.append(tmp)
        index.append((i/len(data))*100 )
        i += 1
#Scatter plot

    print("create tab")
    one_use_low_last_use = 0
    one_use_high_last_use = 0
    several_use_low_last_use = 0
    bad_locality = 0
    nb_account = 0
    for x in data:
        if float(x[1]) > 1:
            nb_account += 1
            if int(x[1]) <= 5:
                if float(x[2]) < 5:
                    one_use_low_last_use += 1
                else:
                    one_use_high_last_use += 1

            else:
                if float(x[2]) < 5:
                    several_use_low_last_use += 1
                else:
                    bad_locality += 1
    
    print("one_use_low_last_use:", one_use_low_last_use, " ", (one_use_low_last_use/nb_account)*100,"%")
    print("one_use_high_last_use:", one_use_high_last_use, " ", (one_use_high_last_use/nb_account)*100,"%")
    print("several_use_low_last_use:", several_use_low_last_use, " ", (several_use_low_last_use/nb_account)*100,"%")
    print("bad_locality:", bad_locality, " ", (bad_locality/nb_account)*100,"%")

if __name__ == "__main__":
   main()