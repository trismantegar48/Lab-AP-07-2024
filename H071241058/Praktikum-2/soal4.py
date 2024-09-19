penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk(peak)? ")
jenis_pengguna = input("Apakah anda pengguna personal atau bisnis? ")
    
if penggunaan_data < 10: 
    kategori_pengguna = "ringan"
elif 10 <= penggunaan_data <= 50:
    kategori_pengguna = "sedang"
else :
    kategori_pengguna = "berat"
        
if kategori_pengguna == "ringan" and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    print("paket A")
elif kategori_pengguna == "sedang" and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    print("paket B")
elif kategori_pengguna == "berat" and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    print("paket c")
elif kategori_pengguna == "berat" and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
    print("paket D")
else:
    print("tidak ada paket yang cocok")