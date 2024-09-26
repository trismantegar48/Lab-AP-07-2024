populasi_serangga_a = int(input("Masukkan Populasi Awal Serangga A: "))
populasi_serangga_b = int(input("Masukkan Populasi Awal Serangga B: "))
jumlah_hari = int(input("Masukkan Jumlah Hari: "))

for hari in range(1, jumlah_hari + 1):
    if hari % 2 != 0:
        populasi_serangga_a += populasi_serangga_a * 0.3  
        populasi_serangga_b += populasi_serangga_b * 0.5
    else:
        populasi_serangga_a -= populasi_serangga_a * 0.2  
        populasi_serangga_b -= populasi_serangga_b * 0.4

    if hari % 5 == 0:
        populasi_serangga_a = int(populasi_serangga_a * 0.9)
        populasi_serangga_b = int(populasi_serangga_b * 0.9)
        
        print(f"Hari {hari}: Predator memakan 10% dari populasi.")

    print(f"Hari {hari}: Serangga A = {populasi_serangga_a:.0f}, Serangga B = {populasi_serangga_b:.0f})")
