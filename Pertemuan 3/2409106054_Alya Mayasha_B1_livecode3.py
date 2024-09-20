cuaca = "cerah"
if cuaca == "cerah":
    print("pergi ke luar")
uang = 0
if uang:
    print("pergi ke pasar")
else :
    print("pergi ke rumah teman")

# variabel akan bernilai false jika string kosong
nilai = 70
if nilai <70:
    print("tidak lulus")
else :
    print("lulus")
if nilai < 0:
    print("bialngan negatif")
else :
    print("bilangan positif")
umur = int(input("masukkan umur anda"))

if umur <= 10:
    print("anak anak")
elif umur <= 18:
    print("remaja")
elif umur <= 35:
    print("dewasa")
elif umur <= 65:
    print("paruh baya")
else:
    print("tua")
if nilai >= 80:
    if nilai >= 85:
        print("nilai A+")
    else :
        print("nilai A-")
else:
    print("tidak lulus")

print("1. nonton film")
print("2. ngoding")
print("3. keluar")

menu = int(input("masukkan pilihan anda"))

if menu == 1:
   print("sedang nonton film")
elif menu == 2:
   print("sedang ngoding")
elif menu == 3:
    print("keluar dari aplikasi")
else:
    print("menu tidak tersedia")
angka = 10
#perkondisian pertama
if angka % 2 == 0:
    print("genap")
if angka > 0:
    print("positif")

#perkondisian kedua
if angka % 2 == 0:
    print("genap")
elif angka > 0:
    print("positif")



