def minimum_deletions(string1, string2):
    original_string1 = string1
    original_string2 = string2

    for char in original_string2:
        if char in string1:
            string1 = string1.replace(char, '', 1)

    for char in original_string1:
        if char in string2:
            string2 = string2.replace(char, '', 1)

    deletions = len(string1) + len(string2)

    return deletions


string1 = input('Masukkan string pertama: ')
string2 = input('Masukkan string kedua: ')


result = minimum_deletions(string1, string2)
print(f'Jumlah minimum penghapusan untuk membuat anagram: {result}')