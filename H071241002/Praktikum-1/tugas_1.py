# Meminta pengguna untuk memasukkan harga saham kemarin
harga_kemarin = float(input("Masukkan harga saham kemarin: "))

# Harga saham hari ini sudah diketahui
harga_hari_ini = 105.0

# Menghitung perubahan persentase harga saham
perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

# Menentukan rekomendasi investasi berdasarkan perubahan persentase harga
rekomendasi = ("Beli" * (perubahan_persen > 5) + 
               "Tahan" * (-3 <= perubahan_persen <=5) +
               "Jual" * (perubahan_persen < -3))

# Menampilkan hasil
print(f"Perubahan persentase harga: {perubahan_persen:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")
