import random

angka_rahasia = random.randint(1, 100)
max_attempts = 5
      
for attempt in range(1, max_attempts + 1):
        tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
        
        if tebakan == 0:
            print("Permainan dihentikan.")
            break
        elif tebakan == angka_rahasia:
            print("Selamat! Anda menebak angka dengan benar.")
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar.")
        else:
            print("Angka terlalu kecil.")
        
        if attempt == max_attempts:
            print(f"Maaf, kesempatan Anda telah habis. Angka yang benar adalah {angka_rahasia}.")


