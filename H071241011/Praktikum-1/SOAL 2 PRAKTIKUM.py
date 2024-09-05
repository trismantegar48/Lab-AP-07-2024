karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

isi = karakter in kalimat
cari = (f'{karakter} ditemukan dalam "{kalimat}"') * isi + (f'{karakter} tidak ditemukan dalam "{kalimat}"') * (not isi)
print(cari)
