import os
import random
from datetime import datetime

os.system("cls")

list_film = []
daftar_nama_tiket = []

def menu_admin():
    while True:
        print(" Menu Admin ".center(27, "="))
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali")

        opsi = input("Pilih Fungsi (1/2/3/4) : ")

        match opsi:
            case "1" : tambah_film()
            case "2" : hapus_film()
            case "3" : daftar_tiket()
            case "4" : menu_awal()

def menu_pengunjung():
    while True:
        print(" Pengunjung ".center(27, "="))
        print("1. Lihat Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")

        opsi = input("Pilih Fungsi (1/2/3) : ")

        match opsi:
            case "1" : daftar_film()
            case "2" : beli_tiket()
            case "3" : menu_awal()

def menu_awal():
    while True:
        print(" Sistem Pemesanan Tiket Bioskop ".center(40, "="))
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        
        opsi = input("Pilih Peran (1/2/3) : ")

        match opsi:
            case "1" : menu_admin()
            case "2" : menu_pengunjung()
            case "3" : break

def tambah_film():
    while True:
        nama_film = input("Masukkan Nama Film Yang Ingin Ditambahkan (Atau Tekan Enter Untuk Kembali) : ")
        if nama_film == "":
            break
        list_film.append({"nama_film" : nama_film})
        print(f"Film {nama_film} Berhasil Ditambahkan\n")

def hapus_film():
    while True:
        print(" Hapus Film ".center(18, "="))
        if not list_film:
            print("Tidak ada film yang tersedia.")
            break
            
        for i, item in enumerate(list_film, 1):
            print(f"{i}. {item['nama_film']}")
        print("0. Kembali")

        hapus_nomor = int(input("Masukkan Nomor Film Yang Ingin Dihapus (Atau 0 Untuk Kembali) : "))

        if hapus_nomor == 0:
            break
        elif hapus_nomor in range(1, len(list_film) + 1):
            film_dihapus = list_film.pop(hapus_nomor - 1)
            print(f"Film {film_dihapus['nama_film']} Berhasil Dihapus\n")
        else:
            print("Nomor Film Tidak Valid, Silakan Coba Lagi.\n")

def daftar_film():
    if not list_film:
        print("Tidak ada film yang tersedia saat ini.")
        return
        
    print("Daftar Film : ")
    for i, item in enumerate(list_film, 1):
        print(f"{i}. {item['nama_film']}")
    print("0. Kembali")

def beli_tiket():
    TOTAL_TICKETS = 6
    NUM_ROWS = 2
    SEATS_PER_ROW = 3
    used_seats = {}

    while True:
        try:
            if not list_film:
                print("\nMaaf, tidak ada film yang tersedia saat ini.")
                print("Silakan tunggu admin menambahkan film.")
                return
                
            print("\nDaftar Film : ")
            for i, item in enumerate(list_film, 1):
                print(f"{i}. {item['nama_film']}")
            print("0. Kembali")

            input_tiket = input("Pilih Nomor Film Yang Ingin Ditonton (Atau 0 Untuk Kembali) : ")
            if not input_tiket.isdigit():
                print("Mohon masukkan angka saja")
                continue
                
            input_tiket = int(input_tiket)
            if input_tiket == 0:
                break
            if input_tiket < 1 or input_tiket > len(list_film):
                print("Pilih nomor film yang tersedia")
                continue

            quantity = input("Masukkan Jumlah Tiket yang ingin dibeli: ")
            if not quantity.isdigit():
                print("Jumlah tiket harus berupa angka")
                continue
                
            quantity = int(quantity)
            if quantity < 1:
                print("Jumlah tiket minimal 1")
                continue
            if quantity > TOTAL_TICKETS:
                print(f"Maksimal pembelian {TOTAL_TICKETS} tiket per teater")
                continue

            theater_number = input_tiket - 1
            film_name = list_film[theater_number]["nama_film"]
            date = datetime.now().date()
            show_time = random.choice(['12:15', '14:20', '16:25', '18:30', '20:35'])

            theater_key = (theater_number, date, show_time)
            if theater_key not in used_seats:
                used_seats[theater_key] = set()

            available_seats = TOTAL_TICKETS - len(used_seats[theater_key])
            if available_seats < quantity:
                print(f"Maaf, hanya tersisa {available_seats} kursi untuk jadwal ini")
                continue

            seats = []
            for _ in range(quantity):
                attempts = 0
                while attempts < 10:
                    seat_row = random.randint(1, NUM_ROWS)
                    seat_column = random.randint(1, SEATS_PER_ROW)
                    seat = (seat_row, seat_column)
                    
                    if seat not in used_seats[theater_key]:
                        used_seats[theater_key].add(seat)
                        seats.append(f"{seat_row}-{seat_column}")
                        break
                    attempts += 1
                else:
                    print("Error: Tidak bisa menemukan kursi yang tersedia")
                    continue

            price = 40000 if date.weekday() >= 5 else 35000
            total_price = quantity * price

            format_ticket = f"TICK{datetime.now().strftime('%d%m%Y%H%M%S')}"

            print("\nLayout Kursi:")
            print("  1 2 3")
            for row in range(1, NUM_ROWS + 1):
                print(f"{row}", end=" ")
                for col in range(1, SEATS_PER_ROW + 1):
                    if (row, col) in used_seats[theater_key]:
                        print("X", end=" ")
                    else:
                        print("O", end=" ")
                print()

            saved_tickets = []
            for i, seat_number in enumerate(seats):
                ticket_filename = f"{format_ticket}_{i+1}"
                try:
                    with open(f"{ticket_filename}.txt", "w", encoding='utf-8') as file:
                        file.write(f"""
╔══════════════════════════════════════╗
║ 𝙕𝙀𝙀𝙊𝙎𝙆𝙊𝙋                           ║
╠══════════════════════════════════════╣
║ {film_name:<36} ║
║                                      ║
║ Date: {date}  Time: {show_time}      ║
║                                      ║
║ Seat: {seat_number:<6}                       ║
║                                      ║
║ Theater {theater_number + 1:<2}                          ║
║                                      ║
║ Price: {price} IDR                   ║
╠══════════════════════════════════════╣
║ ║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║ ║
╚══════════════════════════════════════╝
""")
                    saved_tickets.append(ticket_filename)
                except IOError:
                    print(f"Error: Gagal menyimpan tiket {ticket_filename}")
                    continue

            daftar_nama_tiket.extend(saved_tickets)

            print(f"\nPembelian Berhasil!")
            print(f"ID Tiket: {format_ticket}")
            print(f"Total Pembayaran: Rp {total_price:,}")
            print("File tiket telah disimpan")

        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            continue

def daftar_tiket():
    while True:
        print("\nDaftar Tiket:")
        
        if not daftar_nama_tiket:
            print("Tidak ada tiket yang ditemukan.")
            return

        for i, nama_tiket in enumerate(daftar_nama_tiket, 1):
            print(f"{i}. {nama_tiket}")

        print("0. Kembali")

        pilihan = input("\nPilih Nomor Tiket Yang Ingin Dilihat (Atau 0 Untuk Kembali): ").strip()
        
        if not pilihan.isdigit():
            print("Input tidak valid. Harap masukkan angka.")
            continue
            
        pilihan = int(pilihan)
        
        if pilihan == 0:
            break
            
        if pilihan < 1 or pilihan > len(daftar_nama_tiket):
            print("Pilihan tidak valid. Silakan pilih nomor yang ada.")
            continue

        try:
            nama_tiket = daftar_nama_tiket[pilihan - 1]
            with open(f"{nama_tiket}.txt", "r", encoding='utf-8') as file:
                print("\nDetail Tiket:")
                print(file.read())
                input("\nTekan Enter untuk melanjutkan...")
        except FileNotFoundError:
            print(f"Tiket {nama_tiket} tidak ditemukan.")
            daftar_nama_tiket.remove(nama_tiket)
        except UnicodeDecodeError:
            try:
                with open(f"{nama_tiket}.txt", "r", encoding='latin-1') as file:
                    print("\nDetail Tiket:")
                    print(file.read())
                    input("\nTekan Enter untuk melanjutkan...")
            except Exception as e:
                print(f"Tidak dapat membaca file tiket: {str(e)}")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")

menu_awal()