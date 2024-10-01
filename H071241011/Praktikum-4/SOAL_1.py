import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def jenis_kartu():
    kartu = random.randint(1, 10)
    if kartu == 1:
        return 11
    return kartu

def jumlah_kartu(kartu):
    nilai_total = sum(kartu)
    if nilai_total > 21 and 11 in kartu:
        nilai_total -= 10
    return nilai_total

def judul_keren():
    print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▄▄ █░░ ▄▀█ █▀▀ █▄▀ ░░█ ▄▀█ █▀▀ █▄▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▄█ █▄▄ █▀█ █▄▄ █░█ █▄█ █▀█ █▄▄ █░█
    """)

def main():
    clear_screen()
    judul_keren()

    while True:
        kartu_pemain = [jenis_kartu()]
        kartu_dealer = [jenis_kartu()]

        while True:
            print(f"\n-- Kartu Anda: {kartu_pemain}, Total: {jumlah_kartu(kartu_pemain)} --")
            print(f"-- Kartu Dealer Yang Terlihat: {kartu_dealer[0]} --")

            if jumlah_kartu(kartu_pemain) > 21:
                print("\n-- BUST! --")
                print("-- Anda Kalah! --")
                break

            ambil_kartu = input("-- Apakah Anda Masih Ingin Mengambil Kartu? Y/N : ").lower()
            if ambil_kartu == 'n':
                break

            kartu_pemain.append(jenis_kartu())

        if jumlah_kartu(kartu_pemain) <= 21:
            print("\n-- Giliran Dealer --")
            while jumlah_kartu(kartu_dealer) < 17:
                kartu_dealer.append(jenis_kartu())
                print(f"-- Kartu Dealer: {kartu_dealer}, Total: {jumlah_kartu(kartu_dealer)} --")

            if jumlah_kartu(kartu_dealer) > 21:
                print("\n-- BUST! --")
                print("-- Dealer Kalah! --")
            else:
                print(f"\n-- Total Kartu Anda: {jumlah_kartu(kartu_pemain)} --")
                print(f"-- Total Kartu Dealer: {jumlah_kartu(kartu_dealer)} --")

                if jumlah_kartu(kartu_pemain) > jumlah_kartu(kartu_dealer):
                    print("-- Anda Menang! --")
                elif jumlah_kartu(kartu_pemain) == jumlah_kartu(kartu_dealer):
                    print("-- Permainan Seri! --")
                else:
                    print("-- Dealer Menang! --")

        main_lagi = input("\nApakah Anda ingin bermain lagi? (Y/N): ").lower()
        if main_lagi == 'n':
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    main()