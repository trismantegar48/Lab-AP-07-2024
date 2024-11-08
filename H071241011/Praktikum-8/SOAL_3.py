import re

def is_valid_username(username):
    pattern = r'^[A-Za-z0-9]{5,20}$'
    return bool(re.match(pattern, username))

def is_valid_email(email):
    pattern = r'^[a-z]+\d{2,}@[a-z]+\.(com|co\.id)$'
    return bool(re.match(pattern, email))

def is_valid_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{8,}$'
    return bool(re.match(pattern, password))

def main():
    username = input("Masukkan username: ")
    if is_valid_username(username):
        email = input("Masukkan email: ")
        if is_valid_email(email):
            password = input("Masukkan password: ")
            if is_valid_password(password):
                print(f"\nRegistrasi berhasil! Halo {username}")
            else:
                print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
        else:
            print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
    else:
        print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")

if __name__ == "__main__":
    main()