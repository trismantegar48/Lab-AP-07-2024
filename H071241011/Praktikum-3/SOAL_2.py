import random as zee

kesempatan = 0
angka_rahasia = zee.randint(1, 100)

while True:
    tebakan = int(input("Masukkan Tebakan Anda (0 Untuk Berhenti) = "))
    kesempatan += 1
    
    if tebakan == 0:
        print("Permainan Dihentikan")
        break

    if tebakan > angka_rahasia:
        print("Angka Terlalu Besar.")
    elif tebakan < angka_rahasia:
        print("Angka Terlalu Kecil.")
    else:
        print("Selamat! Anda Menebak Angka Dengan Benar.")
        break
    
    if kesempatan == 5:
        print(f"Kesempatan Anda Habis, Silahkan Coba Lagi. Angka Yang Benar Adalah {angka_rahasia}")
        break
