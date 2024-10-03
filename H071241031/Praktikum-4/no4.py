
def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan!"

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Pilih operasi:")
print("1. penjumlahan ")
print("2. pengurangan ")
print("3. perkalian ")
print("4. pembagian ")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == '1':
    print(f"Hasil: {penjumlahan(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {pengurangan(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {perkalian(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {pembagian(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")
