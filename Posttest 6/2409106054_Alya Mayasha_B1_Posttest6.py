import os
schedule_dokter = {
    "nama_dokter" : [
        "dr. chae song hwa Sp.Bs.", 
        "dr. lee ik jun Sp.B.",
        "dr. kim jun wan Sp.BTKV",
        "dr. yang seok hyung Sp.OG.",
        "dr. andrea Sp.A."
    ],
    "nama_praktik" : [
        "spesialis saraf",
        "spesialis bedah umum",
        "spesialis bedah jantung",
        "spesialis kandungan",
        "spesialis anak"
    ],
    "hari_praktik" : [
        "senin",
        "rabu",
        "selasa",
        "jumat",
        "sabtu"
    ],
    "jam_praktik" : [
        "13.00-16.30",
        "09.00-12.00",
        "12.00-16.00",
        "13.30-17.00",
        "08.00-11.30"
    ],
    "jenis_operasi" : [
        "kraniotomi (bedah otak)",
        "biopsi payudara",
        "implan alat pacu jantung",
        "pengangkatan rahim",
        "obstruksi usus"
    ],
    "tanggal_operasi" : [
        "07/10/2024",
        "10/10/2024",
        "11/10/2024",
        "15/10/2024",
        "08/10/2024"
    ]
}
os.system('cls || clear')

while True:
    print("\n========== Jadwal Dokter RS YULJE ==========")
    print("1. Lihat Jadwal Praktik dan Operasi Dokter")
    print("2. Tambah Jadwal Dokter")
    print("3. Perbarui Jadwal Operasi Dokter")
    print("4. Hapus Jadwal Operasi Dokter")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan menu Anda: ")
    os.system('cls || clear')
    
    if pilihan == "1" : 
            print("========Lihat Jadwal Dokter========")
            for i in range(len(schedule_dokter["nama_dokter"])) :
                print(f"data ke {i+1}")
                print(f"Nama dokter : {schedule_dokter['nama_dokter'][i]}")
                print(f"Nama praktik : {schedule_dokter['nama_praktik'][i]}")
                print(f"Hari praktik : {schedule_dokter['hari_praktik'][i]}")
                print(f"Jam praktik : {schedule_dokter['jam_praktik'][i]}")
                print(f"Jenis operasi : {schedule_dokter['jenis_operasi'][i]}")
                print(f"Tanggal operasi : {schedule_dokter['tanggal_operasi'][i]}")
                print("="*40)
            input("Enter untuk kembali memilih menu")    
            os.system('cls || clear')    
    elif pilihan == "2" :
         print("========Tambah Jadwal Dokter========")
         inputdokter = input("Masukkan nama dokter yang ingin Anda tambahkan: ")
         inputpraktik = input("Masukkan jenis praktik dokter yang ingin Anda tambahkan: ")
         inputhari = input("Masukkan hari praktik yang ingin Anda tambahkan: ")
         inputjam = input("Masukkan jam praktik yang ingin Anda tambahkan: ")
         inputoperasi = input("Masukkan jenis operasi yang ingin Anda tambahkan: ")
         inputtgloperasi = input("Masukkan tanggal operasi yang ingin Anda tambahkan: ")
         schedule_dokter['nama_dokter'].append(inputdokter)
         schedule_dokter['nama_praktik'].append(inputpraktik)
         schedule_dokter['hari_praktik'].append(inputhari)
         schedule_dokter['jam_praktik'].append(inputjam)
         schedule_dokter['jenis_operasi'].append(inputoperasi)
         schedule_dokter['tanggal_operasi'].append(inputtgloperasi)
         os.system('cls||clear')
         print(f"Nama Dokter : {inputdokter}")
         print(f"Praktik : {inputpraktik}")
         print(f"Hari Praktik : {inputhari}")
         print(f"Jam Praktik : {inputjam}")
         print(f"Jenis Operasi : {inputoperasi}")
         print(f"Tanggal Pelaksanaan OP : {inputtgloperasi} ")
         print(f"jadwal {inputdokter} berhasil ditambahkan")
         input("Enter untuk kembali memilih menu")
         os.system('cls || clear')
    elif pilihan == "3" :
         print("========Perbarui Jadwal Operasi Dokter========")
         index = int(input("Masukkan index jenis operasi dan tanggal operasi yang ingin diperbarui: "))
         if 0 <= index < len(schedule_dokter['jenis_operasi']) :
              operasi_baru = input("Masukkan jenis operasi yang baru: ")
              schedule_dokter['jenis_operasi'][index]=operasi_baru
              tgloperasi_baru = input("Masukkan tanggal operasi yang baru: ")
              schedule_dokter['tanggal_operasi'][index]=tgloperasi_baru
              print(f"Jenis Operasi {schedule_dokter['nama_dokter'][index]} {schedule_dokter['jenis_operasi'][index]} tanggal {schedule_dokter['tanggal_operasi'][index]}")
              print("Jadwal operasi berhasil diperbarui")
         else:
              print("index tidak valid")
         input("Enter untuk kembali memilih menu")
         os.system('cls || clear')
    elif pilihan == "4" :
         print("========Hapus Jadwal Operasi Dokter========")
         index = int(input("Masukkan index jenis operasi dan tanggal operasi yang ingin dihapus: "))
         if 0 <= index < len(schedule_dokter['jenis_operasi']):
              del_operasi = schedule_dokter['jenis_operasi'].pop(index)
              del_tgloperasi = schedule_dokter['tanggal_operasi'].pop(index)
              print(schedule_dokter['jenis_operasi'])
              print(schedule_dokter['tanggal_operasi'])
              print(f"Jadwal operasi {del_operasi} pada {del_tgloperasi} telah dihapus")
         else:
              print("index tidak valid")
         input("Enter untuk kembali memilih menu")
         os.system('cls || clear')
    elif pilihan == "5" :
         print("Anda memilih menu 5")
         print("Keluar Program")
         exit()
         os.system('cls || clear')
    else:
         print(f"menu {pilihan} tidak tersedia")
         input("Enter untuk memilih menu")
         os.system('cls || clear')