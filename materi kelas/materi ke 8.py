# function diawli dgn keybord 'def'
def hello():
    print("helo ngab")
    print("helo juga bang")

print("coba in fungsinya")

hello

#function dngan parameter nama
def sapa(nama):
    print("hello bang", nama)
    print("apa kabar", nama)
    print("=================")


sapa("umair")
sapa("firanda")
sapa("juna")

# fungsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    print("> panjang: ",panjang)
    print("> lebar ",lebar)
    rumus = panjang * lebar
    print("luas persegi panjang:= ",rumus)

luas_persegi_panjang(45,56)
luas_persegi_panjang(30,32)

def luaslingkaran(phi, jarijari):
    print("> phi =",phi)
    print("> pi =",jarijari)
    rumus = phi * jarijari * jarijari
    print("=============================")
    print("luas lingkaran nya adalah: ", rumus)
luaslingkaran(3.16, 17)


