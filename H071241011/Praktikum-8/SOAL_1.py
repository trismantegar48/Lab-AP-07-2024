import re

def validate_string(s):
    first_40 = r'^[a-zA-Z02468]{40}'
    
    last_5 = r'[13579\s]{5}$'
    
    if len(s) != 45:
        return False
    
    return bool(re.match(first_40 + last_5, s))

s = input()
print(validate_string(s))