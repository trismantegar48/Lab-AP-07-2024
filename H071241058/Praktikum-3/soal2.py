import random

print("="*51)
print("=====Selamat datang di permainan menebak angka=====")
print("="*51)
print("\n", "  Tebaklah angka antara 1 sampai 100")
print("ketik '0' jika ingin menghentikan permainan")

angka_rahasia = random.randint(1, 100)
percobaan = 5

for i in range(percobaan):
    try: 
        tebakan = int(input("\n" f"Masukkan tebakan anda (0 untuk berhenti): "))
        if tebakan == 0:
            print("Permainan telah berhenti karena pemain telah mengetik angka 0")
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar")
        elif tebakan < angka_rahasia:
            print("Angka terlalu kecil")        
        else:
            print("Selamat! Anda menebak angka dengan benar")       
    except ValueError:
        print("Mohon masukkan angka dengan benar")
else:
    print(f"Maaf, Anda telah kehabisan percobaan. Angka rahasia adalah {angka_rahasia}")      