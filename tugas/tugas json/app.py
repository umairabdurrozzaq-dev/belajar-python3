import requests

url_arab = "https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
url_eng  = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"

# Ambil text arab 
data_arab = requests.get(url_arab).json()
text_arab = data_arab["data"]["text"]

# Ambil terjemahan B.inggris
data_eng = requests.get(url_eng).json()
text_eng = data_eng["data"]["text"]
print ("-"*80)
print ("Surah Al -Baqoroh ayat : 25 (Ayat kursi)")
print ("-"*80)
print (text_arab)
print ("-"*80)
print ("Artinya :")
print (text_eng)