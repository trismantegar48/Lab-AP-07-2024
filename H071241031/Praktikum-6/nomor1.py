# Inventory Gudang 

inventory = {}

def tambah_barang():
    kode = input("Masukkan kode barang: ")
    if kode in inventory:
        print("Barang dengan kode ini sudah ada.")
    else:
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))
        harga = float(input("Masukkan harga barang: "))
        inventory[kode] = {"nama": nama, "jumlah": jumlah, "harga": harga}
        print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    if kode in inventory:
        del inventory[kode]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_daftar_barang():
    if not inventory:
        print("Inventory kosong.")
    else:
        print("Daftar Barang di Inventory:")
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")

def cari_barang():
    kode = input("Masukkan kode barang yang ingin dicari: ")
    if kode in inventory:
        data = inventory[kode]
        print(f"Barang ditemukan - Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Barang tidak ditemukan.")

def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    if kode in inventory:
        nama = input("Masukkan nama baru barang: ")
        jumlah = int(input("Masukkan jumlah baru barang: "))
        harga = float(input("Masukkan harga baru barang: "))
        inventory[kode] = {"nama": nama, "jumlah": jumlah, "harga": harga}
        print("Data barang berhasil diupdate.")
    else:
        print("Barang tidak ditemukan.")

def menu():
    while True:
        print("\n=== Menu Inventory Gudang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_daftar_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
menu()