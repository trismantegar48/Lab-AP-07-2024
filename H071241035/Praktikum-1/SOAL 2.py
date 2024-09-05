# SOAL 2 :
# Input 
karakter = input("Masukkan Karakter: ")
kalimat = input("Masukkan kalimat: ")

# Menggunakan operator `in` untuk memeriksa apakah karakter ada di dalam kalimat
pesan = f'Karakter "{karakter}" "merupakan bagian dari" * (karakter in kalimat) or "tidak ditemukan dalam "{kalimat}"'

# Output 
print(pesan)

