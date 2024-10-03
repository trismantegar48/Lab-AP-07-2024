def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:
           n = n / 2
        else:
            n = 3 * n + 1
        langkah += 1

        print (n)
    return langkah

try:
    n = int(input("Masukkan bilangan bulat positif: "))
    if n > 0:
        print(f"Jumlah langkah: {hitung_langkah(n)}")
    else:
        print("Input tidak Valid")
except ValueError:
    print("Input tidak Valid")
