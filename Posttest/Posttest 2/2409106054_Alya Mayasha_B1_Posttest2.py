nama = input("masukan nama anda : ")
tinggibadan = float(input("masukan tinggi badan anda (dalam cm) :"))
beratbadan = float(input("masukkan berat badan anda (dalam kg) :") )
umur = int(input("masukkan umur anda:"))
programstudi = input ("masukkan program studi anda: ")
jeniskelamin_input = input("masukkan gender (perempuan/lakilaki): ").strip().lower()
if jeniskelamin_input == "perempuan" :
    jeniskelamin = True
if jeniskelamin_input == "lakilaki" :
    jeniskelamin = False

total = tinggibadan + beratbadan 

print("====================================================")
print("                  Bio Data Anda                     ")
print("====================================================")

if jeniskelamin :
    print(f"Nama                             : {nama}")
    print("jenis Kelamin                    : perempuan")
else :
    print(f"Nama                             : {nama}")
    print("jenis Kelamin                    : lakilaki")

print(f"Tinggi Badan                     : {tinggibadan} cm")
print(f"Berat Badan                      : {beratbadan} kg ")
print(f"Umur                             : {umur} tahun")
print(f"Program Studi                    : {programstudi}")
print(f"Total Tinggi Badan + Berat Badan : {total}")
