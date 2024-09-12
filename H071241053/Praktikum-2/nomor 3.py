nilai = int(input("Masukkan nilai akhir: "))
persentase = int(input("Masukkan persentase kehadiran: "))

if persentase >= 75:
    if nilai >= 85:
        predikat = "Lulus dengan Predikat A"
    elif nilai >= 70:
        predikat = "Lulus dengan Predikat B"
    elif nilai >= 60:
       predikat = "Lulus dengan Predikat C"
    else:
        nilai_tugas = int(input("Masukkan nilai tugas tambahan: "))
        if nilai_tugas >= 70:
            predikat = "Lulus dengan Predikat C"
        else:
           predikat = "Tidak lulus"
else:
   predikat = "Tidak lulus"
    
print(predikat)


    