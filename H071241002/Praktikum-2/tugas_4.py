penggunaan_data = float(input("Masukkan penggunaan data per bulan (dalam GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan data Anda di jam sibuk (Peak) atau di luar jam sibuk (Off-Peak)? ")
jenis_pengguna = input("Jenis pengguna (personal/bisnis) ")  

if penggunaan_data < 10:
    if waktu_penggunaan == 'off-peak' and jenis_pengguna == 'personal':
        paket = "Paket A"
    else:
        paket = "Tidak ada paket yang cocok"
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == 'peak' and jenis_pengguna == 'personal':
        paket = "Paket B"
    else:
        paket = "Tidak ada paket yang cocok"
else:  
    if waktu_penggunaan == 'peak':
        if jenis_pengguna in ['personal', 'bisnis']:
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    elif waktu_penggunaan == 'off-peak' and jenis_pengguna == 'bisnis':
        paket = "Paket D"
    else:
        paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket}")
