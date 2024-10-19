print("Konversi detik ke jam")
n = int(input(f"Masukkan jumlah detik: "))

a = n // 3600
b = (n % 3600) // 60
c = n % 60

print(f"{a:02}:{b:02}:{c:02}")