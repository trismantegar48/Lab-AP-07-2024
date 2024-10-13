def semua_substring(s): 
    substring = []
    panjang = len(s)

    for i in range(1, panjang + 1):
        for k in range(panjang - i + 1):
            substring.append(s[k:k + i])
        
    return substring

n = input("Input your string: ")
hasil = semua_substring(n)
print("=====================")

for substring in hasil:
    print(substring)
