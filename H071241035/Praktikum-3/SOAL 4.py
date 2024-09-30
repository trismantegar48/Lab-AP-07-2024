pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

#Input
while True:
    try :
        total_harga = int(input("Masukkan total harga: "))
        uang_diberikan = int(input("Masukkan uang yang diberikan: "))
        break
    except :
        print("Input tidak valid, masukkan bilangan bulat")

#kembalilian
kembalian = uang_diberikan - total_harga

if kembalian < 0:
    print("Uang yang diberikan kurang.")
else:
    print(f"Kembalian: Rp {kembalian}")
    
    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah_lembar = kembalian // pecahan
            kembalian = kembalian % pecahan
            print(f"{jumlah_lembar} lembar Rp {pecahan:,}")


























































# pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

# # Input
# total_harga = int(input("Masukkan total harga: "))
# uang_diberikan = int(input("Masukkan uang yang diberikan: "))

# # Kembalian
# kembalian = uang_diberikan - total_harga

# if kembalian < 0:
#     print("Uang yang diberikan kurang.")
# else:
#     print(f"Kembalian: Rp {kembalian}")
    
#     i = 0  # Inisialisasi indeks untuk while loop
#     while i < len(pecahan_uang):
#         pecahan = pecahan_uang[i]
#         if kembalian >= pecahan:
#             jumlah_lembar = kembalian // pecahan
#             kembalian = kembalian % pecahan
#             print(f"{jumlah_lembar} lembar Rp {pecahan:,}")
#         i += 1  # Inkrementasi indeks untuk while loop
