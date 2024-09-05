c = float(input("Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit\nMasukkan suhu dalam Celcius: "))

k = c + 273.15
r = c * 4/5
f = c * 9/5 + 32

kr = round(k)
rr= round(r)
fr = round(f)

print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah: {kr}K")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Reamur adalah: {rr}R")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Fahrenheit adalah: {fr}F")