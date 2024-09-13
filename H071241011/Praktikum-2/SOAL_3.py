nilai_akhir = float(input("Masukkan Nilai Akhir : "))
kehadiran = float(input("Masukkan Persentase Kehadiran : "))

if kehadiran >= 75:
    if nilai_akhir >= 85:
        predikat = "A"
    elif nilai_akhir >= 70:
        predikat = "B"
    elif nilai_akhir >= 60:
        predikat = "C"
    else:
        nilaitambah = int(input("Masukkan Nilai Tambahan : "))
        if nilaitambah >= 70:
            predikat = "C"
        else:
            predikat = "Tidak Lulus"
else:
    predikat = "Tidak Lulus"
print(f"Lulus Dengan Predikat {predikat}")