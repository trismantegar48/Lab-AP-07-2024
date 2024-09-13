penggunaan_data = float(input("Masukkan penggunaan data dalam GB: "))
waktu_penggunaan = input("Masukkan waktu penggunaan (peak/Off-Peak): ").lower()
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ").lower()

if penggunaan_data < 10:
  penggunaan = "ringan"
elif penggunaan_data <= 50 and penggunaan_data >= 10:
  penggunaan = "sedang"
else:
  penggunaan = "berat"

if waktu_penggunaan == "Off-Peak":
  waktu = "Luar Jam Sibuk"
else:
  waktu = "Jam Sibuk"

match (penggunaan ,waktu,jenis_pengguna):
    case  ("ringan","luar Jam Sibuk","personal" ):
        saran = "Paket A"
    case ("sedang","Jam Sibuk","personal"):
        saran = "Paket B"
    case ("berat", "Jam Sibuk","personal"):
        saran = "Paket C"
    case ("berat","Jam Sibuk","bisnis"):
        saran = "Paket D"
    case _:
        saran = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai : {saran}")