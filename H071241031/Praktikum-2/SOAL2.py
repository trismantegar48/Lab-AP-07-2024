usia = int(input("Masukkan usia : "))
keanggotaan = (input("Apakah berlangganan? (ya/tidak) : "))

if usia < 5:
    harga = 0

elif usia >= 5 and usia <= 12:
    harga = 50000

elif usia >= 13 and usia <= 59:
    harga = 100000

else:
    harga = 70000

diskon = harga * (80/100)


hargatiket = diskon if keanggotaan == ("ya") else harga

print(f"Harga tiket = Rp. {int(hargatiket)} ")