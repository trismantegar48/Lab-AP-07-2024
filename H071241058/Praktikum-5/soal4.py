def cetak_substring(s):
    print(f"Input your string: {s}")
    print("=" * 25)

    for i in range(len(s)):
        print(s[i])

    for i in range(1, len(s)):
        for j in range(len(s) - i):
            print(s[j:j+i+1])

s = input("Input your string: ")

cetak_substring(s)