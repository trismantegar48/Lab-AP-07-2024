def anagram(str1, str2):
    hitung1 = {}
    hitung2 = {}
    
    for char in str1:
        hitung1[char] = hitung1.get(char, 0) + 1
    
    for char in str2:
        hitung2[char] = hitung2.get(char, 0) + 1

    penghapusan = 0
    for char in set(list(hitung1.keys()) + list(hitung2.keys())):
        penghapusan += abs(hitung1.get(char, 0) - hitung2.get(char, 0))
    
    return penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

penghapusan = anagram(str1, str2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {penghapusan}")