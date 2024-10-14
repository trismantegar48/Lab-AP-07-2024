string = input('Masukkan string: ')
shift = int(input('Masukkan jumlah pergeseran: '))
huruf = 'abcdefghijklmnopqrstuvwxyz'
result = ""

for char in string:
    if char in huruf:  
        a = huruf.find(char)
        new_char = huruf[(a + shift) % 26]
        result += new_char  
    else:
        result += char  

print(result)

