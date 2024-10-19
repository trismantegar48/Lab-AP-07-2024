usia = input("Masukkan usia: ")

if not usia.isdigit() or int(usia) < 0 : 
    print("input usia tidak valid")
else:
    usia = int(usia)
    cek = input("Apakah anda anggota (ya/tidak): ")
    
    if cek != "ya" and cek != "tidak":
        print("input anggota tidak valid")
    else:
        harga = 0 if usia < 5 else (50000 if usia <= 12 else (100000 if usia <= 59 else 70000))
        harga = harga * 0.8 if cek == "ya" else harga 
        
        print(f"harga tiket: Rp. {int(harga)}")
    

    