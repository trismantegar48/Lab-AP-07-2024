def hitung_langkah(n):
    langkah = 0
    hasil = []

    while n > 1:
        hasil.append(n)  
        if n % 2 == 0:  
            n = n / 2
        else:           
            n = 3 * n + 1
        langkah += 1

    hasil.append(1.0) 
    return hasil, langkah

def main():
    try:
        angka = int(input("Masukkan angka: "))
        if angka <= 0: 
            print("Input tidak Valid")
            return
        
        hasil, jumlah_langkah = hitung_langkah(angka)

        for nilai in hasil:
            print(nilai)

        print("Jumlah langkah:", jumlah_langkah)

    except ValueError:
        print("Input tidak Valid")


main()
