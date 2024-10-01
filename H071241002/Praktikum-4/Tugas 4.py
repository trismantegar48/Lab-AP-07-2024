def calculator():
    print("Selamat datang di Kalkulator Sederhana!")
    
    while True:
        try:
            num1 = float(input("Angka pertama: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    while True:
        try:
            num2 = float(input("Angka kedua: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    while True:
        operation = input("Operasi (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        result = num1 / num2

    print(f"Hasil: {int(result) if result.is_integer() else result}")

calculator()
