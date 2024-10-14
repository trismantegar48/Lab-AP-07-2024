def Palindrome():
    input_str = input("Masukkan string: ")
    cleaned_str = input_str.replace(" ", "").lower() 

    if cleaned_str == cleaned_str[::-1]:
        print("Palindrome") 
    else:
        print("Not Palindrome")

Palindrome()
