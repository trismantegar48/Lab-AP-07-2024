print("konversi suhu dari celcius ke kelvin, Reamur dan Fahrenheit")
c = float(input("masukkan suhu dalam Celcius: "))

K = c + 273
R = 4 / 5 * c
F = (9 / 5)*c + 32

print(f"Hasil konversi dari suhu {c} derajat celcius ke kelvin adalah:{K:.0f}K")
print(f"Hasil konversi dari suhu {c} derajat celcius ke Reamur adalah:{R:.0f}R")
print(f"Hasil konversi dari suhu {c} derajat celcius ke Fahrenheit adalah:{F:.0f}F")