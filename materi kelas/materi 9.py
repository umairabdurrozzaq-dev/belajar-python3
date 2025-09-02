print("------->MATERI KE 9<---------")
# faction tidak akn di eksekusi jika tidak di panggil
def say_hello(name):
# print("hello mr.", name)
# kasih f diawal string untuk mengisikan fariabel / sparameter
   print(f"hello mr.,{name}")
   print("baek baek aje")
# lambda untuk menulis fungsi nyang ringkas dgn 1 baris
# sering disebut juga funsi anonim(tanpa nama)
say_hello_mini = lambda name: print(f"hello mr.{name}")
# fungsi nya dibawah sini
say_hello("rozak")
say_hello("maer")
print("---------")
say_hello_mini("ari")
say_hello_mini("untung")


#  contoh penerapan lambda dgn higner-order fuction
#  map(), ---sorted()---filter()
jajan_mingguan = [50000, 20000, 70000, 80000]
# sorted -> mengurutkan data 
urutkan_uang = sorted(jajan_mingguan)
print(f"urutkan uang: {urutkan_uang}")
urutkan_uang_terbalik = sorted (jajan_mingguan, reverse=True)
print(f"urutkan uang terbalik: {urutkan_uang_terbalik}")

# map()-> mentrasformasi data
kurangi_uang = map(lambda uang: uang - 500, jajan_mingguan)
# list mengubah data objek map menjadi berikut list
list_kurangi_uang = list(kurangi_uang)
print(f"map uang berkurang: {list_kurangi_uang}")

# filter() -> menyaring / memfilter data
jajan_banyak = filter(lambda uang: uang >= 2000, jajan_mingguan )
list_jajan_banyak = list(jajan_banyak)
print(f"filter jajan diatas 20rb: {list_jajan_banyak}")


