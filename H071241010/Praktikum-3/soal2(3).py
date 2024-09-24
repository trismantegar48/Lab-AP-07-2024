import random

angka_rahasia = random.randint(1, 100)

percobaan = 0
while percobaan < 5:
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))

    if tebakan == 0:
        print("Terima kasih sudah bermain!")
        break

    percobaan += 1

    if tebakan < angka_rahasia:
        print("Angka terlalu kecil.")
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Selamat! Anda menebak angka dengan benar.")
        break

if percobaan == 5 and tebakan != angka_rahasia:
    print(f"Anda kehabisan percobaan. Angka rahasianya adalah {angka_rahasia}.")