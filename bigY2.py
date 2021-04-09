__author__ = "Ilpo Kantonen"
__date__ = "$9.4.2021 22:24:00$"

from csv import reader

def make_dictionary(fname_p: str):
    tmp_dict = {"A": 0, "T": 0, "C": 0, "G": 0, "?": 0, "TOT": 0}
    r, v = 0, 0
    try:
        with open(fname_p, 'r') as read_obj:
            csv_reader = reader(read_obj)
            for k in csv_reader:
                r += 1
                if k[6] == "A":
                    tmp_dict["A"] += 1
                elif k[6] == "T":
                    tmp_dict["T"] += 1
                elif k[6] == "C":
                    tmp_dict["C"] += 1
                elif k[6] == "G":
                    tmp_dict["G"] += 1
                elif k[6] == "?":
                    tmp_dict["?"] += 1
                tmp_dict["TOT"] += 1
    except (IOError, OSError) as err:
        print(err)
    finally:
        if read_obj is not None:
            read_obj.close()
    return tmp_dict

if __name__ == '__main__':
    path = '/home/sda4/Lataukset/'
    files = ['KIT1_BigY_Data_20210408.csv', 'KIT2_BigY_Data_20210408.csv']

    for f in files:
        filen = path + f
        dic = make_dictionary(filen)
        for di in dic:
            print(di, dic[di], 'pieces and percentage', 100 * dic[di] / dic["TOT"])
            print()
