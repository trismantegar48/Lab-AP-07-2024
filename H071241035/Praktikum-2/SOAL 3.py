# Input
nilai_akhir = int(input("Masukkan nilai akhir: "))
persentase_kehadiran = int(input("Masukkan persentase kehadiran: "))

if persentase_kehadiran >= 75:
    if nilai_akhir >= 85:
        predikat = "Lulus dengan Predikat A"
    elif nilai_akhir >= 70:
        predikat = "Lulus dengan Predikat B"
    elif nilai_akhir >= 60:
        predikat = "Lulus dengan Predikat C"
    else:
        nilai_tugas = int(input ("Masukkan Nilai Tambahan : "))
        if nilai_tugas >= 70 :
            predikat = "Lulus dengan Predikat C"
        else:
            predikat = "Tidak Lulus"
else : 
    predikat = "Tidak Lulus"

print(predikat)
