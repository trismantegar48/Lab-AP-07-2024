nilai = int(input("Masukkan masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))

if kehadiran >= 75 :
    if nilai >= 85 :
        predikat = "Lulus dengan predikat A"
    elif nilai >= 70 :
        predikat = "Lulus dengan predikat B"  
    elif nilai >= 60 :
        predikat = "Lulus dengan predikat C"
    else:
        nilai_tugas = int(input("Masukkan nilai tugas tambahan: "))
        if nilai_tugas >= 70 :
            predikat = "Lulus dengan predikat C"
        else:
            predikat = "tidak lulus"        
else:
    predikat = "tidak lulus"  
     
print(predikat)         