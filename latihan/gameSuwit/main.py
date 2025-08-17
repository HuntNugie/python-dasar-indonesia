# game suwit
import random
# selamat datang
print("Selamat datang di game suwit jawa !!!")
ulang = True

while(ulang):
    # masukan input user
    user = int(input("anda dapat memilih berikut ini \n1.gajah \n2.semut \n3.manusia \nMasukan pilihan anda (1-3) : "))

    # verifikasi pilihan user
    if(user == 1):
        user = "gajah"
    elif(user == 2):
        user = "semut"
    elif(user == 3):
        user = "manusia"
    else:
        print("Anda tidak memasukkan dengan benar!!")
        break;
    
    # pilihan computer
    comp = random.randint(1,3)
    if(comp == 1):
        comp = "gajah"
    elif(comp == 2):
        comp = "semut"
    elif(comp == 3):
        comp = "manusia"
        
    
    # membuat rule
    if(user == comp):
        hasil = "user dan computer imbang"
    else:
        if(user == "gajah"):
            hasil = "user menang" if(comp == "manusia") else "user kalah"
        elif(user == "semut"):
            hasil = "user menang" if(comp == "gajah") else "user kalah"
        elif(user == "manusia"):
            hasil = "user menang" if(comp == "semut") else "user kalah"
    
    print(f"pilihan user = {user} \npilihan computer = {comp} \nHasil pertandingan nya adalah {hasil}")
    user = input("apakah anda mau bermain kembali (y/n) :")
    if(user == "y"):
        ulang = True
    else:
        ulang = False
