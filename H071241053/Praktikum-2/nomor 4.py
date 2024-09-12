data = int(input("Masukkan jumlah data yang digunakan: "))
waktu = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
pengguna = input("Apakah Anda pengguna personal atau bisnis? ")

match (data, waktu, pengguna):
    case (data, "off-peak", "personal") if data < 10:
        paket = "Paket A"
    case (data, "peak", "personal") if 10 <= data <= 50:
        paket = "Paket B"
    case (data, "peak", "personal") | (data, "peak", "bisnis") if data > 50:
        paket = "Paket C"
    case (data, "off-peak", "bisnis") if data > 50:
        paket = "Paket D"
    case _:
        paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket}")