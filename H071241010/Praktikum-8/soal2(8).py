import re

def check_ip_addresses():
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv6_pattern = r"^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$"
    while True:
        try:
            N = int(input("Masukkan jumlah baris input: "))
            if N <= 0:
                raise ValueError("Jumlah baris input harus lebih besar dari 0.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")
    
    for i in range(N):
        ip = input().strip()  
        if re.match(ipv4_pattern, ip)and all(0 <= int(part) <= 255 for part in ip.split('.')):
            print("IPv4")
        elif re.match(ipv6_pattern, ip):
            print("IPv6")
        else:
            print("Bukan IP Address")


check_ip_addresses()