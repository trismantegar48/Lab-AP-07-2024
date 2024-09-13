usia = input("Masukkan Usia : ")

if not usia.isdigit() or int(usia) < 0 :
    print("Usia Tidak Valid")
else:
    usia = int(usia) 
    status = input("Apakah Anda Anggota (ya/tidak) : ").lower()

    if status != "ya" and status != "tidak":
        print("Status Tidak Valid")
        
    else:
        harga = "Gratis" if usia < 5 else (50000 if usia <= 12 else (100000 if usia <= 59 else 70000))
        if harga != "Gratis":
            harga = harga * 0.8 if status == "ya" else harga

        if harga == "Gratis":
            print("Harga Tiket : Gratis")
        else:
            print(f"Harga Tiket : Rp. {harga}")