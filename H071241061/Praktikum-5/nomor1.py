def palindrome(s):
    kata_balikan = ''.join(reversed(s))
    if s == kata_balikan :
        print("Palindrom")
    else:
        print("Bukan Palindrom")
        
string = input("Masukkan Kalimat: ")
palindrome(string)
