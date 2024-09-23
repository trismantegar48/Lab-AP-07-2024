M = int(input("M : "))
N = int(input("N : "))

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(f"MOVE to ({i},{j})")
    else:
        for j in range(M-1, -1, -1):
            print(f"MOVE to ({i},{j})")
