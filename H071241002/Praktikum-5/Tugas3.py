from collections import Counter

def penghapusan_minimum_untuk_anagram(str1, str2):
    str1 = ''.join(filter(str.isalpha, str1)).lower()
    str2 = ''.join(filter(str.isalpha, str2)).lower()

    hitung1 = Counter(str1)
    hitung2 = Counter(str2)

    penghapusan = 0

    for char in hitung1:
        if char in hitung2:
            penghapusan += abs(hitung1[char] - hitung2[char])
        else:
            penghapusan += hitung1[char]
    
    for char in hitung2:
        if char not in hitung1:
            penghapusan += hitung2[char]

    return penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

hasil = penghapusan_minimum_untuk_anagram(str1, str2)
print(f"Jumlah minimum karakter yang perlu dihapus: {hasil}")