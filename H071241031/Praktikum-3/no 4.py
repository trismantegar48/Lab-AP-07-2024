harga = int(input("Masukkan total harga : "))
uang = int(input("Masukkan uang yang diberikan : "))
nominal = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uang - harga

print("uang kembalian : ", kembalian)

for i in nominal :
    if kembalian >= i :
        lembar_uang = kembalian // i
        kembalian -= lembar_uang * i
        print(f"{lembar_uang} lembar Rp. {i}")