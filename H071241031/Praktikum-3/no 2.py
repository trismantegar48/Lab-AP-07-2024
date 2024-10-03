import random

angka_rahasia = random.randint(1, 100)

max_percobaan = 5

print("Tebak angka antara 1 hingga 100. Anda memiliki 5 kali percobaan.")
print("Ketik '0' jika Anda ingin menghentikan permainan.")

for percobaan in range(1, max_percobaan + 1):
    tebakan = int(input(f"Percobaan {percobaan}: Masukkan tebakan Anda: "))
    
    if tebakan == 0:
        print("Permainan dihentikan. Terima kasih telah bermain!")
        break
    
    if tebakan == angka_rahasia:
        print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar!")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
    if percobaan == max_percobaan:
        print(f"Maaf, Anda telah mencapai batas percobaan. Angka rahasianya adalah {angka_rahasia}.")
