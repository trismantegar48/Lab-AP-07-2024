teks = input("Masukkan sebuah string: ")

for panjang in range(1, len(teks) + 1):
    for i in range(len(teks) - panjang + 1):
        print(teks[i:i + panjang])