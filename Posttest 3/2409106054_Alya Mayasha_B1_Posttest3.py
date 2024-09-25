print("==================================================================")
print("  Menu Program Menghitung Luas Permukaan dan Volume Bangun Ruang  ")
print("==================================================================")
print("1. Luas permukaan kubus")
print("2. Volume kubus")
print("3. Luas permukaan tabung")
print("4. Volume tabung")
print("5. Luas permukaan bola")
print("6. Volume bola")
print("7. Keluar dari program")

Menu = int(input("Silakan masukkan pilihan yang akan anda pilih :"))
if Menu == 1:
    SisiKubus = float(input("Masukkan panjang sisi kubus (dalam cm) :"))
    LuasPermukaanKubus = 6*SisiKubus**2
    print(f"Luas permukaan kubus dengan panjang sisi {SisiKubus} cm adalah {LuasPermukaanKubus} cm^2")
elif Menu == 2:
    SisiKubus = float(input("Masukkan panjang sisi kubus (dalam cm) :"))
    VolumeKubus = SisiKubus**3
    print(f"Volume kubus dengan panjang sisi {SisiKubus} cm adalah {VolumeKubus} cm^3")
elif Menu == 3:
    RadiusTabung = float(input("Masukkan radius tabung (dalam cm) :"))
    TinggiTabung = float(input("Masukkan tinggi tabung (dalam cm) :"))
    LuasPermukaanTabung = 2*3.14*RadiusTabung*(RadiusTabung+TinggiTabung)
    print(f"Luas permukaan tabung dengan radius {RadiusTabung} cm dan tinggi {TinggiTabung} cm adalah {LuasPermukaanTabung} cm^2")
elif Menu == 4:
    RadiusTabung = float(input("Masukkan radius tabung (dalam cm) :"))
    TinggiTabung = float(input("Masukkan tinggi tabung (dalam cm) :"))
    VolumeTabung = 3.14*RadiusTabung**2*TinggiTabung
    print(f"Volume tabung dengan radius {RadiusTabung} cm dan tinggi {TinggiTabung} cm adalah {VolumeTabung} cm^3")
elif Menu == 5:
    RadiusBola = float(input("Masukkan radius bola (dalam cm) :"))
    LuasPermukaanBola = 4*3.14*RadiusBola**2
    print(f"Luas permukaan bola dengan radius {RadiusBola} cm adalah {LuasPermukaanBola} cm^2")
elif Menu == 6:
    RadiusBola = float(input("Masukkan radius bola (dalam cm) :"))
    VolumeBola = 4/3*3.14*RadiusBola**3
    print(f"Volume bola dengan radius {RadiusBola} cm adalah {VolumeBola} cm^3")
elif Menu == 7:
    print("Keluar dari program")
else:
    print("Menu tidak valid")


     
    