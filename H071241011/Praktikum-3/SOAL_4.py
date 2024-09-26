total_harga = int(input("Masukkan Total Harga : "))
jumlah_uang = int(input("Masukkan Uang Yang Diberikan : "))

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = jumlah_uang - total_harga

for uang in pecahan_uang:
    if kembalian == 0:
        print("Uang Yang Diberikan Pas")
        break
    if kembalian < 0:
        print("Uang Yang Diberikan Tidak Cukup")
        break
    else:
        jumlah_lembar = kembalian // uang
        kembalian %= uang
        
        if jumlah_lembar > 0:
            print(f"{jumlah_lembar} lembar Rp." + format(uang, ","))
