harga_kemarin = float(input("masukan harga saham kemarin :"))
harga_hari_ini = 105

persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = ((persen > 5) * "Beli" + (-3 <= persen <= 5) * "Tahan" + (persen < -3) * "Jual")
print(f"Perubahan presentase: {persen:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")