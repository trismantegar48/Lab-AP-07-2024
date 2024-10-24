daftar_film = {}
daftar_tiket = {}

from datetime import datetime

def tambah_film():
    while True:
        print("\n--- Tambah Film ---")
        judul = input("Masukkan nama film yang ingin ditambahkan (atau tekan 0 untuk kembali): ")
        if judul == "0":
            print("\nKembali ke menu admin")
            break
        try:
            daftar_film[judul] = judul
            print(f"\nFilm '{judul}' berhasil ditambahkan")
        except ValueError:
            print("input tidak valid")
            
def list_film():
    if len(daftar_film) == 0:
        print("Tidak ada film yang tersedia")  
    else:
        print("Daftar Film:") 
        for angka, film in enumerate(daftar_film, start=1):
            print(f"{angka}. {film}")

def hapus_film():
    while True:
        if len(daftar_film) == 0:
            print("Tidak ada film dalam daftar")
        list_film()
        pilihan = input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")
        if pilihan == "0":
            break
        try:
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(daftar_film):
                judul = list(daftar_film.keys())[pilihan - 1]
                del daftar_film[judul]
                print(f"Film '{judul}' berhasil dihapus")
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Input harus berupa angka. coba lagi")

def buat_id_tiket():
    sekarang = datetime.now()
    return sekarang.strftime("TICK%d%m%Y%H%M%S")

def buat_tiket(id_tiket, film, tanggal):
    tiket = (
        "+" + "-"*50 + "+\n"
        "|" + " " * 50 + "|\n"
        "|" + "TIKET BIOSKOP".center(50) + "|\n"
        "|" + " " * 50 + "|\n"
        "+" + "-"*50 + "+\n"
        "| ID Tiket  : " + id_tiket.ljust(39) + "|\n"
        "| Film      : " + film.ljust(39) + "|\n"
        "| Tanggal   : " + tanggal.ljust(39) + "|\n"
        "+" + "-"*50 + "+\n"
        "| Terima kasih telah membeli tiket Anda!      |\n"
        "+" + "-"*50 + "+\n"
    )
    
    with open("tiket_bioskop.txt", "a") as file:
        file.write(tiket)
    
    print("Tiket berhasil disimpan ke 'tiket_bioskop.txt'.")   
  
def tampilkan_tiket(id_tiket, film, tanggal):
    tiket = (
        "+" + "-"*50 + "+\n"
        "|" + " " * 50 + "|\n"
        "|" + "TIKET BIOSKOP".center(50) + "|\n"
        "|" + " " * 50 + "|\n"
        "+" + "-"*50 + "+\n"
        "| ID Tiket  : " + id_tiket.ljust(39) + "|\n"
        "| Film      : " + film.ljust(39) + "|\n"
        "| Tanggal   : " + tanggal.ljust(39) + "|\n"
        "+" + "-"*50 + "+\n"
        "| Terima kasih telah membeli tiket Anda!      |\n"
        "+" + "-"*50 + "+\n"
    )
    
    print(tiket)        

def beli_tiket():
    while True:
        if len(daftar_film) == 0:
            print("Tidak ada film yang tersedia untuk dibeli")
        else:    
            list_film()
            pilihan = input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ")
            if pilihan == "0":
                break
            try: 
                pilihan = int(pilihan)
                if 1 <= pilihan <= len(daftar_film):
                    id_tiket = buat_id_tiket()
                    film = list(daftar_film.keys())[pilihan - 1]
                    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    tiket = {'id': id_tiket, 'film': film, 'tanggal': tanggal}
                    daftar_tiket[id_tiket] = tiket
                    buat_tiket(id_tiket, film, tanggal)
                    print(f"Tiket untuk film '{film}' berhasil dibeli dengan ID {id_tiket}.")
                else:
                    print("Pilihan tidak valid. Coba lagi.")
            except ValueError:
                print("Input harus berupa angka. Coba lagi.")

def list_tiket():
    if len(daftar_tiket) == 0:
        print("Belum ada tiket yang dibeli.")
    else:
        print("\nDaftar Tiket:")
        for angka, tiket in enumerate(daftar_tiket.values(), start=1):
            print(f"{angka}. ID Tiket: {tiket['id']}, Film: {tiket['film']}")

def tampilkan_detail_tiket():
    if len(daftar_tiket) == 0:
        print("Belum ada tiket yang dibeli.")
    else:
        list_tiket()
        pilihan = input("\nPilih nomor tiket yang ingin dilihat detailnya (atau 0 untuk kembali): ").strip()
        if pilihan == "0":
            return
        try:
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(daftar_tiket):
                tiket = list(daftar_tiket.values())[pilihan - 1]
                tampilkan_tiket(tiket['id'], tiket['film'], tiket['tanggal'])
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

def hapus_tiket():
    while True:
        if len(daftar_tiket) == 0:
            print("Tidak ada tiket dalam daftar")
            break
        list_tiket()
        pilihan = input("\nMasukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): ")
        if pilihan == "0":
            break
        try:
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(daftar_tiket):
                tiket = list(daftar_tiket.keys())[pilihan - 1]
                del daftar_tiket[tiket]
                print(f"Tiket nomor {pilihan} berhasil dihapus")
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Input harus berupa angka. coba lagi")  
            
def menu_tiket():
    while True:
        print("\n-- Daftar Tiket --")
        print("1. Lihat daftar tiket \n2. Lihat Detail Tiket \n3. Hapus tiket \n4. Kembali")
        tiket = input("pilih opsi (1/2/3/4): ")
        if tiket == "1":
            list_tiket()
        elif tiket == "2":
            tampilkan_detail_tiket()
        elif tiket == "3":
            hapus_tiket()
        elif tiket == "4":
            break    
                

def menu_admin():
    while True:
        print("\n-- Menu Admin --")
        print("1. Tambah Film \n2. Hapus Film \n3. Daftar tiket \n4. Kembali")
        admin = input("pilih opsi (1/2/3/4): ")
        if admin == "1":
            tambah_film()
        elif admin == "2":
            hapus_film()  
        elif admin == "3":
            menu_tiket()
        elif admin == "4":
            break

def menu_pengunjung():
    while True:
        print("\n-- Menu Pengunjung --")
        print("1. Lihat daftar film \n2. Beli tiket \n3. Daftar tiket \n4. Kembali")
        pengunjung = input("pilih opsi (1/2/3/4): ")     
        if pengunjung == "1":
            list_film() 
        elif pengunjung == "2":
            beli_tiket()  
        elif pengunjung == "3":
            list_tiket()
        elif pengunjung == "4":
            break

def main():
    while True:
        print("--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin \n2. Pengunjung \n3. Keluar")
        pilihan = input("Pilih peran (1/2/3): ")
        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            menu_pengunjung()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem ini!")
            break

main()
 