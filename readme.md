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