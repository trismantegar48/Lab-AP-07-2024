def palindrome(kata):
    kata = kata.replace(" ", "").lower()
    if kata == kata[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

palindrome("kakak")