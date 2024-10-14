

def cetak_substring():
    kalimat = input("Input your string: ")
    print("=========================")

    for panjang in range(1, len(kalimat) + 1):
        for i in range(len(kalimat) - panjang + 1):
            substring = kalimat[i:i + panjang]
            print(substring)
cetak_substring()