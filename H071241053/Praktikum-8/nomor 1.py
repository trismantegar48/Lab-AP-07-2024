import re

def validate_string(s):
    pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
    return len(s) == 45 and bool(re.match(pattern, s))


n = input("input karakter : ")
print(validate_string(n))  
