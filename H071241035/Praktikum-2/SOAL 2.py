# input
usia = input("Masukkan usia: ")

if not usia.isdigit() or int(usia) < 0 : 
    print ("Usia tidak Valid")
else :
    usia = int(usia)
    anggota = input("Apakah Anda anggota (ya/tidak): ").lower() == 'ya'

    if anggota != "ya" and anggota != "tidak" :
        print ("input anggota tidak valid")

# Menentukan harga tiket 
    else : 
        harga_tiket = 0 if usia < 5 else 50000 if usia <= 12 else 100000 if usia <= 59 else 70000


# memkai ternary operator untuk diskon jika pengguna adalah anggota 
        harga_tiket = harga_tiket * 0.8 if anggota else harga_tiket

# harga tiket
        print(f"Harga tiket: Rp. {int(harga_tiket)}")
