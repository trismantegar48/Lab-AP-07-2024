celcius = float(input("Masukkan suhu dalam celcius: "))

kelvin = celcius + 273.15
reamur = celcius * 4/5
fahrenheit = (celcius * 9/5) + 32

print(f"hasil konversi dari suhu {celcius:.0f} derajat celcius ke kelvin adalah: {kelvin:.0f}K")
print(f"hasil konversi dari suhu {celcius:.0f} derajat celcius ke reamur adalah: {reamur:.0f}R")
print(f"hasil konversi dari suhu {celcius:.0f} derajat celcius ke fahrenheit adalah: {fahrenheit:.0f}F")