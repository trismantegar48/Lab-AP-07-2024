def cek_langkah(jarak):
  """Memeriksa apakah langkah aman atau tidak."""
  return jarak <= 20

def ambil_langkah():
  while True:
    try:
      langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
      if langkah <= 0:
        return 0
      else:
        return langkah
    except ValueError:
      print("Input tidak valid. Masukkan bilangan bulat.")

def berburu_harta_karun():
  total_jarak = 0
  ada_bahaya = "Tidak"

  while True:
    langkah = ambil_langkah()
    if langkah == 0:
      break
    total_jarak += langkah
    if not cek_langkah(langkah):
      ada_bahaya = "Ya"
  print(f"total jarak:{total_jarak} meter")
  print("Ada bahaya:", ada_bahaya)
  if total_jarak == 50 and ada_bahaya == "Tidak":
    print("Aman! Kamu tepat menemukan harta karun dan menang!")
  elif total_jarak == 50 and ada_bahaya == "Ya":
    print("keputusan :Tidak aman untuk menggali harta karun. Coba lagi!")
  else:
    print("keputusan :Tidak menemukan harta karun. Coba lagi!")

berburu_harta_karun()