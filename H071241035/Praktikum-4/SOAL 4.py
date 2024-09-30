def Kalkulator_sederhana():
    print("Selamat datang di Kalkulator Sederhana!")
    
    #inpt angka pertama
    try:
        angka1 = float(input("Angka pertama: "))
    except ValueError:
        print("Input tidak valid: could not convert string to float.")
        return

    #input angka kedua
    try:
        angka2 = float(input("Angka kedua: "))
    except ValueError:
        print("Input tidak valid: could not convert string to float.")
        return

    operasi = input("Operasi (+, -, *, /): ")

    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        else:
            hasil = angka1 / angka2
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /.")
        return

    print(f"Hasil: {hasil:.2f}")
    
Kalkulator_sederhana()
