inventory_barang = {
    '001': {
        'nama': 'Pensil',
        'jumlah': 100,
        'harga': 1500
    },
    '002': {
        'nama': 'Buku',
        'jumlah': 50,
        'harga': 25000
    },
    '003': {
        'nama': 'Pulpen',
        'jumlah': 70,
        'harga' : 5000
    }
}

def tambah_barang():
    kode_barang = input("Masukkan kode barang: ")
    if kode_barang in inventory_barang:
        print("Kode barang sudah ada. Silakan masukkan kode barang yang berbeda.")
        return

    nama_barang = input("Masukkan nama barang: ")
    while True:
        try:
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            if jumlah_barang < 0:
                print("Jumlah barang tidak boleh negatif. Silakan masukkan angka yang benar.")
                continue  
            harga_per_unit = float(input("Masukkan harga per unit: "))
            if harga_per_unit < 0:
                print("Harga tidak boleh negatif. Silakan masukkan angka yang benar.")
                continue 
            inventory_barang[kode_barang] = {
                'nama': nama_barang,
                'jumlah': jumlah_barang,
                'harga': harga_per_unit
            }
            print("Barang berhasil ditambahkan.")
            break  
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar.")

def hapus_barang():
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    if kode_barang in inventory_barang:
        del inventory_barang[kode_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_barang():
    if not inventory_barang:
        print("Inventory kosong.")
    else:
        print("\nDaftar Barang:")
        for kode, data in inventory_barang.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']:.2f}")

def cari_barang():
    cari_berdasarkan = input("Cari berdasarkan (1) kode atau (2) nama: ")
    if cari_berdasarkan == '1':
        kode_barang = input("Masukkan kode barang: ")
        if kode_barang in inventory_barang:
            data = inventory_barang[kode_barang]
            print(f"Kode: {kode_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']:.2f}")
        else:
            print("Barang tidak ditemukan.")
    elif cari_berdasarkan == '2':
        nama_barang = input("Masukkan nama barang: ")
        found = False
        for kode, data in inventory_barang.items():
            if data['nama'].lower() == nama_barang.lower():
                print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']:.2f}")
                found = True
        if not found:
            print("Barang tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

def update_barang():
    tampilkan_barang()

    kode_barang = input("Masukkan kode barang yang ingin diupdate: ")
    if kode_barang in inventory_barang:
        while True:
            try:
                jumlah_barang = int(input("Masukkan jumlah baru: "))
                if jumlah_barang < 0:
                    print("Jumlah barang tidak boleh negatif. Silakan masukkan angka yang benar.")
                    continue  
                harga_per_unit = float(input("Masukkan harga per unit baru: "))
                if harga_per_unit < 0:
                    print("Harga tidak boleh negatif. Silakan masukkan angka yang benar.")
                    continue  
                
                inventory_barang[kode_barang]['jumlah'] = jumlah_barang
                inventory_barang[kode_barang]['harga'] = harga_per_unit
                print("Data barang berhasil diperbarui.")
                break  
            except ValueError:
                print("Input tidak valid. Harap masukkan angka yang benar.")
    else:
        print("Barang tidak ditemukan.")
        
while True:
    print("\n--- Menu Inventory ---")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        hapus_barang()
    elif pilihan == '3':
        tampilkan_barang()
    elif pilihan == '4':
        cari_barang()
    elif pilihan == '5':
        update_barang()
    elif pilihan == '6':
        print("Terima kasih telah menggunakan program inventory.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
