kemarin = float(input("Masukkan harga saham kemarin: "))

harini = 105.0

p = (harini - kemarin)/kemarin * 100
p = round(p, 2)

r = {
    p < -3: "Jual",
    -3 <= p <= 5: "Tahan",
    p > 5: "Beli"
}

print("Perubahan presentase harga saham:",p,"%")
print("Rekomendasi investasi:",r[True])