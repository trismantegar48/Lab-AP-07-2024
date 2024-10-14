def cetak_substring():
    input_str = input("Input your string : ")

    n = len(input_str)
 
    for length in range(1, n+1):
        for i in range(n-length+1):
            print(input_str[i:i+length])

cetak_substring()


