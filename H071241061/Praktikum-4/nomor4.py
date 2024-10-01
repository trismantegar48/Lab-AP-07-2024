print("Selamat datang di kalkulator sederhana!")

def kalkulator(angka_pertama, angka_kedua, operasi):
    try:
        if operasi == '+':
            return angka_pertama + angka_kedua
        elif operasi == '-':
            return angka_pertama - angka_kedua
        elif operasi == '*':
            return angka_pertama * angka_kedua
        elif operasi == '/':
            if angka_kedua == 0:
                return "Pembagian dengan nol tidak diperbolehkan."
            else:
                return angka_pertama / angka_kedua
        else:
            return "Operasi tidak valid. Gunakan +, -, *, atau /."
    except ValueError:
        return "Input tidak valid"

try:
    angka_pertama = int(input("Masukkan angka pertama: "))
    angka_kedua = int(input("Masukkan angka kedua: "))
    operasi = input("Masukkan operasi (+, -, *, /): ")

    hasil = kalkulator(angka_pertama, angka_kedua, operasi)
    print(f"Hasil: {hasil}")
except ValueError:
    print("Input yang dimasukkan harus berupa angka.")