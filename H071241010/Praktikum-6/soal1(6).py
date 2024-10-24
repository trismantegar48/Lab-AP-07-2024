def tambah_barang(barang_list, barang):
    barang_list.append(barang)
    print("Barang berhasil ditambahkan!")


def hapus_barang(barang_list, kode_barang):
    for barang in barang_list:
        if barang['kode'] == kode_barang:
            barang_list.remove(barang)
            print("Barang berhasil dihapus.")
            return
    print("Inventory kosong.")


def tampilkan_barang(barang_list):
    if barang_list:
        for barang in barang_list:
            if 'harga' in barang:
                print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: Rp {barang['harga']:,.2f}")
            else:
                print("Harga tidak ditemukan.")
    else:
        print("Inventory kosong.")


def cari_barang(barang_list, kode_barang=None, nama_barang=None):
    if kode_barang:
        for barang in barang_list:
            if barang['kode'] == kode_barang:
                print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: Rp {barang['harga']:,.2f}")
                return
        print("Barang tidak ditemukan.")
    elif nama_barang:
        for barang in barang_list:
            if barang['nama'] == nama_barang:
                print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Harga: {barang['harga']}, Jumlah: {barang['jumlah']}")
                return
        print("Barang tidak ditemukan.")


def update_barang(barang_list, kode_barang, harga_baru, jumlah_baru):
    for barang in barang_list:
        if barang['kode'] == kode_barang:
            barang['harga'] = harga_baru
            barang['jumlah'] = jumlah_baru
            print("Data barang berhasil diperbarui.")
            return
    print("Barang tidak ditemukan.")


def inventory():
    barang_list = []
    while True:
        print("===Menu Inventory Barang===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == "1":
            kode = input("Masukkan kode barang: ")
            if not kode:
                print("Kode tidak boleh kosong.")
                continue
            nama = input("Masukkan nama barang: ")
            if not nama:
                print("Nama tidak boleh kosong.")
                continue
            try:
                jumlah = int(input("Masukkan jumlah barang: "))
                if jumlah < 0:
                    print("Jumlah tidak boleh minus.")
                    continue
            except ValueError:
                print("Jumlah harus berupa angka.")
                continue
            try:
                harga = float(input("Masukkan harga per unit: "))
                if harga < 0:
                    print("Harga tidak boleh minus.")
                    continue
            except ValueError:
                print("Harga harus berupa angka.")
                continue
            tambah_barang(barang_list, {'kode': kode, 'nama': nama, 'harga': harga, 'jumlah': jumlah})
        elif pilihan == "2":
            kode = input("Masukkan kode barang yang akan dihapus: ")
            hapus_barang(barang_list, kode)
        elif pilihan == "3":
            tampilkan_barang(barang_list)
        elif pilihan == "4":
            pilihan_cari = input("Cari berdasarkan (1) kode atau (2) Nama: ")
            if pilihan_cari == "1":
                kode = input("Masukkan kode barang: ")
                cari_barang(barang_list, kode_barang=kode)
            elif pilihan_cari == "2":
                nama = input("Masukkan nama barang: ")
                cari_barang(barang_list, nama_barang=nama)
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        elif pilihan == "5":
            kode = input("Masukkan kode barang yang ingin diupdate : ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            harga_baru = float(input("Masukkan harga per unit baru: "))
            update_barang(barang_list, kode, harga_baru, jumlah_baru)
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program inventory.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print()


inventory()



