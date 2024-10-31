import re

def is_valid_username(username):
    # Pola untuk memvalidasi username (panjang minimal 5 dan maksimal 20 karakter)
    pattern = r"^[A-Za-z0-9]{5,20}$"  
    return re.match(pattern, username) 

def is_valid_email(email):
    # Pola untuk validasi email (contoh: user@example.com atau user@example.co.id)
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|co\.id)$'
    return re.match(pattern, email)

def is_valid_password(password):
    # Pola untuk validasi password (minimal 8 karakter, setidaknya 1 huruf besar, 1 huruf kecil, 1 angka, 1 simbol)
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password)

# --------
username = input("Masukkan username: ")
if is_valid_username(username):
    email = input("Masukkan email: ")
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! Halo {username}")
        else:
            print("\nPassword yang kamu input berisiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")
