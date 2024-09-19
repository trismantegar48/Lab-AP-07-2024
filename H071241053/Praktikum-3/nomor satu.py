t = int(input("Masukkan Jumlah Baris: "))

for i in range(t):
    if i < t // 2: 
        print(' ' * (t-i) + '*' * (2 * i + 1))
    else:  
        print(' ' * (i+1) + '*' * (2 * (t - i) - 1))



