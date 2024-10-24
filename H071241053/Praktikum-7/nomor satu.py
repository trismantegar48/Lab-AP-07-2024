from datetime import datetime

gudang_film = []  
tiket_terjual = []  

def tambah_film():
    film = input("Masukkan nama film: ")
    gudang_film.append(film)
    print(f"Film '{film}' berhasil ditambahkan.")

def hapus_film():
    tampilkan_film()
    pilihan = int(input("Masukkan nomor film yang ingin dihapus: ")) - 1
    if 0 <= pilihan < len(gudang_film):
        film_terhapus = gudang_film.pop(pilihan)
        print(f"Film '{film_terhapus}' berhasil dihapus.")
    else:
        print("Pilihan tidak valid.")

def tampilkan_film():
    if gudang_film:
        print("Daftar Film:")
        for i, film in enumerate(gudang_film, 1):
            print(f"{i}. {film}")
    else:
        print("Tidak ada film yang tersedia.")

def beli_tiket():
    tampilkan_film()
    pilihan = int(input("Pilih nomor film: ")) - 1
    if 0 <= pilihan < len(gudang_film):
        nama = input("Masukkan nama Anda: ")
        id_tiket = f"TICK{datetime.now().strftime('%Y%m%d%H%M%S')}"
        tiket = {
            "id": id_tiket, 
            "film": gudang_film[pilihan], 
            "nama": nama, 
            "tanggal": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }
        tiket_terjual.append(tiket)
        print(f"Tiket berhasil dibeli! ID: {id_tiket}")
        simpan_tiket(tiket)
    else:
        print("Pilihan tidak valid.")

def simpan_tiket(tiket):
    with open("tiket.txt", "a") as file:
        file.write(f"{tiket['id']} | {tiket['film']} | {tiket['nama']} | {tiket['tanggal']}\n")
    print("Tiket berhasil disimpan ke tiket.txt")

def tampilkan_tiket():
    if tiket_terjual:
        print("Daftar Tiket:")
        for i, tiket in enumerate(tiket_terjual, 1):
            print(f"{i}. ID: {tiket['id']}, Film: {tiket['film']}, Nama: {tiket['nama']}")
    else:
        print("Belum ada tiket yang terjual.")

def lihat_detail_tiket():
    if not tiket_terjual:
        print("Belum ada tiket yang terjual.")
        return
    
    tampilkan_tiket()
    pilihan = int(input("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ")) - 1
    
    if 0 <= pilihan < len(tiket_terjual):
        tiket = tiket_terjual[pilihan]
        print(f"\nDetail Tiket '{tiket['id']}':")
        print("+--------------------------------------------+")
        print("|                 TIKET BIOSKOP              |")
        print("+--------------------------------------------+")
        print(f"| ID Tiket : {tiket['id']}  |")
        print(f"| Film     : {tiket['film']}    |")
        print(f"| Tanggal  : {tiket['tanggal']} |")
        print("+--------------------------------------------+")
        print("|   Terima kasih telah membeli tiket Anda!   |")
        print("+--------------------------------------------+")

        print("\n--- Detail Tiket ---")
        print("\nDaftar Tiket")
        for i, tiket in enumerate(tiket_terjual, 1):
            print(f"{i}. ID: {tiket['id']}")
    else:
        print("Pilihan tidak valid.")

def hapus_tiket():
    tampilkan_tiket()
    pilihan = input("Masukkan ID tiket yang ingin dihapus: ")
    for tiket in tiket_terjual:
        if tiket["id"] == pilihan:
            tiket_terjual.remove(tiket)
            print(f"Tiket dengan ID {pilihan} berhasil dihapus.")
            return
    print("ID tiket tidak ditemukan.")

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah film")
        print("2. Hapus film")
        print("3. Daftar Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            tambah_film()
        elif pilihan == "2":
            hapus_film()
        elif pilihan == "3":
            menu_tiket_admin()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def menu_tiket_admin():
    while True:
        print("\n--- Daftar Tiket ---")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            tampilkan_tiket()
        elif pilihan == "2":
            lihat_detail_tiket()
        elif pilihan == "3":
            hapus_tiket()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def menu_utama():
    while True:
        print("\n--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input("Pilih peran (1/2/3): ")

        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu_utama()
