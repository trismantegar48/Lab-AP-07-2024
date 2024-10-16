def palindrom(a):

    x = "".join(reversed(a.lower().split()))


    if x == x [::-1]:
        print("kata palindrom")
    else:
        print("bukan kata palindrom")

palindrom("jonas buaya")


