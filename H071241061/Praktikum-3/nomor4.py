total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

kembalian = uang_diberikan - total_harga

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

print(f"Kembalian: {kembalian:,} rupiah")

for uang in pecahan:
    if kembalian >= uang:
        jumlah_lembar = kembalian // uang
        kembalian %= uang
        print(f"{jumlah_lembar} lembar Rp {uang:,}")
