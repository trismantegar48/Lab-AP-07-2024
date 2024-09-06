harga_hari_ini = 105.0
harga_kemarin = float(input("Masukkan harga kemarin:"))

persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100
rekomendasi = ((persen > 5) * "beli" + (-3 <= persen <= 5) * "tahan" + (persen < -3) * "jual")

print(f"Perubahan persentase :{persen:.2f}%")
print(f"Rekomendasi investasi:{rekomendasi}")
