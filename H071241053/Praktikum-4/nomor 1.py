import random

def n():
    return random.randint(1, 11)

def dealer(nilai_kartu):
    while sum(nilai_kartu) < 17:
        nilai_kartu.append(n())
    return nilai_kartu

def blackjack():
    print("Welcome to Blackjack!")
    kartu_pemain = [n()]
    nilai_kartu = [n()]
    print(f"Kartu dealer adalah: {nilai_kartu[0]}")
    
    while True:
        kartu_pemain.append(n())
        print(f"Kartu anda sekarang adalah: {sum(kartu_pemain)}")
        if sum(kartu_pemain) > 21:
            print("Anda kalah, kartu anda melebihi 21.")
            return
        decision = input("Apakah masih akan mengambil kartu? (y/n): ")
        if decision.lower() == 'n':
            break
    
    nilai_kartu = dealer(nilai_kartu)
    print(f"Kartu dealer sekarang adalah: {sum(nilai_kartu)}")
    
    if sum(nilai_kartu) > 21:
        print("Anda menang, dealer melebihi 21.")
    elif sum(nilai_kartu) == sum(kartu_pemain):
        print("Seri!")
    elif sum(kartu_pemain) > sum(nilai_kartu):
        print("Anda menang!")
    else:
        print("Dealer menang!")

blackjack()
