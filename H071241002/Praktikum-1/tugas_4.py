print("konversi suhu dari celsius ke kelvin, reamur dan fahrenheit")
celcius = float(input("Masukkan suhu dalam Celcius: "))

kelvin = celcius + 273.15
reamur = celcius * 4 / 5
fahrenheit = celcius * 9 / 5 + 32

print(f"hasil konversi dari Suhu {celcius:.0f} derajat celsius ke kelvin adalah : {kelvin:.0f} K")
print(f"hasil konversi dari Suhu {celcius:.0f} derajat celsius ke reamur adalah : {reamur:.0f} R")
print(f"hasil konversi dari Suhu {celcius:.0f} derajat celsius ke Fahrenheit adalah : {fahrenheit:.0f} F")