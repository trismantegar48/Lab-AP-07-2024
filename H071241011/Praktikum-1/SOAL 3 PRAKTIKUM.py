print("Konversi detik ke jam")
detik = int(input("Masukkan jumlah detik: "))

jam = detik // 3600
menit = (detik % 3600) // 60
detik = detik % 60

print(f"{jam:02}:{menit:02}:{detik:02}")