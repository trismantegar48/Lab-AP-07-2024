while True :
    try:
        N = int(input("Input nilai N : "))
        M = int(input("Input nilai M : "))
        break
    except :
        print("Input tidak valid, masukkan bilangan bulat")

for i in range(N):
    if i % 2 == 0:  
        for j in range(M):
            print(f"MOVE to ({i},{j})")
    else:  
        for j in range(M - 1, -1, -1):
            print(f"MOVE to ({i},{j})")
