# aritmatika merupakan operasi matematika yang ada di bahasa pemograman
'''
tambah +
kurang -
bagi /
kali *
exponen(pangkat) **
modulus(sisa bagi) %
floor division(pembagian dengan pembulatan ke bawah)
'''
a = 10
b = 5

# pertambahan
hasil = a+b
print(f"Hasil dari {a} + {b} adalah {hasil}")

# pengurangan
hasil = a-b
print(f"Hasil dari {a} - {b} adalah {hasil}")

# pembagian (otomatis tipe data nya adalah float)
hasil = a/b
print(f"Hasil dari {a} / {b} adalah {hasil} ")

# perkalian
hasil = a*b
print(f"Hasil dari {a} * {b} adalah {hasil}")

# exponen(pangkat)
hasil = a**b
print(f"Hasil dari {a} ** {b} adalah {hasil}")

# modulus(sisa bagi)
hasil = a%b
print(f"Hasil dari {a} % {b} adalah {hasil}")

# floor division
hasil = a//b
print(f"Hasil dari {a} // {b} adalah {hasil}")

'''
urutan prioritas
1.kurung ()
2.exponen **
3.kali,bagi,modulus,floor division *,/,%,//
4.tambah kurang +, -
'''