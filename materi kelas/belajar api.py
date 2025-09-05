
import requests

# 1. Panggil API
url = "https://api.aladhan.com/v1/timingsByCity?city=Jakarta&country=Indonesia&method=2"
response = requests.get(url)

# 2. Ubah hasil ke format JSON (jadi dictionary Python)
data = response.json()

# 3. Ambil bagian tertentu (jadwal sholat)
jadwal = data['data']['timings']

# 4. Tampilkan hasil
print("=== Jadwal Sholat Jakarta ===")
print(f"Subuh    : {jadwal['Fajr']}")
print(f"Dhuhur   : {jadwal['Dhuhr']}")
print(f"Ashar    : {jadwal['Asr']}")
print(f"Maghrib  : {jadwal['Maghrib']}")
print(f"Isya     : {jadwal['Isha']}")
