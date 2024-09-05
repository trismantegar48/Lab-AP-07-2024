karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

o = f"{karakter} merupakan bagian dari kalimat" * (karakter in kalimat) or f"{karakter} tidak ditemukan dalam kalimat"

print(o)