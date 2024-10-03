populasi_A = int(input("Masukkan populasi awal serangga A :"))
populasi_B = int(input("Masukkan populasi awal serangga B :"))
jumlah_hari = int(input("Masukkan jumlah hari : "))

for i in range(1, jumlah_hari + 1):
    if i % 2 == 1:
        populasi_A = int(populasi_A * 1.3)
        populasi_B = int(populasi_B * 1.5)
    else:
        populasi_A = int(populasi_A * 0.8)
        populasi_B = int(populasi_B * 0.6)
    
    if i % 5 == 0 :
        populasi_A = int(populasi_A * 0.9)
        populasi_B = int(populasi_B * 0.9)
        print(f"hari {i}: predator memakan 10% populasi.")

    print(f"hari {i}: serangga A =  {populasi_A}, serangga B = {populasi_B} ")