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
def clear_screen():
    os.system('cls || clear')

clear_screen()
def tampilkan_jadwal():
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

def tambah_jadwal(nama_dokter, jenis_praktik, hari_praktik, jam_praktik, jenis_operasi, tanggal_operasi):
     schedule_dokter['nama_dokter'].append(nama_dokter)
     schedule_dokter['nama_praktik'].append(jenis_praktik)
     schedule_dokter['hari_praktik'].append(hari_praktik)
     schedule_dokter['jam_praktik'].append(jam_praktik)
     schedule_dokter['jenis_operasi'].append(jenis_operasi)
     schedule_dokter['tanggal_operasi'].append(tanggal_operasi)
     return f"Jadwal {nama_dokter} berhasil ditambahkan."

def perbarui_jadwal(index):
     if 0 <= index < len(schedule_dokter['jenis_operasi']) :
           operasi_baru = input("Masukkan jenis operasi yang baru: ")
           schedule_dokter['jenis_operasi'][index]=operasi_baru
           tgloperasi_baru = input("Masukkan tanggal operasi yang baru: ")
           schedule_dokter['tanggal_operasi'][index]=tgloperasi_baru
           return f"Jenis Operasi {schedule_dokter['nama_dokter'][index]} {schedule_dokter['jenis_operasi'][index]} tanggal {schedule_dokter['tanggal_operasi'][index]} berhasil diperbarui."
     else:
           return f"index tidak valid."

def hapus_jadwal(index):
     if 0 <= index < len(schedule_dokter['jenis_operasi']):
           del_operasi = schedule_dokter['jenis_operasi'].pop(index)
           del_tgloperasi = schedule_dokter['tanggal_operasi'].pop(index)
           print(schedule_dokter['jenis_operasi'])
           print(schedule_dokter['tanggal_operasi'])
           print(f"Jadwal operasi {del_operasi} pada {del_tgloperasi} telah dihapus.")
     else:
           print(f"index tidak valid.") 
     
     
while True:
    print("\n========== Jadwal Dokter RS YULJE ==========")
    print("1. Lihat Jadwal Praktik dan Operasi Dokter")
    print("2. Tambah Jadwal Dokter")
    print("3. Perbarui Jadwal Operasi Dokter")
    print("4. Hapus Jadwal Operasi Dokter")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan menu Anda: ")
    clear_screen()
    
    if pilihan == "1" : 
            tampilkan_jadwal()
            input("Enter untuk kembali memilih menu")    
            clear_screen()    
    elif pilihan == "2" :
         print("========Tambah Jadwal Dokter========")
         inputdokter = input("Masukkan nama dokter yang ingin Anda tambahkan: ")
         inputpraktik = input("Masukkan jenis praktik dokter yang ingin Anda tambahkan: ")
         inputhari = input("Masukkan hari praktik yang ingin Anda tambahkan: ")
         inputjam = input("Masukkan jam praktik yang ingin Anda tambahkan: ")
         inputoperasi = input("Masukkan jenis operasi yang ingin Anda tambahkan: ")
         inputtgloperasi = input("Masukkan tanggal operasi yang ingin Anda tambahkan: ")
         print(tambah_jadwal(inputdokter, inputpraktik, inputhari, inputjam, inputoperasi, inputtgloperasi))
         input("Enter untuk kembali memilih menu")
         clear_screen()
    elif pilihan == "3" :
         print("========Perbarui Jadwal Operasi Dokter========")
         index = int(input("Masukkan index jenis operasi dan tanggal operasi yang ingin diperbarui: "))
         print(perbarui_jadwal(index))
         input("Enter untuk kembali memilih menu")
         clear_screen()
    elif pilihan == "4" :
         print("========Hapus Jadwal Operasi Dokter========")
         index = int(input("Masukkan index jenis operasi dan tanggal operasi yang ingin dihapus: "))
         (hapus_jadwal(index))
         input("Enter untuk kembali memilih menu")
         clear_screen()
    elif pilihan == "5" :
         print("Anda memilih menu 5")
         print("Keluar Program")
         exit()
         clear_screen()
    else:
         print(f"menu {pilihan} tidak tersedia")
         input("Enter untuk memilih menu")
         clear_screen()