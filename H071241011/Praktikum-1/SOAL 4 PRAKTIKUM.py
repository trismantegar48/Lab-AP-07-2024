print("Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")
celcius = float(input("Masukkan Suhu dalam Celcius : "))

kelvin = celcius + 273
reamur = 4/5 * celcius
fahrenheit = (9/5 * celcius) + 32

print(f"Hasil Konversi dari suhu {celcius:.0f} derajat Celcius ke Kelvin adalah : {kelvin:.0f}K")
print(f"Hasil Konversi dari suhu {celcius:.0f} derajat Celcius ke Reamur adalah : {reamur:.0f}R")
print(f"Hasil Konversi dari suhu {celcius:.0f} derajat Celcius ke Fahrenheit adalah : {fahrenheit:.0f}F")

