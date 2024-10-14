def acronym():
    input_str = input("acronym: ")

    if len (input_str.split()) < 2:
        print("Input tidal valid masukkan lebih dari satu kata")
        return
        
    acronym_str = ''.join([word[0].upper() for word in input_str.split()])

    print(f"{acronym_str}")

acronym()
