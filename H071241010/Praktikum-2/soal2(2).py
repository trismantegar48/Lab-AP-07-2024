usia = input("Masukkan usia Anda: ")

if not usia.isdigit() or int(usia) < 0:
    print("usia tidak valid")
else:
    usia = int(usia)
    anggota = input("Apakah Anda anggota (ya/tidak)? ").lower()

    if anggota != "ya" and anggota != "tidak":
        print("keanggotaan tidak valid")

    else:
        harga_tiket = 0 if usia < 5 else (50000 if usia <= 12 else (100000 if usia <= 59 else 70000))
        harga_setelah_diskon = harga_tiket * 0.8 if anggota == 'ya' else harga_tiket

        print(f"Harga tiket yang harus dibayar: Rp. {harga_setelah_diskon:.0f}")