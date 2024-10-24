import os
import datetime

os.makedirs('films',  exist_ok=True)
os.makedirs('tickets',  exist_ok=True)

def tampilkan_menu():
    print("\n=== Sistem Pemesanan Tiket Bioskop ===")
    print("1. Admin")
    print("2. Pengunjung")
    print("3. Keluar")

def tampilan_menu_admin():
    print("\n=== Menu Admin ===")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Tampilkan Daftar Film")
    print("4. Daftar Tiket")
    print("5. Kembali")

def tampilan_daftar_tiket():
    print("\n=== Daftar Tiket ===")
    print("1. Lihat Daftar Tiket")
    print("2. Lihat Detail Tiket")
    print("3. Hapus Tiket")
    print("4. Kembali")

def tampilan_menu_pengunjung():
    print("\n=== Menu Pengunjung ===")
    print("1. Daftar Film")
    print("2. Beli Tiket")
    print("3. Kembali")

def tambah_film():
    while True:
        print("\n=== Tambah Film ===")
        nama_film = input('Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ')
        if nama_film == '':
            print('Kembali ke menu admin')
            break
        else:
            file_path = os.path.join('films', f"{nama_film}.txt")
            if os.path.exists(file_path):
                print(f"Film '{nama_film}' sudah tersedia.")
            else:
                try:
                    with open(os.path.join('films', "films.txt"), 'a') as f:
                        f.write(f'{nama_film}\n')
                    print(f"Film '{nama_film}' berhasil ditambahkan.")
                except IOError:
                    print("Terjadi kesalahan saat menambahkan film.")

def hapus_film():
    while True:
        print("\n=== Hapus Film ===")
        with open(os.path.join('films', "films.txt"), 'r') as f:
            film_title = f.readlines()
        
        print("Daftar Film:")
        for index,film in enumerate(film_title, start=1):
            print(f"{index}. {film.strip()}")
        print("0. Kembali")
        try:
            pilihan = int(input("\nMasukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
            if pilihan == 0:
                break  
            elif 1 <= pilihan <= len(film_title):
                film_dipilih = film_title[pilihan - 1]

                try:
                    film_title.pop(pilihan-1)
                    with open(os.path.join('films', "films.txt"), 'w') as f:
                        f.writelines(film_title)
                    print(f"Film '{film_dipilih}' berhasil dihapus."
                          )
                except IOError:
                    print(f"Pilihan tidak valid.")
            else:
                print("Pilihan tidak valid. Silakan pilih nomor yang ada di daftar.")
        except ValueError:
            print("Pilihan harus berupa angka.")

def daftar_film():
    print("\n=== Daftar Film ===")
    film_files = os.listdir('films')
    if film_files:
        with open(os.path.join('films', "films.txt"), 'r') as f:
            film_title = f.readlines()
        
        print("Daftar Film:")
        for index,film in enumerate(film_title, start=1):
            print(f"{index}. {film.strip()}")
    else:
        print("Belum ada film yang tersedia.")

def daftar_tiket():
    while True:
        tampilan_daftar_tiket()
        try:
            pilihan = int(input("Pilih Menu (1/2/3/4): "))
            if pilihan == 1:
                lihat_daftar_tiket()
            elif pilihan == 2:
                lihat_detail_tiket()
            elif pilihan == 3:
                hapus_tiket()
            elif pilihan == 4:
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan harus angka.")

def lihat_daftar_tiket():
    print("\n=== Daftar Tiket ===")
    ticket_files = os.listdir('tickets')

    if ticket_files:
        print("Daftar Tiket:")
        for index, ticket in enumerate(ticket_files, start=1):
            print(f"{index}. {ticket.replace('.txt', '')}")
    else:
        print("Tidak ada tiket yang tersedia.")

def lihat_detail_tiket():
    print("\n=== Detail Tiket ===")
    ticket_files = os.listdir('tickets')

    while True:
        print("Daftar Tiket:")
        for index, ticket in enumerate(ticket_files, start=1):
            print(f"{index}. {ticket.replace('.txt', '')}")
        print("0. Kembali")

        try:
            pilihan = int(input("\nPilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): "))
            if pilihan == 0:
                break 
            elif 1 <= pilihan <= len(ticket_files):
                ticket_dipilih = ticket_files[pilihan - 1]
                ticket_path = os.path.join('tickets', ticket_dipilih)
                with open(ticket_path, 'r') as f:
                    detail_tiket = f.read()
                print(f"\nDetail Tiket {ticket_dipilih}:")
                print(detail_tiket)
            else:
                print("Pilihan tidak valid. Silakan pilih nomor yang ada di daftar.")
        except ValueError:
            print("Pilihan harus berupa angka.")


def hapus_tiket():
    print("\n=== Hapus Tiket ===")
    
    while True:
        ticket_files = os.listdir('tickets') 
        print("Daftar Tiket:")
        for index, ticket in enumerate(ticket_files, start=1):
            print(f"{index}. {ticket.replace('.txt', '')}")
        print("0. Kembali")

        try:
            pilihan = int(input("\nMasukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
            if pilihan == 0:
                break  
            elif 1 <= pilihan <= len(ticket_files):
                ticket_dipilih = ticket_files[pilihan - 1]
                ticket_path = os.path.join('tickets', ticket_dipilih) 
                try:
                    os.remove(ticket_path)
                    print(f"Tiket '{ticket_dipilih.replace('.txt', '')}' berhasil dihapus.")
                except IOError:
                    print(f"Pilihan tidak valid")
            else:
                print("Pilihan tidak valid. Silakan pilih nomor yang ada di daftar.")
        except ValueError:
            print("Pilihan harus berupa angka.")


def generate_ticket_id():
    return "TICK" + datetime.datetime.now().strftime("%d%m%Y%H%M%S")

def simpan_tiket(nama_film):
    ticket_id = generate_ticket_id()
    ticket_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ticket_info = (
    f"+-------------------------------------+\n"
    f"|           TIKET BIOSKOP             |\n"
    f"+-------------------------------------+\n"
    f"| ID Tiket  : {ticket_id}       |\n"
    f"| Film      : {nama_film}             |\n"
    f"| Tanggal   : {ticket_date}      |\n"
    f"+-------------------------------------+\n"
    f"|   Terima kasih telah membeli tiket   |\n"
    f"|               Anda!                 |\n"
    f"+-------------------------------------+\n"
    )
    ticket_file = os.path.join('tickets', f"{ticket_id}.txt")
    with open(ticket_file, 'w') as f:
        f.write(ticket_info)
    print(f"Tiket berhasil disimpan dengan ID: {ticket_id}")

def beli_tiket():
    print("\n=== Beli Tiket ===")
    film_files = os.listdir('films')

    if film_files:
        print("Daftar Film:")
        with open(os.path.join('films', "films.txt"), 'r') as f:
            film_title = f.readlines()
     
        for index,film in enumerate(film_title, start=1):
            print(f"{index}. {film.strip()}")
        print("0. Kembali")

        try:
            
            pilihan = int(input("\nPilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
            with open(os.path.join('films', "films.txt"), 'r') as f:
                film_title = f.readlines()
            if pilihan == 0:
                return 
            elif 1 <= pilihan <= len(film_title):
                film_dipilih = film_title[pilihan - 1]
                nama_film = film_dipilih.replace("\n", '')
              
                simpan_tiket(nama_film)
            else:
                print("Pilihan tidak valid. Silakan pilih nomor yang ada di daftar.")
        except ValueError:
            print("Pilihan harus berupa angka.")
    else:
        print("Tidak ada film yang tersedia.")

def menu_admin():
    while True:
        tampilan_menu_admin()
        try:
            pilihan = int(input("Pilih Menu (1/2/3/4/5): "))
            if pilihan == 1:
                tambah_film()
            elif pilihan == 2:
                hapus_film()
            elif pilihan == 3:
                daftar_film()
            elif pilihan == 4:
                daftar_tiket()
            elif pilihan == 5:
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan harus angka.")

def menu_pengunjung():
    while True:
        tampilan_menu_pengunjung()
        try:
            pilihan = int(input("Pilih Menu (1/2/3/4): "))
            if pilihan == 1:
                daftar_film()
            elif pilihan == 2:
                beli_tiket()
            elif pilihan == 3:
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan harus angka.")

def main():
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih Peran (1/2/3): "))
            if pilihan == 1:
                menu_admin()
            elif pilihan == 2:
                menu_pengunjung()
            elif pilihan == 3:
                print("Terima kasih telah menggunakan sistem ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan harus angka.")


main()
