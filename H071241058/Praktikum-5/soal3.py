def penghapusan_anagram(s1, s2):
    total_penghapusan = 0
    for char in set(s1 + s2):
        total_penghapusan += abs(s1.count(char) - s2.count(char))
    return total_penghapusan

s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")
print("Jumlah minimum penghapusan untuk membuat anagram:", penghapusan_anagram(s1, s2))