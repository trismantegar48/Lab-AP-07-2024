input_string = input("Masukkan String : ")
shift = int(input("Masukkan jumlah pergeseran : "))

encrypted_string = ""

for char in input_string:
    if char.islower():
        new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encrypted_string += new_char
    elif char.isupper():
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        encrypted_string += new_char
    else:
        encrypted_string += char

print("teks  :", input_string)
print("Shift :", shift)
print("Cipher:", encrypted_string)