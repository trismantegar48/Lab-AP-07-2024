#SOAL 1
harga_hari_ini = 105.0
harga_kemarin = float(input("Masukkan harga saham kemarin: "))


perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = {
    True: "Beli",
    perubahan_persen >= -3 and perubahan_persen <= 5: "Tahan",
    perubahan_persen < -3: "Jual"
}

print(f"Perubahan persentase: {perubahan_persen:.2f}%")
print(f"Rekomendasi: {rekomendasi[True]}")