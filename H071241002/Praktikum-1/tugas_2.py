karakter = input("Masukkan karakter yang ingin dicari: ")
kalimat = input("Masukkan kalimat: ")

pesan = (f"{karakter} Karakter tidak ditemukan dalam Kalimat '{kalimat}'", f"{karakter} Karakter merupakan bagian dari Kalimat '{kalimat}'")[karakter in kalimat]

print(pesan)