import random

angka_rahasia = random.randint(1, 100)
Percobaan = 5

print("Met datang tebak angka!, ANG ANG ANG")

while True :
    for i in range(Percobaan):
        try:
            tebakan = int(input(f"Masukkan tebakan Anda ({i+1}/{Percobaan}, 0 untuk berhenti): "))
        except ValueError:
            print("PLEASE!. Masukkan angka, ANGKA!!!")
            continue
        
        if tebakan == 0:
            print("Permainan di stop, yakin gak maen?.")
            break

        if tebakan == angka_rahasia:
            print("Njay Slebew! Anda menebak angka dengan benar.")
            break

        elif tebakan > angka_rahasia:
            print("Kebesaran Angkanya Bang.")
        else:
            print("Kecil Pula Angkanya, Higher!")
    else:
        print(f"LO kehabisan percobaan. Angka rahasia nya adalah {angka_rahasia}. jangan semangat, coba lagi.")
        continue

    break