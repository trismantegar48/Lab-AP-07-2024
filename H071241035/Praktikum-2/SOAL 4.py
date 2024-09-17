Penggunaan_data = float(input("Masukkan jumlah data yang digunakan (GB): "))
penggunaan_waktu = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)?: ").lower()
tipe_user = input("Apakah Anda pengguna Personal atau Bisnis?: ").lower()

if Penggunaan_data < 10 and penggunaan_waktu == "off-peak" and tipe_user == "personal":
    package = "Paket A"
elif 10 <= Penggunaan_data <= 50 and penggunaan_waktu == "peak" and tipe_user == "personal":
    package = "Paket B"
elif Penggunaan_data > 50 and penggunaan_waktu == "peak" and (tipe_user == "personal" or tipe_user == "bisnis"):
    package = "Paket C"
elif Penggunaan_data > 50 and penggunaan_waktu == "off-peak" and tipe_user == "bisnis":
    package = "Paket D"
else:
    package = "Tidak ada paket yang cocok"


print(f"Paket yang sesuai: {package}")