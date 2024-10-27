import os

os.system("cls")

list_barang = []

def tambah_barang():
    kode_barang = int(input("Masukkan Kode Barang : "))
    nama_barang = input("Masukkan Nama Barang : ")
    jumlah_barang = int(input("Masukkan Jumlah Barang : "))
    harga_barang = float(input("Masukkan Harga Per Unit : "))

    if jumlah_barang < 0 or harga_barang < 0:
        print("Jumlah dan Harga Tidak Boleh Negatif")
        return
    
    list_barang.append({
        "kode_barang" : kode_barang,
        "nama_barang" : nama_barang,
        "jumlah_barang" : jumlah_barang,
        "harga_barang" : harga_barang
    })

    print("Barang Berhasil Ditambahkan\n")

def hapus_barang():
    kode_barang = int(input("Masukkan Kode Barang yang akan di hapus : "))

    for barang in list_barang:
        if barang["kode_barang"] == kode_barang:
            list_barang.remove(barang)
            print("Barang berhasil dihapus\n")
            break
    else:
        print("Barang tidak ditemukan\n")

def tampilkan_barang():
    for data in list_barang:
        print(f"Kode Barang : {data['kode_barang']}, Nama Barang : {data['nama_barang']}, Jumlah Barang : {data['jumlah_barang']}, Harga Per Unit : {data['harga_barang']} \n")

def cari_barang():
    input_cari = int(input("Cari Berdasarkan (1) Kode Atau (2) Nama : "))

    if input_cari == 1:
        cari_kode = int(input("Masukkan Kode Barang : "))
        for kode in list_barang:
            if kode["kode_barang"] == cari_kode:
                print(f"Kode Barang : {kode['kode_barang']}, Nama Barang : {kode['nama_barang']}, Jumlah Barang : {kode['jumlah_barang']}, Harga Per Unit : {kode['harga_barang']} \n")
                break
        else:
            print("Barang tidak ditemukan\n")

    elif input_cari == 2:
        cari_nama = input("Masukkan Nama Barang : ")
        for nama in list_barang:
            if nama["nama_barang"] == cari_nama:
                print(f"Kode Barang : {nama['kode_barang']}, Nama Barang : {nama['nama_barang']}, Jumlah Barang : {nama['jumlah_barang']}, Harga Per Unit : {nama['harga_barang']} \n")
                break
        else:
            print("Barang tidak ditemukan\n")

def update_barang():
    update_kode = int(input("Masukkan Kode Barang Yang Ingin Diupdate : "))

    for kode in list_barang:
        if kode["kode_barang"] == update_kode:
            jumlah_baru = int(input("Masukkan Jumlah Baru : "))
            harga_baru = float(input("Masukkan Harga Per Unit Baru : "))

            kode["jumlah_barang"] = jumlah_baru
            kode["harga_barang"] = harga_baru

            print("Data Barang Berhasil Diperbaharui\n")
            return
    print("Barang tidak ditemukan\n")

while True:
    print(" Menu Inventori Barang ".center(27, "="))
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Barang")
    print("4. Cari Barang")
    print("5. Update Barang")
    print("6. Keluar")

    opsi = input("Pilih Opsi (1-6) : ")
    match opsi:
        case "1" : tambah_barang()
        case "2" : hapus_barang()
        case "3" : tampilkan_barang()
        case "4" : cari_barang()
        case "5" : update_barang()
        case "6" : break

    if opsi < "1" or opsi > "6":
        print("Pilih Opsi Yang Tersedia (1-6)")