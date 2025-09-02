import json
# tambahkan modul json dgn import
print("materi 12- json file hendling")
print("-----RED JSON-----")
file_path_json = r"C:\python\materi kelas\materi.json"
with open(file_path_json, "r") as file_materi:
    data_materi = json.load(file_materi)
# akses data json dgn 'key' nya
       
print(f"judul berkas: {data_materi['title']}")
print(f"total kelas A: {data_materi['total']}")
print(f"status_santri: {data_materi['status_santri']}")
print(f"status_lulus: {data_materi['status_lulus']}")
print(f"pelajaran: {data_materi['pelajaran']}")
# eksatra data list dng for loop
for pelajaran in data_materi['pelajaran']:
    print(f"--->{pelajaran}")
# keys suroh: no, nama, ayat, turun
print("-" * 50)# gandakan simbol perkalian
print("| no  | nama | ayat | turun | ")
print("-" * 50)
for surah in data_materi['surah']:
    print(f"->{surah['no']} | {surah['nama']} | {surah['ayat']} |  {surah['turun']} |")