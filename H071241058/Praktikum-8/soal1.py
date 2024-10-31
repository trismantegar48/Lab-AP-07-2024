import re
inputan = input("Masukkan kata: ")
pola = r'^[2468A-Za-z]{40}[13579\s]{5}$'
hasil = re.match(pola, inputan)
if hasil :
    print("True")
else:
    print("False")    