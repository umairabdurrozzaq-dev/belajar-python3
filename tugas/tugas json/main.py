import json
file_path = r"c:\python\belajar python3\tugas\tugas json\peminjaman buku.json"
with open(file_path, "r") as f:
    data = json.load(f)


total_dipinjam = 0
total_belum_kembali = 0

print("Buku yang belum kembali")
for anggota in data["anggota"]:
    for buku in anggota["pinjam"]:
        total_dipinjam += 1
        if not buku['kembali']:
           total_belum_kembali += 1
           print(f"- {anggota['nama']} : {buku['judul']} ({buku['tanggal']})")
           print(f"total kembali :")

print("\nRingkasan : ")
print(f"Total dipinjam: {total_dipinjam}")
print(f"Total belum kembali: {total_belum_kembali}")
