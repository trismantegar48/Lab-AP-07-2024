harga = int(input("Masukkan total harga: "))
uang = int(input("Masukkan jumlah uang yang diberikan: "))


pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uang - harga
print(f"Kembalian: {kembalian}")
    
for p in pecahan:
        jumlah_lembar = kembalian // p
        if jumlah_lembar > 0:
            print(f"{jumlah_lembar} lembar Rp {p}")
            kembalian %= p


