A = float(input("Masukkan populasi awal serangga A: "))
B = float(input("Masukkan populasi awal serangga B: "))
H = int(input("Masukkan jumlah hari: "))


for hari in range(1, H + 1):

        if hari % 2 == 1: 
            A = int(A * 1.3)
            B = int(B * 1.5)
        else:  
            A = int(A * 0.8)
            B = int(B * 0.6)

        if hari % 5 == 0:
            A = int(A * 0.9)
            B = int(B * 0.9)
            print(f"Hari {hari}: Predator memakan 10% populasi.")
        
        
        if hari % 5 != 0:
            print(f"Hari {hari}: Serangga A = {A:.0f}, Serangga B = {B:.0f}")
            

