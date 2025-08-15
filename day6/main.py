# komparasi(perbandingan)

# komparasi atau perbandingan merupakan membandingkan 2 nilai yang akan menghasilkan boolean

# ==
# membandingkan apakah nilai nya sama 
a = 5
b = 5
hasil = a == b
print(f"{a} == {b} = {hasil}")
# !=
# membandingkan apakah nilai nya tidak sama
hasil = a!=b
print(f"{a} != {b} = {hasil}")

# <
# membandingkan apakah nilai yang ada di sebelah kiri lebih kecil di banding di sebelah kanan
hasil = a < b
print(f"{a} < {b} = {hasil}")
# >
# membandingkan apakah nilai yang ada di sebelah kiri lebih besar di banding di sebelah kanan
hasil = a>b
print(f"{a} > {b} = {hasil}")

# <=
# membandingkkan apakah nilai yang ada di sebelah kiri lebih kecil atau sama dengan di sebelah kanan
hasil = a<=b
print(f"{a} <= {b} = {hasil}")

# >=
# membandingkan apakah nilai yang ada di sebelah kiri lebih besar atau sama dengan di sebelah kanan
hasil = a>=b
print(f"{a} >= {b} = {hasil}")

# is (object identity)
# membandingkan apakah object tersebut apakah sama berada di alamat memori yang sama
hasil = a is b
print(f"{a} is {b} = {hasil}")

# is not(object identity)
# membandingkna apakah object tersebut apakah tidak sama berada di alamat memori yang berbeda
hasil = a is not b
print(f"{a} is not {b} = {hasil}")
