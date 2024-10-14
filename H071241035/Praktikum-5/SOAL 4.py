def substrings(input_string):
    for panjang in range(1, len(input_string) + 1):
        
        for i in range(len(input_string) - panjang + 1):
            substring = input_string[i:i + panjang]
            print(substring)


input_string = input("Input your string: ")
print("====================")

substrings(input_string)

