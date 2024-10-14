def caesar_cipher(teks, pergeseran):
    hasil = ""

    for char in teks:
        if char.isalpha():
            shift = pergeseran % 26  
            if char.islower(): 
                hasil += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper(): 
                hasil += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:

            hasil += char

    return hasil

# Mengambil input dari pengguna
input_string = input("Masukkan string: ")
shift_value = int(input("Masukkan jumlah pergeseran: "))

# Melakukan enkripsi
encrypted_string = caesar_cipher(input_string, shift_value)

# Menampilkan hasil
print(f"Text: {input_string}")
print(f"Shift: {shift_value}")
print(f"Cipher: {encrypted_string}")
