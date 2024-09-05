# Soal 4 : Buatlah program yang bisa secara otomatis mengonversi suhu dari skala
#Celcius ke beberapa skala lain seperti Kelvin, Reamur, dan Fahrenheit.

# Input dari pengguna
celsius = float(input("Masukkan Suhu dalam Celcius: "))

# Konversi ke Kelvin
kelvin = celsius + 273.15

# Konversi ke Reamur
reamur = celsius * 0.8

# Konversi ke Fahrenheit
fahrenheit = celsius * 1.8 + 32

# Output hasil konversi
print(f"Hasil konversi dari suhu {celsius:.0f} derajat Celcius ke Kelvin adalah: {kelvin:.0f}K")
print(f"Hasil konversi dari suhu {celsius:.0f} derajat Celcius ke Reamur adalah: {reamur:.0f}R")
print(f"Hasil konversi dari suhu {celsius:.0f} derajat Celcius ke Fahrenheit adalah: {fahrenheit:.0f}F")

