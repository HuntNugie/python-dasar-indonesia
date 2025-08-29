# format string merupakan sebuah fitur dimana kita dapat membuat format pada string agar tidak perlu menggunakan generic untuk merangkat satu string

# format string
# cara penggunaan
nama = "Nugie"
format_string = f"nama saya {nama}"
print(format_string)

# bisa memisahkan dengan ordo ribuan dan ini otomatis
uang = 20000
format_uang = f"Rp.{uang:,}"
print(format_uang)

# bisa mengambil angka di belakang koma untuk decimal
angka = 123897.567
format_decimal = f"angka = {angka:.2f}"
print(format_decimal)

# bisa leading zero
angka = 123.234
format_leading = f"zero = {angka:09}"
print(format_leading)

# bisa aritmatika
a = 1000
b = 19
hasil = f"hasil dari {a} x {b} = {a*b:,}"
print(hasil)