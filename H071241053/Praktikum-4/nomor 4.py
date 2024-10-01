def kalkulator_sederhana():
    print("Selamat datang di Kalkulator Sederhana!")
    
    try:
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua = float(input("Angka kedua: "))
        operasi = input("Operasi (+, -, *, /): ")
        
        if operasi == '+':
            hasil = angka_pertama + angka_kedua
        elif operasi == '-':
            hasil = angka_pertama - angka_kedua
        elif operasi == '*':
            hasil = angka_pertama * angka_kedua
        elif operasi == '/':
            if angka_kedua == 0:
                print("Pembagian dengan nol tidak diperbolehkan.")
                return
            hasil = angka_pertama / angka_kedua
        else:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")
            return
        
        print(f"Hasil: {float(hasil)}")
    
    except ValueError:
        print("Input tidak valid: could not convert string to float:'a'")

kalkulator_sederhana()

