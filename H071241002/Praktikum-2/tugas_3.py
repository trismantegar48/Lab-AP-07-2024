nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

if kehadiran >= 75:
    if nilai_akhir >= 85:
        predikat = "Lulus dengan Predikat A"
    elif  nilai_akhir >= 70:
        predikat = "Lulus dengan Predikat B"
    elif nilai_akhir >= 60:
        predikat = "Lulus dengan Predikat C"
    else:
        tugas = float(input("Masukkan nilai tugas tambahan: "))
        if tugas >= 70: 
            predikat = "Lulus dengan Predikat C"
        else:
            predikat = "Tidak Lulus"
    
else: 
    predikat = "Tidak Lulus"

print(predikat)

