Baris = int(input("Masukkan Jumlah Baris: "))

input_ganjil = Baris % 2 != 0
lebar_maks = (Baris if input_ganjil else Baris - 1) * 2 - 1


for i in range(1, Baris // 2 + 1):
    print(("* " * (2 * i - 1)).center(lebar_maks))

if input_ganjil:
    print(("* " * Baris).center(lebar_maks))

for i in range(Baris // 2, 0, -1):
    print(("* " * (2 * i - 1)).center(lebar_maks))


