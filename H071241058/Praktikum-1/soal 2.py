karakter = input("masukkan karakter: ")
kalimat = input("masukkan kalimat: ")

pengecekan = ("ditemukan dalam" * (karakter in kalimat) +
              "tidak ditemukan dalam" * (karakter not in kalimat)
              )
print(f"{karakter} {pengecekan} {kalimat}")