# konversi suhu dari celcius ke reamur, fahrenheit, dan kelvin

print("====PROGRAM KONVERSI CELCIUS====")
suhu = float(input("Masukkan suhu anda dalam satuan celcius : "))

# dalam celcius
print(f"suhu Dalam celcius adalah {suhu} celcius")

# dalam reamur
reamur = (4/5) * suhu
print(f"suhu Dalam reamur adalah {reamur} Reamur")

# dalam fahrenheit
fahrenheit = ((9/5)*suhu) + 32
print(f"suhu dalam fahrenheit adalah {fahrenheit} Fahrenheit")

# kelvin
kelvin = suhu+273
print(f"suhu dalam kelvin adalah {kelvin} Kelviin")
