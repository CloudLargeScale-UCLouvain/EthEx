import os


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
            nb_trans = len(tmp_int_trans)
            tmp_last_use = []
            vector = 0
            if nb_trans <= 1:
                last_use = 0
                vector = 0
            else:
                for i in range(len(tmp_int_trans)-1):
                    tmp_last_use.append(tmp_int_trans[i+1] - tmp_int_trans[i])
                last_use = sum(tmp_last_use)/nb_trans
                if last_use <= 0:
                    vector = 0
                else:
                    vector = nb_trans*last_use
            account_data.append([vector, nb_trans, last_use])
        account_data = sorted(account_data, key=lambda x: x[0])
        with open(dir_path + "/../Data/ProcessedData/last_use_vector.txt", 'a') as txt_files:
            for x in account_data:
                line = str(x[0]) + "," + str(x[1]) + "," + str(x[2])+ "\n"
                txt_files.write(line)


if __name__ == "__main__":
   main() 