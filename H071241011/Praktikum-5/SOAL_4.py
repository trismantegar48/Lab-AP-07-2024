def generate_substrings():
    string = input("Masukkan sebuah string : ")
    n = len(string)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            print(string[start:start+length])

generate_substrings()
            