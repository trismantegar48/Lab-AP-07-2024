nilai_akhir = int(input("Masukkan nilai akhir : "))
kehadiran = int(input("Masukkan persentase kehadiran : "))
if kehadiran < 75:
    print("Anda Tidak Lulus")
    exit()
match nilai_akhir:
    case nilai_akhir if 85<=nilai_akhir<=100:
        print("Lulus dengan Predikat A")
    case nilai_akhir if 70<=nilai_akhir<=84:
        print("Lulus dengan Predikat B")
    case nilai_akhir if 60<=nilai_akhir<=69:
        print("Lulus dengan Predikat C")
    case nilai_akhir if nilai_akhir < 60:
        nilai = int(input("Nilai tambahan :"))
        if nilai >= 70 :
            print("Lulus dengan Predikat C")
        else:
            print("Anda Tidak Lulus")