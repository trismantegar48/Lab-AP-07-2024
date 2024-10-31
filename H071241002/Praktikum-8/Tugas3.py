import re

def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.match(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z]+[0-9]*@[a-z]+\.(com|co\.id)$"
    return re.match(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8,}$"
    return re.match(pattern, password)


username = input("Masukkan username: ").strip()

if not username:
    print("\nUsername tidak boleh kosong. Registrasi gagal!")
elif is_valid_username(username):
    email = input("Masukkan email: ").strip()
    if not email:
        print("\nEmail tidak boleh kosong. Registrasi gagal!")
    elif is_valid_email(email):
        password = input("Masukkan password: ").strip()
        if not password:
            print("\nPassword tidak boleh kosong. Registrasi gagal!")
        elif is_valid_password(password):
            print(f"\nRegistrasi berhasil! Selamat datang, {username}!")
        else:
            print("\nPassword tidak valid. Pastikan password memiliki setidaknya 8 karakter, satu huruf kapital, satu huruf kecil, dan satu angka. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid. Username harus panjang antara 5 hingga 20 karakter dan hanya terdiri dari huruf dan angka.")
