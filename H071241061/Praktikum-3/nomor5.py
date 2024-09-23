populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
N = int(input("Masukkan jumlah hari: "))

for hari in range(1, N + 1):
    if hari % 2 != 0:
        populasi_A = int(1.3 * populasi_A)
        populasi_B = int(1.5 * populasi_B)
    else:
        populasi_A = int(0.8 * populasi_A)
        populasi_B = int(0.6 * populasi_B)
    
    if hari % 5 == 0:
        populasi_A = int(0.9 * populasi_A)
        populasi_B = int(0.9 * populasi_B)
        print(f"Hari {hari}: Predator memakan 10% populasi.")

    print(f"Hari {hari}: Populasi Serangga A = {populasi_A:.0f} Populasi Serangga B = {populasi_B:.0f}")
