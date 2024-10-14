def substrings(a):
    n = len(a)
    for length in range(1, n+1): 
        for start in range(n - length + 1): 
            print(a[start:start + length]) 
            
substrings(input("Input your string: "))