def hapus_anagram(str1, str2):
    hapus = 0
    str2_list = list(str2)

    for char in str1:
        if char in str2_list:
            str2_list.remove(char)
        else:
            hapus += 1
    hapus += len(str2_list)

    return hapus

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

result = hapus_anagram(str1, str2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {result}")