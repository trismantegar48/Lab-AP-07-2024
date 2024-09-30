import random
print("Welcome to Blackjack!")
def permainan_Blackjack():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
    random.shuffle(deck)

    def nilai_kartu(deck):
        if deck in ["J", "K", "Q"]:
            return 10
        elif deck == "A":
            return 11
        else:
            return deck

    nilai_pemain = 0
    nilai_dealer = 0

    kartu_baru = deck.pop()
    nilai_pemain += nilai_kartu(kartu_baru)
    print(f"Kartu anda sekarang adalah: {kartu_baru}")

    while True:
        ambil_kartu = input("Apakah masih akan mengambil kartu? (y/n): ")
        
        if ambil_kartu == "y":
            kartu_baru = deck.pop()
            nilai_pemain += nilai_kartu(kartu_baru)
            print(f"Kartu anda sekarang adalah : {nilai_pemain}")
            if nilai_pemain > 21:
                print("Mohon maaf anda kalah, kartu anda lebih dari 21.")
                return  
        elif ambil_kartu == "n":
            break
        else:
            print("Input tidak valid. Silakan masukkan 'y' untuk mengambil kartu atau 'n' untuk berhenti.")

    while nilai_dealer < 17:
        kartu_dealer_baru = deck.pop()
        nilai_dealer += nilai_kartu(kartu_dealer_baru)
        print(f"kartu dealer adalah : {nilai_dealer}")

    if nilai_dealer > 21:
        print("Selamat anda menang, nilai dealer lebih dari 21.")
    elif nilai_pemain > nilai_dealer:
        print("Selamat anda menang!")
    elif nilai_pemain < nilai_dealer:
        print("Mohon maaf anda kalah.")
    else:
        print("Permainan seri.")

permainan_Blackjack()      
            