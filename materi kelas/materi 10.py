import csv
print("--materi 10--")
print("--------------------------")
# buka file
file_pesan = open(r"C:\python\materi kelas\pesan.txt", "r")
# baca isi file
isi_pesan = file_pesan.read()
# tampilkan output isi pesan
print(f"ISI PESAN --> {isi_pesan}")
# tuup file
file_pesan.close()

print("------proyek------")

file_jajan = open(r"C:\python\materi kelas\jajan.csv", "r")
isi_tabel = file_jajan.read()
print(f"---ISI TABEL--->{isi_tabel}")
file_jajan.close()

print("---->append csv file<----")
jajan_baru = [4,"rozak",100000]
print(f"jajan baru: {jajan_baru}")
file_path_csv = r"C:\python\materi kelas\jajan.csv"
with open(file_path_csv, "a", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    writer.writerow(jajan_baru)

# GABUNG SAMA NATERI 11
print("materi 11 - file hendling part 2")
print("-----updet csv-------------")
file_path_csv = r"C:\python\materi kelas\jajan.csv"
data_jajan = []
with open(file_path_csv, "r") as file_jajan:
    isi_tabel_jajan = csv.reader(file_jajan)
    for item_jajan in isi_tabel_jajan:
        print(item_jajan)
        data_jajan.append(item_jajan)


# 2. mengubah atau membuat data baru
for baris in data_jajan:
    print(baris)
    if baris[1] == "juna":
        uang = 15000
        baris[2] = uang
        print(f"data ditemukan, ganti uang jajan{uang}")
    print("------loop end------")

# 3. hapus data dimlist index
del data_jajan[3]
print(f"data jajan terkini: {data_jajan}")

# 4. tulis ulang data dng mode "w -> writer
with open(file_path_csv, "w", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    writer.writerows(data_jajan)

