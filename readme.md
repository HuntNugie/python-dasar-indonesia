# PYTHON DASAR
python merupakan bahasa pemograman dimana bahasa ini adalah bahasa interpreter(di terjemah) hanya saja bisa juga di compiler, bahasa pemograman ini sangat luas sekali penggunaan nya
**bisa untuk**
- Web development(django, flask)
- mobile apps
- Desktop apps
- Data science
- Machine learning
- artificial inteligent(ai)


# Cara menginstall persiapkan diri untuk python
cukup download saja python disini [Download](https://www.python.org/downloads/)<br>
![image](img/image.png)<br>
> untuk pengguna windows setelah download tinggal klik saja hasil download nya dan selesaikan instalasi nya

## untuk mengetes apakah python nya sudah terinstall gunakan perintah di bawah ini di terminal

**di windows**
```bash
python --version
```


**jika hasilnya seperti dibawah ini maka telah terinstall**
```bash
Python 3.13.5
```

## Perintah dasar
Berikut perintah perintah dasar di python
- print() = untuk menampilkan output 
- menggunakan # untuk komentar

# Cara menjalankan program python
cara menjalankan program python terbagi menjadi 2 yaitu dengan interpreter dan compiler

1. menggunakan interpreter
cara nya sangat mudah anda tinggal buka terminal anda dan masuk ke directory working area anda dan tinggal jalankan seperti ini <br>
**di windows**
```bash
python namaProgram.py
```
**contoh**
```bash
python main.py
```

2. Menggunaakn compiler
kadang jika program python kita sudah sangat besar maka waktu unutk menjalankan nya ingin lebih cepat maka menggunakan compiler <br>
**di windows**
```bash
python -m py_compile namaProgram.py
```
**contoh**
```bash
python -m py_compile main.py
```

## Setelah itu akan muncul folder dan file seperti ini
![image](img/pycace.png)

**Masuk terlebih dahulu ke dalam folder dengan perintah**
```bash
cd __pycache__
```

**Setelah itu jalankan perintah python**
```bash
python main.cpython-313.pyc
```

> Catatan : Dalam menjalankan program python ini jika program anda sudah sangat besar di sarankan untuk menggunakan cara compiler agar lebih cepat

# Variabel
di dalam python pembuatan python sangat mudah karna tidak memelukan keyword tambahan seperti di bahasa pemograman lain serta tidak perlu deklarasi tipe data nya

## Penamaan variabel
dalam penamaan varibel ada beberapa aturan dalam pembuatan namanya
<table>
    <tr>
        <th>Contoh</th>
        <th>Konfirmasi</th>
        <th>Keterangan</th>
    </tr>
    <tr>
        <td>10judul</td>
        <td>Tidak boleh</td>
        <td>dalam pembuatan variabel tidak boleh di awali number</td>
    </tr>
    <tr>
        <td>judul10</td>
        <td>boleh</td>
        <td>salah satu contoh yang benar karna number tidak boleh di awal nama variabel</td>
    </tr>
    <tr>
        <td>judul</td>
        <td>boleh</td>
        <td>Seperti pembuatan variabel pada umumnya</td>
    </tr>
    <tr>
        <td>judul Belakang</td>
        <td>tidak boleh</td>
        <td>Tidak boleh ada spasi</td>
    </tr>
    <tr>
        <td>judul-belakang</td>
        <td>tidak boleh</td>
        <td>Tidak boleh menggunakan min(-) karna di dalam python tanda tersebut di gunakan dalam operator aritmatika yaitu pengurangan</td>
    </tr>
    <tr>
        <td>judulBelakang</td>
        <td>boleh</td>
        <td>Disarankan jika ingin menggunakan 2 kalimat menggunakan camel case</td>
    </tr>
    <tr>
        <td>judul_belakang</td>
        <td> boleh</td>
        <td>Boleh memakai underscore untuk menyambung 2 kalimat dalam penamaan variabel</td>
    </tr>
</table>

## Cara penggunaan
```python
nama = "Nugie kurniawan"
print(nama)
```

## Hasil
```bash
Nugie kurniawan
```

> Catatan : Perhatikan dalam penamaan variabel agar sesuai dengan apa yang akan di tampung oleh variabel tersebut

# Tipe Data
tipe data merupakan tipe dari sebuah nilai values nya ada beberapa tipe data utama di python 

## Integer
integer merupakan tipe data untuk angka bilangan bulat

### Cara Penggunaan
```python
angka = 99
print(angka)
```

### Hasil
```
99
```
## Float
Float merupakan tipe data angka untuk bilangan desimal(pecahan)

### Cara penggunaan
```python
phi = 3.14
print(phi)
```

### Hasil
```
3.14
```

## String
String merupakan tipe data untuk kumpulan huruf dan angka

### Cara pengunaan
```python
nama = "Nugie kurniawan"
print(nama)
```

### Hasil
```
Nugie kurniawan
```

## Boolean
tipe data boolean merupakan tipe data yang hanya berisi 2 nilai yaitu True atau False

### Cara Pengunaan
```python
ganteng = True
print(ganteng)
```

### Hasil
```
True
```

## (Bonus) tipe data di bahasa C
di dalam python kita juga dapat menggunakan tipe data dari bahasa C karna python sendiri di buat dengan bahasa C

### Cara pengunaan
```python
# pertama kita harus import dulu modul nya
from ctypes import c_double

data_double = c_double(3.5)
print(data_double.value)
```

### Hasil
```
3.5
```

# Casting(konversi tipe data)
Casting adalah sebuah istilah khusus untuk konversi(mengubah tipe data) tipe data di python 

## Int(Integer)
- int->float = akan dikonversi tipe data float contoh 8.0
- int->string = akan dikonversi sebuah text string "8"
- int->boolean = akan dikonversi False jika integer nya adalah 0 selain 0 akan True

### Cara Penggunaan
```py
print("====INTEGER====")
data_awal = 0
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_float = float(data_awal)
data_str = str(data_awal)
data_boolean = bool(data_awal)

print("data = ",data_float,", tipe data = ", type(data_float)) # akan di ubah menjadi float contoh 10.0
print("data = ",data_str,", tipe data = ", type(data_str)) # akan di ubah menjadi text string
print("data = ",data_boolean,", tipe data = ", type(data_boolean)) #akan menjadi true kecuali jika 0
```

### Hasil
```
====INTEGER====
data awal =  0 , tipe data =  <class 'int'>
data =  0.0 , tipe data =  <class 'float'>
data =  0 , tipe data =  <class 'str'>
data =  False , tipe data =  <class 'bool'>
```

## Float
- float->int = akan di konversi menjadi int **contoh 5**
- float->str = akan di konversi menjadi text "5"
- float->bool = akan di konversi menjadi False jika di isi dengan 0 selain 0 akan menjadi True

### Cara penggunaan
```py
print("====FLOAT====")
data_awal = 8.9
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_int = int(data_awal)
data_str = str(data_awal)
data_boolean = bool(data_awal)

print("data = ",data_int,", tipe data = ", type(data_int)) # akan di ubah menjadi Int contoh 8
print("data = ",data_str,", tipe data = ", type(data_str)) # akan di ubah menjadi text string
print("data = ",data_boolean,", tipe data = ", type(data_boolean)) #akan menjadi true kecuali jika 0
```

### Hasil
```
====FLOAT====
data awal =  8.9 , tipe data =  <class 'float'>
data =  8 , tipe data =  <class 'int'>
data =  8.9 , tipe data =  <class 'str'>
data =  True , tipe data =  <class 'bool'>
```

## Bool(BOOLEAN)
- bool->int = akan di konversi menjadi int jika nilai bool nya True maka akan menghasilkan 1 dan jika False akan menghasilkan 0
- bool->float = akan di konversi menjadi float jika nilai bool nya True maka akan menghasilkan 1.0 dan jika False akan menghasilkan 0.0
- bool->str = akan di konversi menjadi text string saja

### Cara penggunaan
```py
print("====BOOLEAN====")
data_awal = False
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_int = int(data_awal)
data_str = str(data_awal)
data_float = float(data_awal)

print("data = ",data_int,", tipe data = ", type(data_int)) # jika True akan menghasilkan int 1 jika false akan menghasilkan int 0
print("data = ",data_str,", tipe data = ", type(data_str)) # akan di ubah menjadi text string
print("data = ",data_float,", tipe data = ", type(data_float)) # jika True akan menghasilkan float 1.0 jika false akan menghasilkan 0.0
```

### Hasil
```
====BOOLEAN====
data awal =  False , tipe data =  <class 'bool'>
data =  0 , tipe data =  <class 'int'>
data =  False , tipe data =  <class 'str'>
data =  0.0 , tipe data =  <class 'float'>
```

## Str(String)
- str->int = akan dikonversi menjadi int jika string nya berupa angka jika string berupa huruf maka akan error
- str->float = akan di konversi menjadi float jika string nya berupa angka jika string berupa huruf maka akan error
- str->bool = akan di konversi menjadi bool jika string tersebut ada isinya akan menghasilkan true dan jika string kosong akan menghasilkan false

### Cara penggunaan
```py
print("====STRING====")
data_awal = "30"
print("data awal = ",data_awal,", tipe data = ",type(data_awal))

data_int = int(data_awal) 
data_boolean = bool(data_awal)
data_float = float(data_awal)

print("data = ",data_int,", tipe data = ", type(data_int)) # jika string nya adalah berupa angka akan terkonversi menjadi int kecuali jika string nya adalah huruf akan error
print("data = ",data_boolean,", tipe data = ", type(data_boolean)) # jika string nya di isi akan menghasilkan true jika berupa string kosong maka akan menjadi false
print("data = ",data_float,", tipe data = ", type(data_float)) # jika string nya adalah berupa angka akan terkonversi menjadi float kecuali jika string nya adalah huruf akan error
```

### Hasil
```
====STRING====
data awal =  30 , tipe data =  <class 'str'>
data =  30 , tipe data =  <class 'int'>
data =  True , tipe data =  <class 'bool'>
data =  30.0 , tipe data =  <class 'float'>
```

> Catatan : Berhati hati lah jika mau casting tipe data karna bukan hanya tipe data nya saja yang berubah isinya(**nilai**) juga akan menyesuaikan dengan konversi tipe data nya

# input
input merupakan sebuah fungsi bawaan dari python yang berfungsi untuk user bisa menginputkan langsung nilai langsung dari keyboard

## Str(string)
secara default inputan itu akan menghasilkan string

### Cara penggunaan 
```py
nama = input("Masukkan nama anda : ") # jika inputan biasa itu apapun nilai nya akan di konversi jadi string
print("String  = ",nama," ada ",len(nama)," karakter") # fungsi len untuk menghitung berapa banyak karakter dari string
```

### Hasil
```
Masukkan nama anda : Nugie kurniawan
String  =  Nugie kurniawan  ada  15  karakter
```

## int(Integer)
jika kita hanya ingin inputkan itu akan menghasilkan string maka kita wajib casting inputan tersebut menjadi int

### Cara penggunaan
```py
# int
integer = int(input("Masukkan angka integer : ")) # menggunakan casting int untuk bisa inputan nya hanya angka
print("Integer = ",integer)
```

### Hasil
```
Masukkan angka integer : 5
Integer =  5
```

## float
jika ingin inputan nya menghasilkan nilai float maka kita juga harus casting inputan tersebut dengan fungsi float

### Cara penggunaan
```py
# float
floates = float(input("Masukkan angka float : ")) # menggunakan casting float untuk bisa inputan nya di isi angka float
print("float = ",floates)
```

### Hasil
```
Masukkan angka float : 2.3
float =  2.3
```

## bool(Boolean)
jika kita ingin inputan nya hasilnya menjadi nilai boolean alangkah lebih baik nya kita memberi dulu casting dengan int baru casting bool karna hanya int yang konsisten terhadap nilai boolean

### Cara penggunaan
```py
# bool
boolean = bool(int(input("Masukkan angka (1/0) : ")))
print("bool = ",boolean)
```

### Hasil
```
Masukkan angka (1/0) : 0
bool =  False
```

> Catatan : casting pada inputan ini hanya akan mempengaruhi **nilai** nya saja untuk proses dari inputan nya masih tetap bebas menginputkan apapun

# Operator logika
operator logika merupakan operator yang bertugas untuk memanipulasi tipe data boolean

**daftar operator logika**
<table>
    <tr>
        <th>Simbol</th>
        <th>nama Simbol</th>
    </tr>
    <tr>
        <td>not</td>
        <td>not(tidak)</td>
    </tr>
    <tr>
        <td>or</td>
        <td>or(atau)</td>
    </tr>
    <tr>
        <td>and</td>
        <td>and(dan)</td>
    </tr>
    <tr>
        <td>^</td>
        <td>xor</td>
    </tr>
</table>

## NOT(kebalikan)
not dalam operator logika berfungsi untuk membalikan nilai boolean jika true akan menjadi false dan jika false akan menjadi true

### Cara penggunaan
```py
# not
a = True
c = not a

print("========NOT========")
print("Nilai awal = ",a)
print('NOT')
print("Nilai akhir = ",c)
```

### Hasil
```
========NOT========
Nilai awal =  True
NOT
Nilai akhir =  False
```

## OR (atau)
or dalam operator logika bisa di lakukan jika minimal ada 2 atau lebih boolean, untuk or akan bernilai true jika minimal saja salah satu true akan menghasilkan true

### Cara penggunaan
```py
# or (akan true jika minimal salah satu true)
a = True
b = False
c = a or b

print("========OR========")

print(a," OR ",b," = ",c)
a = True
b = True
c = a or b

print(a," OR ",b," = ",c)
a = False
b = True
c = a or b

print(a," OR ",b," = ",c)
a = False
b = False
c = a or b

print(a," OR ",b," = ",c)
```

### Hasil
```
========OR========
True  OR  False  =  True
True  OR  True  =  True
False  OR  True  =  True
False  OR  False  =  False
```

## AND(dan)
and dalam operator logika akan bisa di gunakan jika terdapat 2 atau lebih nilai boolean, and akan bernilai true jika kedua nilai nya adalah true

### Cara penggunaan
```py
# and (akan true jika kedua nya adalah true)
a = True
b = False
c = a and b

print("========AND========")

print(a," AND ",b," = ",c)
a = True
b = True
c = a and b

print(a," AND ",b," = ",c)
a = False
b = True
c = a and b

print(a," AND ",b," = ",c)
a = False
b = False
c = a and b

print(a," AND ",b," = ",c)

```

### Hasil
```
========AND========
True  AND  False  =  False
True  AND  True  =  True
False  AND  True  =  False
False  AND  False  =  False
```

## XOR
XOR dalam operasi logika dapat di gunakan jika minimal ada 2 atau lebih nilai boolean, xor akan bernilai true jika kedua nilai nya berbeda akan menghasilkan true

### Cara penggunaan
```py
# xor (akan true jika salah satu harus true dan satunya lagi harus false)
a = True
b = False
c = a ^ b

print("========XOR========")

print(a," XOR ",b," = ",c)
a = True
b = True
c = a ^ b

print(a," XOR ",b," = ",c)
a = False
b = True
c = a ^ b

print(a," XOR ",b," = ",c)
a = False
b = False
c = a ^ b

print(a," XOR ",b," = ",c)


```

### Hasil
```
========XOR========
True  XOR  False  =  True
True  XOR  True  =  False
False  XOR  True  =  True
False  XOR  False  =  False
```

> Catatan : untuk xor sebenernya bukan operator logika murni melainkan operator bitwise.

# Operator aritmatika
Operator aritmatika merupakan sebuah operator matematika dalam bahasa pemograman untuk mengoperasikan dan memanipulasi bilangan angka(integer,float)
<br>

**Daftar operator aritmatika**
<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Operator</th>
      <th>Nama Operasi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>+</code></td>
      <td>Penjumlahan</td>
    </tr>
    <tr>
      <td><code>-</code></td>
      <td>Pengurangan</td>
    </tr>
    <tr>
      <td><code>*</code></td>
      <td>Perkalian</td>
    </tr>
    <tr>
      <td><code>/</code></td>
      <td>Pembagian (hasil <em>float</em>)</td>
    </tr>
    <tr>
      <td><code>//</code></td>
      <td>Pembagian Bulat (floor division)</td>
    </tr>
    <tr>
      <td><code>%</code></td>
      <td>Modulus (sisa bagi)</td>
    </tr>
    <tr>
      <td><code>**</code></td>
      <td>Pangkat (exponen)</td>
    </tr>
  </tbody>
</table>

## Urutan prioritas 
1. kurung ()
2. exponen(pangkat) **
3. kali,bagi,floor division(pembagian bulat kebawah),modulus(sisa bagi) *,/,//,%
4. tambah,kurang +,-

## Pertambahan(+)
Pertambahan seperti halnya di matematika berfungsi untuk menjumlahkan 2 atau lebih angka

### Cara penggunaan
```py
a = 10
b = 5
# pertambahan
hasil = a+b
print(f"Hasil dari {a} + {b} adalah {hasil}")
```

### Hasil
```
Hasil dari 10 + 5 adalah 15
```

## Pengurangan(-)
Seperti halnya di dalam matematika juga pengurangan disini berfungsi untuk mengurangi 2 angka atau lebih 

### Cara penggunaan
```py
a = 10
b = 5
# pengurangan
hasil = a-b
print(f"Hasil dari {a} - {b} adalah {hasil}")
```

### Hasil
```
Hasil dari 10 - 5 adalah 5
```

## Pembagian(/)
seperti halnya di matematika pembagian merupakan operasi matematik yang berfungsi untuk membagi antara 2 bilangan

### Cara penggunaan
```py
a = 10
b = 5
# pembagian (otomatis tipe data nya adalah float)
hasil = a/b
print(f"Hasil dari {a} / {b} adalah {hasil} ")
```

### Hasil
```
Hasil dari 10 / 5 adalah 2.0 
```

## Perkalian(*)
Seperti halnya di matematika pembagian merupakan operasi matematika yang berfungsi untuk mengkalikan antar 2 bilangan

### Cara penggunaan
```py
a = 10
b = 5
# perkalian
hasil = a*b
print(f"Hasil dari {a} * {b} adalah {hasil}")
```

### Hasil
```
Hasil dari 10 * 5 adalah 50
```


## Exponen(**)
operasi Exponen atau biasa di sebut operasi pangkat di dalam matematika

### Cara penggunaan
```py
a = 10
b = 5
# exponen(pangkat)
hasil = a**b
print(f"Hasil dari {a} ** {b} adalah {hasil}")
```

### Hasil
```
Hasil dari 10 ** 5 adalah 100000
```

## Modulus(%)
Modulus atau sering di sebut sisa bagi merupakan operasi yang akan menghasilkan nilai dari sisa bagia dari kedua nilai

### Cara penggunaan
```py
a = 10
b = 5
# modulus(sisa bagi)
hasil = a%b
print(f"Hasil dari {a} % {b} adalah {hasil}")
```
### Hasil
```
Hasil dari 10 % 5 adalah 0
```

## Floor division(//)
Floor division atau bisa di sebut juga pembagian bulat kebawah merupakan sebuah operasi pembagian tetapi akan menghasilkan tipe data integer serta akan membulatkan kebawah hasil dari pembagian nya

### Cara penggunaan
```py
a = 10
b = 5
# floor division
hasil = a//b
print(f"Hasil dari {a} // {b} adalah {hasil}")
```

### Hasil
```
Hasil dari 10 // 5 adalah 2
```

> Catatan : hati hati dalam ingin menggunakan lebih dari 1 operator aritmatika ingat kembali urutan agar hasilnya sesuai yang di harapkan

# komparasi(perbandingan)
operator komparasi(perbandingan) merupakan operator yang membandingkan 2 buah nilai atau lebih yang akan menghasilkan nilai boolean(true/false)

## sama dengan(==)
akan membandingkan 2 nilai apakah sama nilai nya jika iya maka akan menghasilkan true dan jika tidak akan menghasilkan false

### Cara penggunaan
```py
a = 5
b = 5
hasil = a == b
print(f"{a} == {b} = {hasil}")
```

### Hasil
```
5 == 5 = True
```

## tidak sama dengan(!=)
akan membandingkan nilai apakah tidak sama dengan jika iya akan menghasilkan true jika tidak akan menghasilkan false

### Cara penggunaan
```py
a = 5
b = 5
hasil = a!=b
print(f"{a} != {b} = {hasil}")
```

### Hasil
```
5 != 5 = False
```

## lebih kecil dari(<)
akan membandingkan nilai yang ada di sebelah kiri apakah lebih kecil dari yang sebelah kanan

### Cara penggunaaan
```py
a = 5
b = 5
hasil = a < b
print(f"{a} < {b} = {hasil}")
```

### Hasil
```
5 < 5 = False
```

## lebih besar dari(>)
akan membandingkan apakah nilai yang ada di sebelah kiri lebih besar dari yang ada di sebelah kanan

### Cara penggunaan
```py
a = 5
b = 5
hasil = a>b
print(f"{a} > {b} = {hasil}")
```

### Hasil
```
5 > 5 = False
```

## lebih kecil dari atau sama dengan(<=)
akan membandingkan nilai yang ada di sebelah kiri lebih kecil atau sama dengan nilai yang ada di sebelah kanan

### Cara penggunaan
```py
a = 5
b = 5
hasil = a<=b
print(f"{a} <= {b} = {hasil}")
```

### Hasil
```
5 <= 5 = True
```

## lebih besar dari atau sama dengan(>=)
akan membandingkan apakah nilai yang ada di sebelah kiri lebih besar dari atau sama dengan nilai yang ada di sebelah kanan

### Cara penggunaan
```py
a = 5
b = 5
hasil = a>=b
print(f"{a} >= {b} = {hasil}")
```

### Hasil
```
5 >= 5 = True
```

## is(object indentiity)
akan membandingkan apakah nilai object nya sama alamat nya memori nya sama 

### Cara penggunaan
```py
a = 5
b = 5
hasil = a is b
print(f"{a} is {b} = {hasil}")
```

### Hasil
```
5 is 5 = True
```

## is not(object indentitiy)
akan membandingkan apakah alamat memori dari object nya tidak sama

### Cara penggunaan
```py
a = 5
b = 5
hasil = a is not b
print(f"{a} is not {b} = {hasil}")
```

### Hasil
```
5 is not 5 = False
```

# assigment(penugasan)
operator assigment atau bahasa indonesia nya adalah penugasan merupakan operator yang berfungsi untuk menugaskan variable sebelah kiri dengan nilai sebelah kanan

## jenis jenis Operator assigment

### +=(tambah)
merupakan operasi assigment yang berfungsi untuk menambahkan nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 2
a += 3
print(a)
```

#### Hasil
```
5
```

### -=(kurang)
merupakan operasi yang mengkurangi nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 5
a -= 2
print(a)
```

#### Hasil
```
3
```

### *=(kali)
merupakan operasi assigment yang berfungsi untuk mengkalikan nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 2
a*=2
print(a)
```
#### Hasil
```
4
```

### /=(bagi)
merupakan operasi assigment yang berfungsi untuk membagi nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 10
a/=2
print(a)
```

#### Hasil
```
5.0
```

### **= (exponen(pangkat))
merupakan operasi assigment untuk mempangkatkan nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 18.0
a **= 2
print(a)
```
#### Hasil
```
324.0 # hasilnya float karna operand nya float jika operand nya int maka hasilnya akan integer
```

### //= (floor division(pembagian bulat))
merupakan operasi assigment yang berfungsi untuk membagi menjadi bulat nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 10
a//=3
print(a)
```

#### Hasil
```
3
```

### %= (modulus(sisa bagi))
merupakan operasi assigment yang berfungsi untuk mendapatkan sisa bagi dari pembagian nilai kiri dengan nilai kanan

#### Cara penggunaan
```py
a = 10
a %= 3
print(a)
```

#### Hasil
```
1
```

> Catatan : Menggunakan operasi assigment intinya adalah akan merubah nilai yang ada di sebelah kiri dengan nilai kanan sesuai dengan operasi assigment apa yang di jalankan

# String
string merupakan tipe data gabungan character character

## Membuat string
```py
data = "Nugie"
```

## Penggunaan backslash
di dalam string dapat di manipulasi dengan tambahan backslash

### tab
\t akan membuat seperti ada tab pada string
```py
print("Nugie\t\tNadin")
```

### new line
\n akan membuat seperti di kasih enter
```py
print("Nugie\nNadin")
```

### backspace
\b seperi akan menghapus/backspace karakter sebelum \b
```py
print("Nugie \bNadin")
```

### string literal atau raw
string raw akan menghapus konversi backslash pada string
```py
print(r"C:\user\nugie")
```

### Multiline string
string mulltiline sehingga di dalam quote nya akan di hitung semuanya menjadi character string maupun itu enter sekalipun

```py
print("""
Nugie kurniawan
nadin nugraha
""")
```

# menggunakan method
ada beberapa manipulasi string menggunakan method 

## lower()
berfungsi untuk membuat seluruh string menjadi kecil semua

### Cara penggunaaan
```py
nama = "Nugie Kurniawan"
nama = nama.lower()
print(nama)
```

### Hasil
```
nugie kurniawan
```

## upper()
berfungsi untuk membuat string menjadi besar semua

### Cara penggunaan
```py
nama = "nadin nugraha"
nama = nama.upper()
print(nama)
```

### Hasil
```
NADIN NUGRAHA
```

## isalnum
berfungsi untuk mengecek apakah karakter tersebut menggunakan kombinasi antara huruf dan number

### Cara penggunaan
```py
teks = "nugie123"
print(teks.isalnum())
```

### Hasil
```
True
```

## isalpha
berfungsi untuk mengecek apakah kalimat karakter tersebut menggunakan huruf semua

### Cara penggunaan
```py
teks = "nadin"
print(teks.isalpha())
```

### Hasil
```
True
```

## isdecimal
berfungsi untuk mengecek apakah kalimat karakter tersebut hanya mengandung angka saja atau tidak

### Cara penggunaan
```py
teks = "123"
print(teks.isdecimal())
```

### Hasil
```
True
```

## istitle
berfungsi untuk mengecek kalimat karakter tersebut semuanya di awali dengan huruf besar di awalnya

### Cara penggunaan
```py
teks = "Go Back Couple"
print(teks.istitle())
```

### Hasil
```
True
```

## isspace
berfungsi untuk mengecek apakah string tersebut string kosong yang hanya terdiri dari spasi,tab, ataupun newline

### Cara penggunaan
```py
teks = "  \t"
print(teks.isspace())
```

### Hasil
```
True
```

## islower
berfungsi untuk mengecek apakah kalimat karakter tersebut karakter nya menggunakan huruf kecil semua

### Cara penggunaan
```py
teks = "nugie"
print(teks.islower())
```

### Hasil
```
True
```

## isupper
berfungsi untuk mengecek apakah kalimat karakternya menggunakan huruf besar semua

### Cara penggunaan
```py
teks = "NUGIE"
print(teks.isupper())
```

### Hasil
```
True
```

## startswith
berfungsi untuk mengecek apakah kalimat karakter pertama di suatu kalimat itu merupakan suatu kalimat lain

### Cara penggunaan
```py
teks = "anjay guranjay"
print(teks.startswith("anjay"))
```

### Hasil
```
True
```

## endswith
berfungsi untuk mengecek kalimat terakhir dari suatu kalimat karakter merupakan suatu kalimat lain

### Cara penggunaan
```py
teks = "go back couple"
print(teks.endswith("couple"))
```
### Hasil
```
True
```

## join
berfungsi untuk menggabungkan data array atau list menjadi satu string

### Cara penggunaan
```py
data = ["aku","sayang"] 
print(",".join(data))
```

### Hasil
```
aku,sayang
```

## split
berfungsi untuk mengpisahkan string menjadi bentuk array atau list

### Cara penggunaan
```py
data = "akukyahsayang"
print(data.split("kyah"))
```

### Hasil
```
["aku","sayang"]
```

## rjust
berfungsi untuk membuat string menjadi ada di kanan

### Cara penggunaan
```py
print("kanan".rjust(10,"="))
```

### Hasil
```
=====kanan
```

## ljust
berfungsi untuk membuat string berada di sebelah kiri

### Cara penggunaan
```py
print("kiris".ljust(10,"="))
```
### Hasil
```
kiris=====
```

## center
berfungsi untuk agar string menjadi di tengah

### Cara penggunaan
```py
print("tngh".center(10,"="))
```

### Hasil
```
===tngh===
```

## strip
berfungsi untuk menghapus karakter khusus di sebuah string

### Cara penggunaan
```py
teks = "tngh".center(10,"=")
print(teks.strip("="))
```

### Hasil
```
tngh
```