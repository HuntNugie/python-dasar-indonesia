# belajar operator logika di python

# not, or, and, xor

# not
a = True
c = not a

print("========NOT========")
print("Nilai awal = ",a)
print('NOT')
print("Nilai akhir = ",c)

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
