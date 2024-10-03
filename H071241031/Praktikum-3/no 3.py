baris = int(input("Masukan jumlah baris (N): "))
kolom = int(input("Masukan jumlah kolom (M): "))

for i in range(baris):
    if i % 2 == 0:
        for j in range(kolom):
            print(f"MOVE to ({i}, {j})")
    else:
        for j in range(kolom -1,-1,-1):
            print(f"MOVE to ({i}, {j})")