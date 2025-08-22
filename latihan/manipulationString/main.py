# latihan memanipulasi string

# concatination (menyambung string)
nama_awal = "Nugie"
nama_akhir = "kurniawan"
nama_lengkap = nama_awal + " "+ nama_akhir
print(nama_lengkap)

# mengetahui panjang character dari string
panjang = len(nama_lengkap)
print(f"Nama lengkap memiliki {panjang} character")

# mengecek apakah suatu string berada di dalam string
cek = "u" in nama_lengkap
print(f"u apakah ada di dalam {nama_lengkap} = {cek} ")

# mengecek apakah suatu string tidak berada dalam string
cek = "z" not in nama_lengkap
print(f"z apakah tidak ada di dalam {nama_lengkap} = {cek}")

# indexing dimulai dari 0
print(f"index ke-0 dari {nama_lengkap} = {nama_lengkap[0]}")
# jika menggunakan minus akan mengecek langsung di akhir string sebagai -1 index pertama di akhir
print(f"index ke -1 dari {nama_lengkap} = {nama_lengkap[-1]}")
# range akan mengambil beberapa string 
print(f"mengambil 5 string pertama = {nama_lengkap[0:6]}") #disini menggunakan 6 karna index paling akhir nya yaitu 6 tidak akan di ambil
# bisa mengambil dengan melewati
print(f"mengambil seluruh string hanya saja di lewat 1 baris masing masing {nama_lengkap[0:len(nama_lengkap)-1:2]}")

# mengambil nilai character paling kecil dan besar
print(f"character paling kecil nilai nya di {nama_lengkap} adalah {min(nama_lengkap)}")
# character paling besar
print(f"character paling besar nilai nya di {nama_lengkap} adalah {max(nama_lengkap)}")

# menghitung berapa banyak character yang ada di dalam string
cek = "a"
print(f"Banyak character {cek} di dalam {nama_lengkap} adalah {nama_lengkap.count(cek)}")