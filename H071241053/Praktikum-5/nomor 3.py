from collections import Counter
import re

def hitung_minimum_penghapusan(s1, s2):
    s1 = re.sub(r'[^a-zA-Z]', '', s1)
    s2 = re.sub(r'[^a-zA-Z]', '', s2)
    
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    penghapusan = sum((count1 - count2).values()) + sum((count2 - count1).values())
    
    print("Jumlah minimum penghapusan untuk membuat anagram:", penghapusan)

s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")

hitung_minimum_penghapusan(s1, s2)

# user friendly pada saat input parameter jadi penginputan tanggal cuma tanggalnya doang
# tambahkan dokumentasi yang lengkap
# ubah jadi bahasa inggris 