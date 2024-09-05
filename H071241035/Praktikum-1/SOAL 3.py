# SOAL 3 : Buatlah sebuah program yang mengubah jumlah detik yang diberikan menjadi
#format waktu jam:menit:detik (01:20:40).

# input detik
total_detik = int(input("Masukkan jumlah detik: "))

# fungsi detik ke jam, menit, dan detik
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Output : jam:menit:detik
print(f"{jam:02}:{menit:02}:{detik:02}")

