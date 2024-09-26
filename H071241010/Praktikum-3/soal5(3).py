populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for hari in range(1, jumlah_hari + 1):
    if hari % 2 == 1:  
        populasi_A = int(populasi_A * 1.3)
        populasi_B = int(populasi_B * 1.5)
    else:  
        populasi_A = int(populasi_A * 0.8)
        populasi_B = int(populasi_B * 0.6)

    if hari % 5 == 0:
        populasi_A = int(populasi_A * 0.9)
        populasi_B = int(populasi_B * 0.9)
        print(f"Hari {hari}: Predator memakan 10% populasi.")

    print(f"Hari {hari}: Serangga A = {populasi_A}, Serangga B = {populasi_B}")