import json

inventory = {}

# Load inventory from file if exists
try:
    with open('TUGAS PRAKTIKUM LAB 6/inventory.json', 'r') as file:
        inventory = json.load(file)
except FileNotFoundError:
    inventory = {}

def save_inventory():
    with open('TUGAS PRAKTIKUM LAB 6/inventory.json', 'w') as file:
        json.dump(inventory, file)

def print_menu():
    print("\nMenu Inventory Barang:")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

while True:
    print_menu()
    choice = input("Silakan masukkan pilihan Anda: ")

    if choice == '1':
        kode_item = input("Masukkan kode barang: ").strip().lower()
        nama_item = input("Masukkan nama barang: ").strip().lower()
        jumlah_item = input("Masukkan jumlah barang: ").strip()
        harga_item = input("Masukkan harga per unit: ").strip()
        inventory[kode_item] = {
            'nama': nama_item,
            'jumlah': jumlah_item,
            'harga': harga_item
        }
        save_inventory()
        print(f"Barang dengan kode {kode_item} dan nama {nama_item} telah ditambahkan dengan jumlah {jumlah_item} dan harga {harga_item}.")

    elif choice == '2':
        kode_item = input("Masukkan kode barang yang ingin dihapus: ").strip()
        if kode_item in inventory:
            del inventory[kode_item]
            save_inventory()
            print(f"Barang dengan kode {kode_item} telah dihapus dari inventory.")
        else:
            print(f"Barang dengan kode {kode_item} tidak ditemukan dalam inventory.")

    elif choice == '3':
        if inventory:
            print("\n---------------Daftar Barang---------------")
            for kode, data in inventory.items():
                print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
        else:
            print("Inventory kosong.")

    elif choice == '4':
        search_choice = input("Cari berdasarkan (1) Kode atau (2) Nama: ").strip()
        if search_choice == '1':
            kode_item = input("Masukkan kode barang: ").strip()
            if kode_item in inventory:
                data = inventory[kode_item]
                print(f"Kode: {kode_item}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']}")
            else:
                print(f"Barang dengan kode {kode_item} tidak ditemukan dalam inventory.")
        elif search_choice == '2':
            nama_item = input("Masukkan nama barang: ").strip().lower()
            found = False
            for kode, data in inventory.items():
                if data['nama'] == nama_item:
                    print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']}")
                    found = True
                    break
            if not found:
                print(f"Barang dengan nama {nama_item} tidak ditemukan dalam inventory.")
        else:
            print("Pilihan tidak valid. Silakan pilih (1) atau (2).")

    elif choice == '5':
        kode_item = input("Masukkan kode barang yang ingin diupdate: ").strip()
        if kode_item in inventory:
            jumlah_item_baru = input("Masukkan jumlah baru: ").strip()
            pen_update = input('apakah ingin mengupdate harga ? (y/n): ').strip().lower()
            if pen_update == "n" :
                inventory[kode_item]['jumlah'] = jumlah_item_baru
                inventory[kode_item]['harga'] = harga_item_baru
            elif pen_update == "y":
                harga_item_baru = input("Masukkan harga per unit baru: ").strip()
                inventory[kode_item]['jumlah'] = jumlah_item_baru
                inventory[kode_item]['harga'] = harga_item_baru
            save_inventory()
            print("Data barang berhasil diperbarui.")
        else:
            print(f"Barang dengan kode {kode_item} tidak ditemukan dalam inventory.")

    elif choice == '6':
        print("Anda telah keluar dari program.")
        break

    else:
        print("Maaf, pilihan yang Anda masukkan tidak tersedia. Silakan periksa kembali pilihan Anda.")