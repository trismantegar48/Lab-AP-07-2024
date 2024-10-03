belahketupat = int(input("Masukkan jumlah baris : "))


for i in range (belahketupat):
    if i%2 == 1:
        continue
    else:
        print(" " * (belahketupat - i) + "* " * (i + 1))

if belahketupat%2 == 1:
    for i in range(belahketupat):
        if i%2 == 0:
            continue
        else:
            print(" " * (i + 2) + "* " * (belahketupat - i - 1))

else:
    for i in range (belahketupat):
        if i%2 == 0:
            continue
        else:
            print(" " * (i + 1) + "* " * (belahketupat - i))