total_harga = float(input("Masukkan total harga: "))
uang_diberikan = float(input("Masukkan jumlah uang yang diberikan: "))

kembalian = uang_diberikan - total_harga

if kembalian < 0:
    print("Uang yang diberikan kurang!")
elif total_harga == uang_diberikan:
    print("Uang anda pas!")
else:
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    

    for pecahan in pecahan_uang:
        jumlah_lembar = int(kembalian // pecahan)  
        kembalian %= pecahan  
        if jumlah_lembar > 0:
            print(f"{jumlah_lembar} lembar Rp " + format(pecahan, ","))

