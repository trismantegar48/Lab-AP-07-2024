import random

angka_rahasia = random.randint(1, 100)
maksimal_tebakan = 5

for i in range(maksimal_tebakan):
    try:
        tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))

        if tebakan == 0:
            print("Permainan dihentikan. Terima kasih telah bermain!")
            break
        
        if tebakan < angka_rahasia:
            print("Angka terlalu kecil.")
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar.")
        else:
            print("Selamat! Anda berhasil menebak angka dengan benar.")
            break  

    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

if tebakan != angka_rahasia and tebakan != 0:
    print(f"Anda telah menggunakan semua percobaan. Angka rahasia adalah {angka_rahasia}.")
