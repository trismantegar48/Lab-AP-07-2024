i = int(input("Konversi detik ke jam\nMasukkan jumlah detik: "))
j = i // 3600
sisa = i % 3600
m = sisa // 60
d = sisa % 60

print(f"{j:02}:{m:02}:{d:02}")