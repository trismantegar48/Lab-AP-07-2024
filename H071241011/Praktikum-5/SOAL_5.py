def enkripsi(teks, geser):
    hasil = ""
    for huruf in teks:
        if huruf.isalpha():
            offset_ascii = ord('A') if huruf.isupper() else ord('a')
            char_geser = chr((ord(huruf) - offset_ascii + geser) % 26 + offset_ascii)
            hasil += char_geser
        else:
            hasil += huruf
    return hasil

def main():
    teks_input = input("Masukkan teks yang akan dienkripsi: ")
    geser = int(input("Masukkan jumlah pergeseran: "))
    print("Teks terenkripsi:", enkripsi(teks_input, geser))

if __name__ == "__main__":
    main()
