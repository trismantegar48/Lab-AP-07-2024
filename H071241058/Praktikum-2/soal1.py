x = int(input("Masukkan panjang sisi pertama: "))
y = int(input("Masukkan panjang sisi kedua: "))
z = int(input("Masukkan panjang sisi ketiga: "))

if  x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("Segitiga Sama Sisi")
    elif x == y or x == z or y == z:
        print("Segitiga Sama Kaki")   
    else:
        print("Segitiga sembarang")

else:        
    print("Tidak dapat membentuk segitiga yang valid")        