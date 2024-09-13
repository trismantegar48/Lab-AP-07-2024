nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

if kehadiran >= 75:
  if nilai_akhir >= 85:
    predikat = "lulus dengan predikat A."
  elif nilai_akhir >= 70:
    predikat = "lulus dengan predikat B."
  elif nilai_akhir >= 60:
    predikat = "lulus dengan predikat C"
  else:
    tugas_tambahan = float(input("Masukkan nilai rata-rata tugas tambahan: "))
    if tugas_tambahan >= 70:
      predikat = "lulus dengan predikat C."
    else:
      predikat = "tidak lulus."
  
else:
    predikat = "tidak lulus."

print(predikat)