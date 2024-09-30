populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

if jumlah_hari > 0:
    for hari in range (1, jumlah_hari + 1):
        if hari > 0:
            if hari % 2 == 1:
                populasi_A = int(populasi_A * 1.3)
                populasi_B = int(populasi_B * 1.5)
            else:
                populasi_A = int(populasi_A * 0.8)
                populasi_B = int(populasi_B * 0.6)
                
            if hari % 5 == 0:
                populasi_A = int(populasi_A * 0.9)
                populasi_B = int(populasi_B * 0.9)
                
                print(f"hari ke {hari} predator memakan 10% populasi")
            
            print(f"hari ke {hari}: serangga A = {populasi_A} dan serangga B = {populasi_B}")

else: print("hari harus lebih dari 0")































# populasi_A = int(input("Masukkan populasi awal Serangga A: "))
# populasi_B = int(input("Masukkan populasi awal Serangga B: "))
# jumlah_hari = int(input("Masukkan jumlah hari: "))

# for i in range(1, jumlah_hari + 1):
#     if i % 2 == 1:  
#         populasi_A += int(0.3 * populasi_A) 
#         populasi_B += int(0.5 * populasi_B)  
#     else: 
#         populasi_A -= int(0.2 * populasi_A)  
#         populasi_B -= int(0.4 * populasi_B) 
    
#     if i % 5 == 0:
#         populasi_A -= int(0.1 * populasi_A)  
#         populasi_B -= int(0.1 * populasi_B)  
#         print(f"Hari {i}: Predator memakan 10% populasi.")
    
#     print(f"Hari {i}: Serangga A = {populasi_A}, Serangga B = {populasi_B}")