print("Selamat datang di Kalkulator Sederhana!")
def kalkulator_sederhana():
    try:
        angka1 = float(input("Angka pertama: "))
        angka2 = float(input("Angka kedua: "))    
    except ValueError:
        print(f"Input tidak valid: {ValueError}")    
    operasi = input("Operasi (+. -, *, /): ") 
    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2 
    elif operasi == "*":
        hasil = angka1 * angka2  
    elif operasi == "/":
        if angka2 != 0 :
            hasil = angka1 / angka2
        else:
            print("Pembagian dengan nol tidak diperbolehkan")
            return    
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /")
        return
        
    print(hasil)                        
       
kalkulator_sederhana()