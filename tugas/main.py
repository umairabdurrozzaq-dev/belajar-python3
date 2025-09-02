import csv

file_path = r"C:\python\csv\data.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv. reader(file_baru)
    list_red = list(read)

    print("semua data")
    print("-" * 20)
    for baris in list_red:
        no = baris[0]
        nama = baris[1]
        kelas = baris[2]

        print(f"{no} | {nama} | {kelas}")
        
with open(file_path, 'a', newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["5", "udin", "8"])



                    