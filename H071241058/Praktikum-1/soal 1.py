# harga kemarin
saham_kemarin = float(input("masukkan saham kemarin: "))

# harga saham hari ini
saham_hari_ini = 105.0

# persentase
persentase_saham = ((saham_hari_ini - saham_kemarin) / saham_kemarin) * 100

rekomendasi_investasi = ("beli" * (persentase_saham > 5) + 
                         "tahan" * (-3 <= persentase_saham <= 5) +
                         "jual" * (persentase_saham < -3))

print(f"hasil perubahan persentase harga: {persentase_saham:.2f}%")
print(f"rekomendasi_investasi: {rekomendasi_investasi}")