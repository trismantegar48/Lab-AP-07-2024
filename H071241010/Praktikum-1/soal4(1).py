celsius =float(input("Masukkan suhu dalam celcius:"))
kelvin = celsius + 273.15
reamur = celsius * 4 // 5
fahrenheit = (celsius * 9 // 5) + 32

print(f"Hasil konversi dari suhu {celsius:.0f} derajat celsius ke Kelvin adalah: {kelvin:.0f}K")
print(f"Hasil konversi dari suhu {celsius:.0f} derajat celsius ke Reamur adalah: {reamur:.0f}R")
print(f"Hasil konversi dari suhu {celsius:.0f} derajat celsius ke Farenheit adalah: {fahrenheit:.0f}F")