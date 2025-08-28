# belajar memanipulasi string menggunakan method

# upper
# berfungsi untuk membuat teks menjadi besar semua
namaDepan = "nugie"
print("normal = " + namaDepan)
namaDepan = namaDepan.upper()
print(f"upper = {namaDepan}")

# lower
# berfungsi untuk membuat teks menjadi kecil semua
namaBelakang = "KURNIAWAN"
print("normal = "+namaBelakang)
namaBelakang = namaBelakang.lower()
print(f"lower = {namaBelakang}")

# pengecekan biasanya menggunakan method dengan nama depan method nya is
# isalpha <== berfungsi untuk mengecek apakah semua karakter nya itu huruf
# dan tentu saja pengecekan semua nya akan menghasilkan nilai boolean True or false
bahasa = "python"
print(f"apakah {bahasa} menggunakan huruf semua : {bahasa.isalpha()}")

# isalnum <== berfungsi untuk mengecek apakah semua karakter nya itu kombinasi antara huruf dan angka
print(f"apakah {bahasa} merupakan kombinasi huruf dan angka : {bahasa.isalnum()}")

# isdecimal <== berfungsi untuk mengecek apakah semua karakter nya itu adalah angka saja
print(f"apakah {bahasa} merupakan angka saja : {bahasa.isdecimal()}")

# isupper <== berfungsi untuk mengecek apakah semua karakter nya itu menggunakan huruf besar semua
print(f"apakah {bahasa} menggunakan huruf besar semua : {bahasa.isupper()}")

# islower <== berfungsi untuk mengecek apakah semua karakter nya itu menggunakan huruf kecil semua
print(f"apakah {bahasa} menggunakan huruf kecil semua : {bahasa.islower()}")

# istitle <== berfungsi untuk mengecek apakah semua kalimat karakter nya itu di awali dengan huruf besar semua 
print(f"apakah {bahasa} semuanya di awali dengan huruf besar : {bahasa.istitle()}")

# isspace()
# berfungsi untuk mengecek apakah kalimat string tersebut merupakan string kosong yang berisi hanya spasi,tab,ataupun newline
print(f"apakah {" \t"} adalah string kosong : {" \t".isspace()}")

# startswitch
# berfungsi untuk mengecek apakah kalimat karakter pertama menggunakan suatu kalimat 
judul = "Go back couple"
cek_start = judul.startswith("Go")
print(f"apakah {judul} di awali dengan kalimat Go : {cek_start}")

# endswitch
# berfungsi untuk mengecek apakah kalimat karakter terakhir menggunakan suatu kalimat
cek_end = judul.endswith("couple")
print(f"apakah {judul} di akhiri dengan kalimat couple : {cek_end}")

# penggabungan .join dan pemisahan .split
data = ["aku","sayang","kamu"]
print(data)
gabung = ",".join(data)
print(f"hasil penggabungan dari {data} : {gabung}")

# pemisahan .splice
data = "akukyahsayangkyahkamu"
pisah = data.split("kyah")
print(f"hasil pemisahan dari {data} : {pisah}")

# alokasi karakter rjust,ljust,center
# rjust
# berfungsi untuk agar string berada di kanan
print("kanan".rjust(15,"="))

# ljust
# berfungsi untuk agar string berada di kiri
print("kiri".ljust(15,"="))

# center
# berfungsi untuk agar string berada di tengah
tengah = "tengah".center(15,"=")
print(tengah)

# bekebalikan nya strip
# berfungsi untuk menghapus karakter yang di inginkan kecuali menghapus karakter dari string nya
print(tengah.strip("="))