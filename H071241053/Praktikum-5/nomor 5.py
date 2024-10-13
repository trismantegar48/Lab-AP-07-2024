n = input("Masukkan String : ")
p = int(input("Masukkan jumlah pergeseran : "))

def caesar_cipher(s, shift):
    encrypted = []
    for char in s:
        if char.isalpha():  
            offset = 65 if char.isupper() else 97  
            encrypted.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            encrypted.append(char)  
    print(f'Text : {n}')
    print(f'Shift : {p}')
    print(f'Chipher : {''.join(encrypted)}')

caesar_cipher(n, p)

