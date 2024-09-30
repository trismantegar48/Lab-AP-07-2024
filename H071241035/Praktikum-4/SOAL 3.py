def proses_angka():
    while True:
        try:
            n = int(input("Masukan angka: "))
            if n <= 0:
                raise ValueError

            langkah = 0
            
            while n != 1:
                print(f"{n:.0f}.0")  
                if n % 2 == 0:
                    n /= 2  #genap, bagi 2
                else:
                    n = 3 * n + 1  #ganjil, kali 3 dan tambah 1
                langkah += 1
            
            print(f"1.0")  
            print(f"Jumlah langkah: {langkah:.0f}")  
           
            break
        
        except ValueError:
            print("Input tidak Valid, masukkan angka")

proses_angka()
