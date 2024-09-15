z = int(input("Masukkan Panjang Sisi Pertama : "))
f = int(input("Masukkan Panjang Sisi Kedua : "))
c = int(input("Masukkan Panjang Sisi Ketiga : "))

if z + f > c and z + c > f and c + f > z:
    if z == f == c:
        print("Segitiga Sama Sisi")
    elif z == f or z == c or f == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Segitiga Ini Tidak Valid")