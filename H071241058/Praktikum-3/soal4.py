total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: "))
kembalian = uang_diberikan - total_harga

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if kembalian < 0:
    print(f"Uang yang diberikan kurang {kembalian} rupiah.")
elif kembalian == 0:
    print("Tidak ada kembalian.")
else:
    print(f"Kembalian: {kembalian} rupiah")
    print("Rincian kembalian:")
    for pecahan in pecahan_uang:
        jumlah_lembar = kembalian // pecahan  
        if jumlah_lembar > 0:
            print(f"{jumlah_lembar:,} lembar uang {pecahan:,}")
        kembalian %= pecahan  
