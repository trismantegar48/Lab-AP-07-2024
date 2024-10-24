gudang_barang = {}

def tambah_barang():
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    harga_per_unit = float(input("Masukkan harga per unit: "))
    jumlah = int(input("Masukkan jumlah barang: "))

    if kode_barang in gudang_barang:
        print(f"Barang dengan kode {kode_barang} sudah ada di dalam gudang. Jumlah akan diperbarui.")
        gudang_barang[kode_barang]["jumlah"] += jumlah
    else:
        gudang_barang[kode_barang] = {"nama": nama_barang, "harga": harga_per_unit, "jumlah": jumlah}
    
    print(f"{nama_barang} telah ditambahkan/diperbarui di dalam gudang.\n")

def hapus_barang():
    kode_barang = input("Masukkan kode barang yang ingin dihapus (contoh: 001, 005): ")
    if kode_barang in gudang_barang:
        del gudang_barang[kode_barang]
        print(f"Barang dengan kode {kode_barang} telah dihapus dari gudang.\n")
    else:
        print(f"Barang dengan kode {kode_barang} tidak ditemukan di dalam gudang.\n")

def tampilkan_gudang():
    if not gudang_barang:
        print("Gudang kosong.\n")
    else:
        print("Daftar barang di gudang saat ini:")
        for kode, data in gudang_barang.items():
            print(f"Kode: {kode.zfill(3)}, Nama: {data['nama']}, Harga: {data['harga']}, Jumlah: {data['jumlah']}")
        print()

def cari_barang():
    kode_barang = input("Masukkan kode barang: ")
    if kode_barang in gudang_barang:
        data = gudang_barang[kode_barang]
        print(f"Kode: {kode_barang.zfill(3)}, Nama: {data['nama']}, Harga: {data['harga']}, Jumlah: {data['jumlah']}\n")
    else:
        print(f"Barang dengan kode {kode_barang} tidak ditemukan di dalam gudang.\n")

def perbarui_barang():
    kode_barang = input("Masukkan kode barang yang ingin diperbarui (contoh: 001, 005): ")
    if kode_barang in gudang_barang:
        jumlah_baru = int(input("Masukkan jumlah baru: "))
        harga_baru = float(input("Masukkan harga baru: "))
        gudang_barang[kode_barang]["jumlah"] = jumlah_baru
        gudang_barang[kode_barang]["harga"] = harga_baru
        print(f"Data barang dengan kode {kode_barang.zfill(3)} telah diperbarui.\n")
    else:
        print(f"Barang dengan kode {kode_barang} tidak ditemukan di dalam gudang.\n")

def main():
    while True:
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Perbarui Barang")
        print("6. Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_gudang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            perbarui_barang()
        elif pilihan == '6':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.\n")

if __name__ == "__main__":
    main()
