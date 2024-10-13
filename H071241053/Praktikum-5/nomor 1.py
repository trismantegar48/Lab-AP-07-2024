def Palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

Palindrome("Ibu Ratna Antar Ubi")  
Palindrome("Sistem Informasi 2024")  
 
