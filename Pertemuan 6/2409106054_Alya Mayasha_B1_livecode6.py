#data_mhs = {
#    "nama" : "ucup",
#    "nim" : "1",
#    "matkul" : ["APD", "kalkulus", "jarkom"]
#    "dosen" : {
#               "nama" : "Pak Awang",
#               "matkul" : "APD"
#    }
#}

data_mhs = [
    {"nama" : "ucup",
    "role" : "admin"
    },

    {"nama" : "michael",
     "role" : "user"
    }
]

print(data_mhs[0]['nama'])
print(data_mhs[1]['nama'])
data_mhs2 = [
    ["ucup", "admin"
     "michael", "user"]
]

print(data_mhs2[0][1])

#print(data_mhs["dosen"]["nama"])

#print(data_mhs['nama'])
#print(data_mhs['nim'])
#print(data_mhs['mapel'])

#print(data_mhs.get('mapel', 'Gak ada'))
#for data in data_mhs:
#    print(data)
#for key_data, valude_data in data_mhs.item():
#    print(f"key: {key_data}\nValue: {value_data}\n")
#data_mhs['alamat'] = "samarinda"
#data_mhs['alamat'] = "tenggarong"
#print(data_mhs)

#data_mhs.update({"alamat" : "samarinda"})
#data_mhs.update({"alamat" : "tengggarong"})

#data_mhs["nama"] = 'michae
#del data_mhs["nim"]
#cache = data_mhs.pop('nim')
#print(data_mhs, "Dictionary")
#print(cache, "cache")

#data_mhs["id"] = cache

#print(data_mhs) 
#print(data_mhs.clear(), "clear")
#print(len(data_mhs))

#key = "apel", "jeruk", "mangga"
#value = 1,5,9
#buah = dict.fromskeys(key, value)
#print(buah)

#for value in data_mhs.keys():
    #print(value)
#for key in data_mhs:
    #print(data_mhs[key])

#Nilai ={
#    "Matematika" : 90,
#    "B.Indonesia" : 90,
#    "Kimia" : 20,
#    "B.Inggris" : 81 
#}