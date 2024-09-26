import random

angka_rahasia = random.randint(1, 100)

print("Selamat datang di permainan tebak angka")
print("Tebak angka antara 1 hingga 100. Kamu punya 5 kesempatan.")

for percobaan in range(5):
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    
    if tebakan == 0:
        print("Permainan dihentikan.")
        break
    
    if tebakan == angka_rahasia:
        print("Selamat! Tebakanmu benar!")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
else:
    print(f"Kesempatan habis. Angka yang benar adalah {angka_rahasia}.")
