# mempelajari tipe data string
# string merupakan kumpulan banyak character
# ada banyak fitur untuk memanipulasi string

# membuat string bisa menggunakan single quote atau double quote
single = 'ini string single quote'
doble = "ini string double quote"
print(single,doble)

# bisa untuk single quote di dalam double quote akan terdeteksi sebagai character di dalam string ataupun sebaliknya
gabungan = "ini adalah hari ju'mat"
print(gabungan)

# backslash \
# backslash di string memiliki banyak fungsi

# tab
# bisa seperti memberi tab pada string
print("Nugie \t\t Nadin")

# new lane
# bisa seperti di beri enter
print("nugie \n nadin")

# backspace 
# bisa seperti menggunakan backspace
print("Nugie \bNadin")

# menggunakan backslash di string
print("C:\\user\\nugie")

# string literal atau raw
# di python ada string literal yang menghapus konversi backslash
print(r"C:\nugie\nadin") # ini akan menghapus konversi backslash menjadi string biasa normal

# multiline string
# string di python bisa multiline speerti penggunaan multiline commentar

print("""
      nama : Nugie
      prodi : teknik informatika
      """)