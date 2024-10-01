import random

def hitung_total(kartu):
    total = 0
    jumlah_as = 0
    for k in kartu:
        if k == 'A':
            jumlah_as += 1
            total += 11
        elif k in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(k)

    while total > 21 and jumlah_as > 0:
        total -= 10
        jumlah_as -= 1
    
    return total

def tarik_kartu():
    kartu = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(kartu)

def main_blackjack():
    print("Welcome to Blackjack!")

    kartu_pemain = [tarik_kartu()]
    kartu_dealer = [tarik_kartu()]
    
    print(f"Kartu anda sekarang adalah: {hitung_total(kartu_pemain)}")
    
    while True:
        jawab = input("Apakah masih akan mengambil kartu? (y/n) ").lower()
        if jawab == 'y':
            kartu_pemain.append(tarik_kartu())
            total_pemain = hitung_total(kartu_pemain)
            print(f"Kartu anda sekarang adalah: {total_pemain}")
            
            if total_pemain > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif jawab == 'n':
            break
        else:
            print("Input tidak valid. Silakan jawab dengan 'y' atau 'n'.")

    print(f"Kartu dealer adalah: {hitung_total([kartu_dealer[0]])}")
    while hitung_total(kartu_dealer) < 17:
        kartu_dealer.append(tarik_kartu())
        print(f"Kartu dealer sekarang adalah: {hitung_total(kartu_dealer)}")
    
    total_dealer = hitung_total(kartu_dealer)
    total_pemain = hitung_total(kartu_pemain)

    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_pemain > total_dealer:
        print("Anda menang!")
    elif total_pemain == total_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")

main_blackjack()
