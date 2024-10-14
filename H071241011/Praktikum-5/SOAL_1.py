def palindrome(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

    return kata

palindrome("ibu raTna antaR uBi")
palindrome("Azizi Shafa Asadel")
