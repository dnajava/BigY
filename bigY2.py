__author__ = "Ilpo Kantonen"
__date__ = "$10.4.2021 02:08:00$"

from csv import reader

def make_dictionary(fname_p: str):
    tmp_dict = {"A": 0, "T": 0, "C": 0, "G": 0, "?": 0, "TOTAL": 0}
    r, v = 0, 0
    try:
        with open(fname_p, 'r') as read_obj:
            csv_reader = reader(read_obj)
            for k in csv_reader:
                r += 1
                if r == 1:
                    continue
                tmp_dict["TOTAL"] += 1
                if k[6] in tmp_dict.keys():
                    tmp_dict[k[6]] += 1
                else:
                    tmp_dict[k[6]] = 1
    except (IOError, OSError) as err:
        print(err)
    finally:
        if read_obj is not None:
            read_obj.close()
    if tmp_dict["TOTAL"] > 0:
        tmp_dict["TOTAL"] -= 1                  # Remove first header line from count
    return tmp_dict

if __name__ == '__main__':
    path = '/path/to/download/directory/'
    files = ['KIT1_BigY_Data_YYYYMMDD.csv', 'KIT2_BigY_Data_YYYYMMDD.csv']

    for f in files:
        filen = path + f
        dic = make_dictionary(filen)
        if (dic["TOTAL"] > 0):
            for di in dic:
                if di != "TOTAL":
                    print(di, dic[di], 'pieces and percentage', 100 * dic[di] / dic["TOTAL"])
            print('TOTAL', dic["TOTAL"], 'pieces and percentage', 100 * dic[di] / dic["TOTAL"])
        else:
            print('There were no A, G, C, T or such in Big Y csv file!')
        print()
