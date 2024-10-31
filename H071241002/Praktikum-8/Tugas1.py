import re

def validate_string(S):
    if len(S) != 45:
        return False
    
    pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
    
    return bool(re.match(pattern, S))

S = input("Masukkan string: ")
print(validate_string(S))
