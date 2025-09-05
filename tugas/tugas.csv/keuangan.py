import csv

file_path = r"C:\python\csv\keuangan.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_red = list(read)

    print("semua data")
    print("-" * 20)
    for baris in list_red:
        tanggal = baris[0]
        keterangan = baris[1]
        katagori = baris[2]
        jumlah = baris[3]

        print(f"{tanggal} | {keterangan} | {katagori} | {jumlah}")
        