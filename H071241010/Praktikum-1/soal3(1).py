print("Konversi detik ke jam")
total_detik = int(input("Masukkan jumlah detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{jam:02}:{menit:02}:{detik:02}")