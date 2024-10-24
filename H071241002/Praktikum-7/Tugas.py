import datetime
import os

daftar_film = []
daftar_tiket = []
folder_tiket = "tiket"
os.makedirs(folder_tiket, exist_ok=True)

def tambah_film(judul):
    daftar_film.append(judul)
    print(f"Film '{judul}' berhasil ditambahkan.")

def hapus_film(judul):
    if judul in daftar_film:
        daftar_film.remove(judul)
        print(f"Film '{judul}' berhasil dihapus.")
    else:
        print(f"Film '{judul}' tidak ditemukan.")

def tampilkan_film():
    if not daftar_film:
        print("Tidak ada film yang tersedia.")
    else:
        print("Daftar film:")
        for index, film in enumerate(daftar_film):
            print(f"{index + 1}. {film}")

def beli_tiket(judul_film):
    id_tiket = buat_id_tiket()
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    tiket = {'id': id_tiket, 'film': judul_film, 'timestamp': timestamp}
    daftar_tiket.append(tiket)
    simpan_info_tiket(tiket)
    print(f"Tiket berhasil dibeli. ID tiket anda: {id_tiket}")
    print(f"File tiket telah dibuat: {folder_tiket}/{id_tiket}.txt")

def buat_id_tiket():
    sekarang = datetime.datetime.now()
    return f"TICK{sekarang.strftime('%d%m%Y%H%M%S')}"

def simpan_info_tiket(tiket):
    with open(f"{folder_tiket}/{tiket['id']}.txt", 'w') as f:
        f.write("\n" + "-" * 45 + "\n")
        f.write("          TIKET BIOSKOP          \n")
        f.write("-" * 45 + "\n")
        f.write(f"ID Tiket   : {tiket['id']}\n")
        f.write(f"Film       : {tiket['film']}\n")
        f.write(f"Tanggal    : {tiket['timestamp']}\n")
        f.write("-" * 45 + "\n")
        f.write("     Terima kasih telah membeli tiket!     \n")
        f.write("-" * 45 + "\n")


def tampilkan_tiket():
    if not daftar_tiket:
        print("Tidak ada tiket yang telah dibeli.")
    else:
        print("Daftar tiket:")
        for index, tiket in enumerate(daftar_tiket):
            print(f"{index + 1}. {tiket['id']}")

def tampilkan_detail_tiket(id_tiket):
    for tiket in daftar_tiket:
        if tiket['id'] == id_tiket:
            bingkai = "-" * 45
            print("\n" + bingkai)
            print("          TIKET BIOSKOP          ".center(45))
            print(bingkai)
            print(f"ID Tiket        : {tiket['id']}")
            print(f"Film            : {tiket['film']}")
            print(f"Tanggal         : {tiket['timestamp']}")
            print("\n" + bingkai)
            print("     Terima kasih telah membeli tiket anda!     ".center(45))
            print(bingkai)
            return
    print(f"Tiket '{id_tiket}' tidak ditemukan.")

def hapus_tiket(id_tiket):
    global daftar_tiket
    daftar_tiket = [tiket for tiket in daftar_tiket if tiket['id'] != id_tiket]
    print(f"Tiket '{id_tiket}' berhasil dihapus.")

def menu_admin():
    while True:
        print("--- Menu Admin ---")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali")
        opsi = input("Pilih opsi (1/2/3/4): ")

        if opsi == '1':
            judul = input("--- Tambah Film ---\nMasukkan nama film: ")
            if judul:
                tambah_film(judul)
        elif opsi == '2':
            tampilkan_film()
            judul = input("--- Hapus Film ---\nMasukkan nama film yang ingin dihapus: ")
            if judul:
                hapus_film(judul)
        elif opsi == '3':
            menu_manajemen_tiket()
        elif opsi == '4':
            break

def menu_manajemen_tiket():
    while True:
        print("--- Daftar Tiket ---")
        print("1. Lihat daftar tiket")
        print("2. Lihat detail tiket")
        print("3. Hapus tiket")
        print("4. Kembali")
        opsi = input("Pilih opsi (1/2/3/4): ")

        if opsi == '1':
            tampilkan_tiket()
        elif opsi == '2':
            tampilkan_tiket()
            nomor_tiket = input("Pilih nomor tiket yang ingin dilihat: ")
            if nomor_tiket.isdigit() and 0 < int(nomor_tiket) <= len(daftar_tiket):
                tampilkan_detail_tiket(daftar_tiket[int(nomor_tiket) - 1]['id'])
        elif opsi == '3':
            tampilkan_tiket()
            nomor_tiket = input("Pilih nomor tiket yang ingin dihapus: ")
            if nomor_tiket.isdigit() and 0 < int(nomor_tiket) <= len(daftar_tiket):
                hapus_tiket(daftar_tiket[int(nomor_tiket) - 1]['id'])
        elif opsi == '4':
            break

def menu_pengunjung():
    while True:
        print("--- Menu Pengunjung ---")
        print("1. Lihat daftar film")
        print("2. Beli tiket")
        print("3. Kembali")
        opsi = input("Pilih opsi (1/2/3): ")

        if opsi == '1':
            tampilkan_film()
        elif opsi == '2':
            tampilkan_film()
            pilihan_film = input("Pilih nomor film yang ingin ditonton: ")
            if pilihan_film.isdigit() and 0 < int(pilihan_film) <= len(daftar_film):
                beli_tiket(daftar_film[int(pilihan_film) - 1])
        elif opsi == '3':
            break

def menu_utama():
    while True:
        print("--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input("Pilih peran (1/2/3): ")

        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_utama()
