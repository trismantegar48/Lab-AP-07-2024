karakter = input("Masukkan karakter :")
kalimat = input("Masukkan kalimat:")

isi = (f'{karakter} merupakan karakter dalam "{kalimat}".' * (karakter in kalimat) + f'{karakter} tidak ditemukan dalam "{kalimat}".' * (karakter not in kalimat ))
print(isi)