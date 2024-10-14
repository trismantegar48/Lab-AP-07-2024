
def caesar_cipher():
    kalimat = input("Masukkan string: ")
    shift = int(input("Masukkan jumlah pergeseran: "))

    cipher = ""
    for karakter in kalimat:
        if karakter.isalpha():
            ascii_offset = 65 if karakter.isupper() else 97
            cipher += chr((ord(karakter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cipher += karakter
    print(f"Text : {kalimat}")
    print(f"Shift : {shift}") 
    print(f"Cipher: {cipher}")

caesar_cipher()

    
