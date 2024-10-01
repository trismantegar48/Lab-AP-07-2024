def kalkulator(angka1, angka2, operasi):

  try:
    angka1 = float(angka1)
    angka2 = float(angka2)

    if operasi == '+':
      hasil = angka1 + angka2
    elif operasi == '-':
      hasil = angka1 - angka2
    elif operasi == '*':
      hasil = angka1 * angka2
    elif operasi == '/':
      if angka2 == 0:
        return "Pembagian dengan nol tidak diperbolehkan."
      else:
        hasil = angka1 / angka2
    else:
      return "Operasi tidak valid. Gunakan +, -, *, atau /."

    return hasil
  except ValueError:
    return "Input tidak valid: could not convert string to float"

if __name__ == "__main__":
  print("Selamat datang di Kalkulator Sederhana!")
  while True:
    try:
      angka1 = input("Angka pertama: ")
      angka2 = input("Angka kedua: ")
      operasi = input("Operasi (+, -, *, /): ")

      hasil = kalkulator(angka1, angka2, operasi)
      print("Hasil:", hasil)
      break
    except ValueError:
      print("Input tidak valid: could not convert string to float")