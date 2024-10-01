def hitung_langkah(n):
  if n <= 0 or not isinstance(n, int):
    return -1

  langkah = 0
  while n != 1:
    langkah += 1
    if n % 2 == 0:
      n //= 2
    else:
      n = n * 3 + 1
    print(float(n))
  return langkah

def main():
  try:
    n = int(input("Masukkan angka: "))
    hasil = hitung_langkah(n)
    if hasil != -1:
      print(f"Jumlah langkah: {hasil}")
    else:
      print("Input tidak valid")
  except ValueError:
    print("Input tidak valid")

main()
