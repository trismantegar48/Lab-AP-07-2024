populasi_a = int(input("Masukkan populasi awal serangga A: "))
populasi_b = int(input("Masukkan populasi awal serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for hari in range(1, jumlah_hari + 1):
    if hari % 2 == 1:  
        populasi_a = int(populasi_a * 1.3)  
        populasi_b = int(populasi_b * 1.5)  
    
    else:  
        populasi_a = int(populasi_a * 0.8) 
        populasi_b = int(populasi_b * 0.6)  

    if hari % 5 == 0:
        populasi_a = int(populasi_a * 0.9)  
        populasi_b = int(populasi_b * 0.9)  
        print(f"Hari {hari}: Predator memakan 10% populasi.")

    print(f"Hari {hari}: Serangga A = {populasi_a}, Serangga B = {populasi_b}")
