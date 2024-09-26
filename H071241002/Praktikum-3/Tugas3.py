N = int(input("N: "))
M = int(input("M: "))

for row in range(N):
    if row % 2 == 0:  
        for col in range(M):
            print(f"MOVE to ({row},{col})")
    else:  
        for col in range(M-1, -1, -1):
            print(f"MOVE to ({row},{col})")