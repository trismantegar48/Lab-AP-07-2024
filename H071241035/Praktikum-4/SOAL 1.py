import random

def Kartu():
    return random.randint(1, 11)

def blackjack_game():
    print("Welcome to Blackjack!")
    
    Kartu_Pemain = Kartu()
    Kartu_bandar = Kartu()
    
    print(f"Kartu anda sekarang adalah: {Kartu_Pemain}")
    
    while True:
        Pilihan = input("Apakah masih akan mengambil kartu? (y/n) ").lower()
        if Pilihan == 'y':
            Kartu_Pemain += Kartu()
            print(f"Kartu anda sekarang adalah: {Kartu_Pemain}")
            if Kartu_Pemain > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif Pilihan == 'n':
            break
        else:
            print("Pilihan tidak valid. Harap masukkan 'y' atau 'n'.")
    
   
    print(f"Kartu Bandar adalah: {Kartu_bandar}")
    
    while Kartu_bandar < 17:
        Kartu_bandar += Kartu()
        print(f"Kartu Bandar sekarang adalah: {Kartu_bandar}")
    

    if Kartu_bandar > 21:
        print("Anda menang, Bandar melebihi 21.")
    elif Kartu_Pemain > Kartu_bandar:
        print("Anda menang!")
    elif Kartu_Pemain == Kartu_bandar:
        print("Seri!")
    else:
        print("Bandar menang!")

blackjack_game()
