import re

def validate_ip(ip):
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv6_pattern = r"^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$"
    
    if re.match(ipv4_pattern, ip) and all(0 <= int(part) <= 255 for part in ip.split('.')):
        return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

N = int(input("Masukkan jumlah baris inputan teks: "))
inputs = [input(f"Masukkan teks ke-{i+1}: ").strip() for i in range(N)]

for ip in inputs:
    print(validate_ip(ip))
