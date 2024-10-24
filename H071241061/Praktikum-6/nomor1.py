def tambah_barang(inventory):   
    kode_barang = input("Masukkan kode barang: ")
    if kode_barang in inventory:
        print(f"Barang dengan kode '{kode_barang}' sudah ada.")
        return
    nama = input("Masukkan nama barang: ")

    while True:
        try:
            jumlah = int(input("Masukkan jumlah barang: "))
            break
        except ValueError:
            print("Jumlah barang harus angka.")

    while True:
        try:
            harga = int(input("Masukkan harga barang per unit: "))
            break
        except ValueError:
            print("Harga barang harus angka.")

    inventory[kode_barang] = {
        'nama': nama,
        'jumlah': jumlah,
        'harga': harga
    }
    print(f"Barang berhasil ditambahkan.")
            

def hapus_barang(inventory):
   
    kode_barang = input("Masukkan kode barang yang akan dihapus: ")
    if kode_barang in inventory:
        del inventory[kode_barang]
        print(f"Barang berhasil dihapus.")
    else:
        print(f"Barang dengan kode '{kode_barang}' tidak ditemukan.")
         
      

def tampilkan_daftar_barang(inventory):
    if inventory:
        print("\nDaftar Barang:")
        for kode_barang, data in inventory.items():
            print(f"- Kode: {kode_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Tidak ada barang dalam inventory.")

def cari_barang(inventory):
    while True:
        try:
            cara_cari = int(input("Cari barang berdasarkan (1) Kode atau (2) Nama: "))
            if cara_cari == 1:
                kode_barang = input('Masukkan kode barang: ')
                if kode_barang in inventory:
                    data = inventory[kode_barang]
                    print(f"Barang ditemukan: Kode: {kode_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
                else:
                    print(f"Barang dengan kode '{kode_barang}' tidak ditemukan.")
                
            elif cara_cari == 2:
                nama_barang = input('Masukkan nama barang: ')
                ditemukan = False
                for kode_barang, data in inventory.items():
                    if data['nama'].lower() == nama_barang.lower():
                        print(f"Barang ditemukan: Kode: {kode_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
                        ditemukan = True
                        break
                if not ditemukan:
                    print(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")
            else:
                print("Pilihan tidak valid.")
            break
        except ValueError:
            print("Pilihan harus berupa angka.")

def update_barang(inventory):
   
    kode_barang = input("Masukkan kode barang yang akan diupdate: ")
    if kode_barang in inventory:
        while True:
            try:
                jumlah = int(input(f"Masukkan jumlah baru: "))
                break
            except ValueError:
                print("Jumlah harus angka.")
        while True:
            try:
                harga = int(input(f"Masukkan harga per unit baru: "))
                break
            except ValueError:
                print("Harga harus angka.")
        inventory[kode_barang]['jumlah'] = jumlah
        inventory[kode_barang]['harga'] = harga
        print(f"Data barang telah diperbarui.")
    else:
        print(f"Barang dengan kode '{kode_barang}' tidak ditemukan.")
    
def main():
    inventory = {}
    def tampilkan_menu():
        print("\n=== Menu Inventori Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")

    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-6): "))
            if pilihan == 1:
                tambah_barang(inventory)
            elif pilihan == 2:
                hapus_barang(inventory)
            elif pilihan == 3:
                tampilkan_daftar_barang(inventory)
            elif pilihan == 4:
                cari_barang(inventory)
            elif pilihan == 5:
                update_barang(inventory)
            elif pilihan == 6:
                print("Program selesai. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan harus angka.")

main()