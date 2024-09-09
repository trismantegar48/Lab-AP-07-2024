karakter = (input("Masukkan karakter: "))
kalimat = (input("Masukkan kalimat: "))

hasil = (karakter in kalimat) and f"{karakter} terdapat dalam \"{kalimat}\"" or f"{karakter} tidak terdapat dalam \"{kalimat}\""

print(hasil)
