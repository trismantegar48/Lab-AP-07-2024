import datetime
import os

films = []
tickets = []

def buat_folder():
    if not os.path.exists("TUGAS PRAKTIKUM LAB 7/01FILMS"):
        os.makedirs("TUGAS PRAKTIKUM LAB 7/01FILMS")
    if not os.path.exists("TUGAS PRAKTIKUM LAB 7/01TICKETS"):
        os.makedirs("TUGAS PRAKTIKUM LAB 7/01TICKETS")
    film_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01FILMS", "films.txt")
    if not os.path.exists(film_file_path):
        with open(film_file_path, "w") as file:
            file.write("")

def tambah_film(judul_film):
    films.append(judul_film)
    film_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01FILMS", "films.txt")
    with open(film_file_path, "a") as file:
        file.write(f"{judul_film}\n")
    print(f"Film '{judul_film}' berhasil ditambahkan!")

def hapus_film():
    if films:
        print("Daftar Film:")
        for idx, film in enumerate(films, start=1):
            print(f"{idx}. {film}")
        index_film = input_integer("Pilih nomor film yang akan dihapus: ")
        if index_film is None:
            print("Dibatalkan.")
            return
        if 1 <= index_film <= len(films):
            judul_film = films.pop(index_film - 1)
            film_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01FILMS", "films.txt")
            with open(film_file_path, "r") as file:
                lines = file.readlines()
            with open(film_file_path, "w") as file:
                for line in lines:
                    if line.strip() != judul_film:
                        file.write(line)
            print(f"Film '{judul_film}' berhasil dihapus!")
        else:
            print("Pilihan tidak valid!")
    else:
        print("Tidak ada film yang tersedia.")

def tampilkan_daftar_film():
    film_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01FILMS", "films.txt")
    if os.path.exists(film_file_path):
        with open(film_file_path, "r") as file:
            lines = file.readlines()
            films.clear()
            films.extend([line.strip() for line in lines])
    
    if films:
        print("\n--------Daftar Film----------")
        for idx, film in enumerate(films, start=1):
            print(f"{idx}. {film}")
    else:
        print("Tidak ada film yang tersedia.")

def beli_tiket(index_film, nama_pengunjung):
    if 1 <= index_film <= len(films):
        judul_film = films[index_film - 1]
        id_tiket = generate_ticket_id()
        tiket = {
            "id": id_tiket,
            "film": judul_film,
            "pengunjung": nama_pengunjung,
            "tanggal": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        tickets.append(tiket)
        simpan_informasi_tiket(tiket)
        print(f"Tiket untuk '{judul_film}' berhasil dibeli oleh {nama_pengunjung}!")
    else:
        print("Film tidak ditemukan!")

def simpan_informasi_tiket(tiket):
    tiket_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01TICKETS", f"{tiket['id']}.txt")
    with open(tiket_file_path, "w") as file:
        file.write(f"+----------------------------------+\n")
        file.write(f"|          TIKET BIOSKOP           |\n")
        file.write(f"+----------------------------------+\n")
        file.write(f"  ID Tiket  : {tiket['id']}         \n")
        file.write(f"  Film      : {tiket['film'][:20]:<20} \n")
        file.write(f"  Pengunjung: {tiket['pengunjung']:<20} \n")
        file.write(f"  Tanggal   : {tiket['tanggal']}    \n")
        file.write(f"+----------------------------------+\n")
        file.write(f"\nTerima kasih telah membeli tiket Anda!\n")
    print("Informasi tiket berhasil disimpan!")

def tampilkan_daftar_tiket():
    while True:
        print("\n--- Daftar Tiket ---")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("Tekan 'Enter' Untuk Kembali")
        pilihan = input_integer("Pilih opsi (1/2/3/4): ")

        if pilihan is None:
            print("Dibatalkan.")
            return
        if pilihan == 1:
            tiket_folder_path = "TUGAS PRAKTIKUM LAB 7/01TICKETS"
            tiket_files = [f for f in os.listdir(tiket_folder_path) if os.path.isfile(os.path.join(tiket_folder_path, f))]
            if tiket_files:
                print("Daftar Tiket:")
                for tiket_file in tiket_files:
                    tiket_file_path = os.path.join(tiket_folder_path, tiket_file)
                    with open(tiket_file_path, "r") as file:
                        lines = file.readlines()
                        id_tiket = lines[3].split(":")[1].strip()
                        film = lines[4].split(":")[1].strip()
                        pengunjung = lines[5].split(":")[1].strip() if len(lines) > 5 else "Tidak diketahui"
                        print(f"ID: {id_tiket}, Film: {film}, Pengunjung: {pengunjung}")
            else:
                print("Tidak ada tiket yang telah dibeli.")
        elif pilihan == 2:
            id_tiket = input("Masukkan ID tiket: ")
            if not id_tiket:
                print("Dibatalkan.")
                continue
            tiket_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01TICKETS", f"{id_tiket}.txt")
            if os.path.exists(tiket_file_path):
                with open(tiket_file_path, "r") as file:
                    print(file.read())
            else:
                print("Tiket tidak ditemukan!")
        elif pilihan == 3:
            id_tiket = input("Masukkan ID tiket yang akan dihapus: ")
            if not id_tiket:
                print("Dibatalkan.")
                continue
            hapus_tiket(id_tiket)
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def hapus_tiket(id_tiket):
    tiket = next((t for t in tickets if t["id"] == id_tiket), None)
    if tiket:
        tickets.remove(tiket)
        tiket_file_path = os.path.join("TUGAS PRAKTIKUM LAB 7/01TICKETS", f"{id_tiket}.txt")
        if os.path.exists(tiket_file_path):
            os.remove(tiket_file_path)
        print(f"Tiket dengan ID '{id_tiket}' berhasil dihapus!")
    else:
        print("Tiket tidak ditemukan!")

def generate_ticket_id():
    now = datetime.datetime.now()
    return f"TICK{now.strftime('%d%m%Y%H%M%S')}"

def input_integer(prompt):
    while True:
        try:
            value = input(prompt)
            if value == "":
                return None
            return int(value)
        except ValueError:
            print("Input tidak valid, masukkan angka!")

def menu_utama():
    while True:
        print("\n--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input_integer("Pilih peran (1/2/3): ")

        if pilihan is None:
            print("Dibatalkan.")
            continue
        if pilihan == 1:
            menu_admin()
        elif pilihan == 2:
            menu_pengunjung()
        elif pilihan == 3:
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Tampilkan Daftar Tiket")
        print("Tekan 'Enter' Untuk Kembali")
        pilihan = input_integer("Pilih opsi (1-4): ")

        if pilihan is None:
            print("Dibatalkan.")
            return
        if pilihan == 1:
            judul_film = input("Masukkan judul film: ")
            if not judul_film:
                print("Dibatalkan.")
                continue
            tambah_film(judul_film)
        elif pilihan == 2:
            hapus_film()
        elif pilihan == 3:
            tampilkan_daftar_tiket()
        else:
            print("Pilihan tidak valid, coba lagi.")

def menu_pengunjung():
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("Tekan 'Enter' Untuk Kembali")
        pilihan = input_integer("Pilih opsi (1-3): ")

        if pilihan is None:
            print("Dibatalkan.")
            return
        if pilihan == 1:
            tampilkan_daftar_film()
        elif pilihan == 2:
            if not films:
                print("Tidak ada film yang tersedia.")
            else:
                tampilkan_daftar_film()
                index_film = input_integer("Pilih nomor film yang ingin dibeli: ")
                if index_film is None:
                    print("Dibatalkan.")
                    continue
                nama_pengunjung = input("Masukkan nama pengunjung: ")
                if not nama_pengunjung:
                    print("Dibatalkan.")
                    continue
                beli_tiket(index_film, nama_pengunjung)
        else:
            print("Pilihan tidak valid, coba lagi.")

buat_folder()
menu_utama()
