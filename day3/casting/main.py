# casting merupakan sebuah istilah untuk konversi tipe data

print("====INTEGER====")
data_awal = 0
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_float = float(data_awal)
data_str = str(data_awal)
data_boolean = bool(data_awal)

print("data = ",data_float,", tipe data = ", type(data_float)) # akan di ubah menjadi float contoh 10.0
print("data = ",data_str,", tipe data = ", type(data_str)) # akan di ubah menjadi text string
print("data = ",data_boolean,", tipe data = ", type(data_boolean)) #akan menjadi true kecuali jika 0

print("====FLOAT====")
data_awal = 8.9
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_int = int(data_awal)
data_str = str(data_awal)
data_boolean = bool(data_awal)

print("data = ",data_int,", tipe data = ", type(data_int)) # akan di ubah menjadi Int contoh 8
print("data = ",data_str,", tipe data = ", type(data_str)) # akan di ubah menjadi text string
print("data = ",data_boolean,", tipe data = ", type(data_boolean)) #akan menjadi true kecuali jika 0

print("====BOOLEAN====")
data_awal = False
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_int = int(data_awal)
data_str = str(data_awal)
data_float = float(data_awal)

print("data = ",data_int,", tipe data = ", type(data_int)) # jika True akan menghasilkan int 1 jika false akan menghasilkan int 0
print("data = ",data_str,", tipe data = ", type(data_str)) # akan di ubah menjadi text string
print("data = ",data_float,", tipe data = ", type(data_float)) # jika True akan menghasilkan float 1.0 jika false akan menghasilkan 0.0

print("====STRING====")
data_awal = "30"
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_int = int(data_awal) 
data_boolean = bool(data_awal)
data_float = float(data_awal)

print("data = ",data_int,", tipe data = ", type(data_int)) # jika string nya adalah berupa angka akan terkonversi menjadi int kecuali jika string nya adalah huruf akan error
print("data = ",data_boolean,", tipe data = ", type(data_boolean)) # jika string nya di isi akan menghasilkan true jika berupa string kosong maka akan menjadi false
print("data = ",data_float,", tipe data = ", type(data_float)) # jika string nya adalah berupa angka akan terkonversi menjadi float kecuali jika string nya adalah huruf akan error



