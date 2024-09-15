sisi1 = int(input("Masukkan panjang sisi pertama:"))
sisi2 = int(input("Masukkan panjang sisi kedua:"))
sisi3 = int(input("Masukkan panjang sisi ketiga:"))

if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
    if sisi1 == sisi2 == sisi3:
        print("Segitiga Sama Sisi")
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")