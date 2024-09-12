a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")
    