nama = input("Masukan nama : ")
umur = input("Masukan Umur: ")
alamat = input("Masukan alamat: ")
email = input("Masukan Email: ")
dosen = input("Masukan Dosen wali: ")

teks = "Nama: {}\nUmur: {}\nAlamat: {}\nemail: {}n\ndosen: {}".format(nama, umur, alamat,email,dosen)

file_open = open ("biodata.txt", "w")
file_open.write(teks)

file_open.close()

file = open("biodata.txt", "r")
text = file.read()
print(text)
file.close()

