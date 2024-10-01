import random

print("Selamat datang di Blackjack!")
def buat_deck():
    """Membuat deck kartu yang diacak."""
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
    random.shuffle(deck)
    return deck

def hitung_nilai(kartu):
    """Menghitung nilai total dari sebuah list kartu."""
    nilai = 0
    for kartu_ini in kartu:
        if kartu_ini in ["J", "Q", "K"]:
            nilai += 10
        elif kartu_ini == "A":
            nilai += 11
        else:
            nilai += kartu_ini
    return nilai

def permainan_Blackjack():
    """Fungsi utama permainan Blackjack."""
    deck = buat_deck()
    pemain_kartu = [deck.pop(), deck.pop()]
    dealer_kartu = [deck.pop()]

    print(f"Kartu Anda sekarang adalah: {hitung_nilai(pemain_kartu)}")

    # Pemain mengambil kartu tambahan
    while True:
        pilihan = input("Apakah Anda ingin mengambil kartu lagi? (y/n): ")
        if pilihan.lower() == 'y':
            pemain_kartu.append(deck.pop())
            print(f"Kartu Anda sekarang adalah: {hitung_nilai(pemain_kartu)}")
            if hitung_nilai(pemain_kartu) > 21:
                print("Anda kalah!")
                return
        else:
            break

    # Dealer mengambil kartu hingga mencapai 17 atau lebih
    print(f"kartu dealer adalah : {hitung_nilai(dealer_kartu)}")
    while hitung_nilai(dealer_kartu) < 17:
         dealer_kartu.append(deck.pop())
    print(f"kartu dealer sekarang adalah : {hitung_nilai(dealer_kartu)}")

    # Hitung nilai akhir dan tentukan pemenang
    nilai_pemain = hitung_nilai(pemain_kartu)
    nilai_dealer = hitung_nilai(dealer_kartu)

    if nilai_pemain > 21:
        print("Anda kalah!")
    elif nilai_dealer > 21:
        print("Anda menang!")
    elif nilai_pemain > nilai_dealer:
        print("Anda menang!")
    elif nilai_pemain < nilai_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

permainan_Blackjack()