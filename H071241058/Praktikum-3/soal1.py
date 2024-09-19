x=int(input("Masukkan jumlah baris: "))
if x % 2 == 0:
    for i in range(x//2):
        print(" " * (x//2 - i - 1) + "*" * (2 * i + 1))
    for i in range(x//2 -1, -1, -1):
        print(" " * (x//2 - i - 1) + "*" * (2 * i + 1))  
else:  
    for i in range(x//2 + 1):
        print(" " * (x//2 - i) + "*" * (2 * i + 1))
    for i in range(x//2):
        print(" " * (i+1) + "*" * (x - 2 * (i + 1)))