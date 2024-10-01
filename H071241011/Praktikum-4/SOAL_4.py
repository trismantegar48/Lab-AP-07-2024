import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kalkulator():
    print("")
    print('''█▓▒▒░░░SELAMAT DATANG DI KALKULATOR SEDERHANA░░░▒▒▓█''')
    print("")

    try:
        angka_pertama = float(input("  Masukkan Angka Pertama   : "))
    except ValueError as zee:
        print(f"Input Tidak Valid: {zee}")
        return
    
    try:
        angka_kedua = float(input("  Masukkan Angka Kedua    : "))
    except ValueError as zee:
        print(f"Input Tidak Valid: {zee}")
        return
    
    operasi = input("  Pilih Operasi (+, -, *, /)  : ")

    if operasi not in ['+', '-', '*', '/']:
        print("Operasi Tidak Valid. Gunakan (+, -, *, /)")
        return
        
    print("")
    try:
        if operasi == "+":
            hasil = angka_pertama + angka_kedua
        elif operasi == "-":
            hasil = angka_pertama - angka_kedua
        elif operasi == "*":
            hasil = angka_pertama * angka_kedua
        elif operasi == "/":
            if angka_kedua == 0:
                raise ZeroDivisionError ("Pembagian Dengan Nol Tidak Diperbolehkan")
            hasil = angka_pertama / angka_kedua
        else:
            return "Operasi tidak valid"
        
        if hasil.is_integer():
            print(f"  Hasil Operasi {operasi} Adalah  : {int(hasil)}")
        else:
            print(f"  Hasil Operasi {operasi} Adalah  : {int(hasil)}")
    except ZeroDivisionError as zee:
        print(zee)
def main():
    clear_screen()
    kalkulator()

if __name__ == "__main__":
    main()