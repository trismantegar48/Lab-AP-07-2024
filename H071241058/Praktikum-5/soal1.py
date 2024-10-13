def palindrome(kata):
    kata = kata.lower().replace(" ", "")  
    if kata == kata[::-1] :
        print("Palindrome") 
    else:
        print("Not Palindrome")
          
palindrome("Ibu Ratna Antar Ubi")          
palindrome("Sistem informasi 2024")