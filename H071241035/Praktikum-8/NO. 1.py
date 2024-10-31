import re

User = input("Masukkan Karakter = ")

pola = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
Cocokkan = re.match(pola, User) is not None

print('True' if len(User) == 45 and Cocokkan else 'False')