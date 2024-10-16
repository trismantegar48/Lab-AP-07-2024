def anagram():
    str1 = input("Masukkan String 1: ")
    str2 = input("Masukkan String 2: ")

    penghapusan = 0
    for char in set(str1 + str2):
        penghapusan += abs(str1.count(char) - str2.count(char))
    return print(f"Jumlah Minimum Penghapusan Untuk Membuat Anagram: {penghapusan}")

anagram()
