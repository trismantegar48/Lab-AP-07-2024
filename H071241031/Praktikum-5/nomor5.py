def caesar_cipher(text, shift):
    return ''.join(
        chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower() else
        chr((ord(c) - ord('A') + shift) % 26 + ord('A')) if c.isupper() else c
        for c in text
    )

text = input("Masukkan string: ")
shift = int(input("Masukkan nilai shift: "))

print("Hasil enkripsi:", caesar_cipher(text, shift))
