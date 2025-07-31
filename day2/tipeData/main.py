# tipe data merupakan sebuah tipe dari sebuah value
# ada beberapa tipe data yang ada di python 

# integer (bilangan bulat)
nomor = 99

# float (bilangan desimal)
desimal = 1.5

# string (kumpulan kata)
nama = "Nugie kurniawan"

# boolean (true/false)
boolean = True

print(f"Nama adalah {type(nama)} \n angka adalah {type(nomor)} \n bilangan pecah adalah {type(desimal)} \n bilangan biner adalah {type(boolean)}")

# tambahan (bilangan complex dan tipe data yang ada di bahasa C)
from ctypes import c_double
double = c_double(2.5)

print(type(double))

kompleks = complex(5,6)
print(type(kompleks))