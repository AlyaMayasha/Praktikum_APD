import os
schedule_dokter = {}
nama_dokter =["dr. chae song hwa Sp.BS.", "dr. lee ik jun Sp.B.", "dr. kim jun wan Sp.BTKV", "dr. yang seok hyung Sp.OG.", "dr. andrea Sp.A."]
nama_praktik =["spesialis saraf", "spesialis bedah umum", "spesialis bedah jantung", "spesialis kandungan", "spesialis anak"]
hari_praktik = ["senin", "rabu", "selasa", "jumat", "sabtu"]
jam_praktik = ["13.00-16.30", "09.00-12.00", "12.00-16.00", "13.30-17.00", "08.00-11.30"]
jenis_operasi = ["kraniotomi (bedah otak)", "biopsi payudara", "implan alat pacu jantung", "pengangkatan rahim", "obstruksi usus"]
tanggal_operasi = ["07/10/2024","10/10/2024", "11/10/2024", " 15/10/2024", "08/10/2024"]
os.system('cls || clear')

while True:
    print("\n========== Jadwal Dokter RS YULJE ==========")
    print("1. Lihat Jadwal Praktik dan Operasi Dokter")
    print("2. Tambah Jadwal Dokter")
    print("3. Perbarui Jadwal Operasi Dokter")
    print("4. Hapus Jadwal Operasi Dokter")
    print("5. Keluar")
    pilih = input("Masukkan pilihan menu Anda: ")
    os.system('cls || clear')
    match (pilih):
          case "1":
                print("========Lihat Jadwal Dokter========")
                index = 0
                print(f"Nama Dokter : {nama_dokter [index]}")
                print(f"Praktik : {nama_praktik [index]}")
                print(f"Hari Praktik : {hari_praktik [index]}")
                print(f"Jam Praktik : {jam_praktik [index]}")
                print(f"Jenis Operasi : {jenis_operasi [index]}")
                print(f"Tanggal Pelaksanaan OP : {tanggal_operasi [index]}")
                print(f"="*30)

                index = 1
                print(f"Nama Dokter : {nama_dokter [index]}")
                print(f"Praktik : {nama_praktik [index]}")
                print(f"Hari Praktik : {hari_praktik [index]}")
                print(f"Jam Praktik : {jam_praktik [index]}")
                print(f"Jenis Operasi : {jenis_operasi [index]}")
                print(f"Tanggal Pelaksanaan OP : {tanggal_operasi [index]}")
                print(f"="*30)

                index = 2
                print(f"Nama Dokter : {nama_dokter [index]}")
                print(f"Praktik : {nama_praktik [index]}")
                print(f"Hari Praktik : {hari_praktik [index]}")
                print(f"Jam Praktik : {jam_praktik [index]}")
                print(f"Jenis Operasi : {jenis_operasi [index]}")
                print(f"Tanggal Pelaksanaan OP : {tanggal_operasi [index]}")
                print(f"="*30)

                index = 3
                print(f"Nama Dokter : {nama_dokter [index]}")
                print(f"Praktik : {nama_praktik [index]}")
                print(f"Hari Praktik : {hari_praktik [index]}")
                print(f"Jam Praktik : {jam_praktik [index]}")
                print(f"Jenis Operasi : {jenis_operasi [index]}")
                print(f"Tanggal Pelaksanaan OP : {tanggal_operasi [index]}")
                print(f"="*30)

                index = 4
                print(f"Nama Dokter : {nama_dokter [index]}")
                print(f"Praktik : {nama_praktik [index]}")
                print(f"Hari Praktik : {hari_praktik [index]}")
                print(f"Jam Praktik : {jam_praktik [index]}")
                print(f"Jenis Operasi : {jenis_operasi [index]}")
                print(f"Tanggal Pelaksanaan OP : {tanggal_operasi [index]}")
                print(f"="*30)
                input("Enter untuk kembali memilih menu")
                os.system('cls || clear')

          case "2":
            print("========Tambah Jadwal Dokter========")
            inputdokter = input("Masukkan nama dokter yang ingin Anda tambahkan: ")
            inputpraktik = input("Masukkan jenis praktik dokter yang ingin Anda tambahkan: ")
            inputhari = input("Masukkan hari praktik yang ingin Anda tambahkan: ")
            inputjam = input("Masukkan jam praktik yang ingin Anda tambahkan: ")
            inputoperasi = input("Masukkan jenis operasi yang ingin Anda tambahkan: ")
            inputtgloperasi = input("Masukkan tanggal operasi yang ingin Anda tambahkan: ")
            nama_dokter.append(inputdokter)
            nama_praktik.append(inputpraktik)
            hari_praktik.append(inputhari)
            jam_praktik.append(inputjam)
            jenis_operasi.append(inputoperasi)
            tanggal_operasi.append(inputtgloperasi)
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
          case "3" :
              print("========Perbarui Jadwal Operasi Dokter========")
              index = int(input("Masukkan index jenis operasi dan tanggal operasi yang ingin diperbarui: "))
              operasi_baru = input("Masukkan jenis operasi yang baru: ")
              jenis_operasi[index]=operasi_baru
              tgloperasi_baru = input("Masukkan tanggal operasi yang baru: ")
              tanggal_operasi[index]=tgloperasi_baru
              print(f"Jenis Operasi {nama_dokter[index]} {jenis_operasi[index]} tanggal {tanggal_operasi[index]}")
              print("Jadwal operasi berhasil diperbarui")
              input("Enter untuk kembali memilih menu")
              os.system('cls || clear')
          case "4" :
            print("========Hapus Jadwal Operasi Dokter========")
            index = int(input("Masukkan index jenis operasi dan tanggal operasi yang ingin dihapus: "))
            del_operasi = jenis_operasi.pop(index)
            del_tgloperasi = tanggal_operasi.pop(index)
            print(jenis_operasi)
            print(tanggal_operasi)
            print(f"Jadwal operasi {del_operasi} pada {del_tgloperasi} telah dihapus")
            input("Enter untuk kembali memilih menu")
            os.system('cls || clear')

          case "5":
            print("Anda memilih menu 5")
            print("Keluar Program")
            exit()
            os.system('cls||clear')

          case _:
            print(f"menu {pilih} tidak tersedia")
            input("Enter untuk memilih menu")
            os.system('cls || clear')
            
            
              