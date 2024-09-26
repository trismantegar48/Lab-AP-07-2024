tinggi_baris = int(input("Masukkan Jumlah Baris : "))

for zee in range(1, 1 + tinggi_baris):
    if zee % 2 == 0:
        continue
    print((tinggi_baris - zee) * " " + "* " * zee)

for zee in range(tinggi_baris - 1, 0, -1):
    if zee % 2 == 0:
        continue
    print((tinggi_baris - zee) * " " + "* " * zee)
