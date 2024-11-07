import re

def validate_string(s):
    pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
    return len(s) == 45 and bool(re.match(pattern, s))

s= "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"
print(validate_string(s))
