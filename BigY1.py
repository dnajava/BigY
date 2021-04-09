__author__ = "Ilpo Kantonen"
__date__ = "$9.4.2021 21:11:00$"

from csv import reader

def handleBigY(fname_p: str):
    r, v = 0, 0
    try:
        with open(fname_p, 'r') as read_obj:
            csv_reader = reader(read_obj)
            for k in csv_reader:
                r += 1
                if k[6] == "?":
                    v += 1
    except (IOError, OSError) as err:
        print(err)
    finally:
        if read_obj is not None:
            read_obj.close()
    ret = (r, v)
    return ret

if __name__ == '__main__':
    path = '/path/to/download/directory/'
    files = ['KIT1_BigY_Data_20210408.csv', 'KIT2_BigY_Data_20210408.csv']

    for f in files:
        filen = path + f
        result = handleBigY(filen)
        print(result[0], 'lines, which', result[1], 'are not clear. Percentage ', 100 * result[1] / result[0] )
