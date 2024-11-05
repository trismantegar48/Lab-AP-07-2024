import re

def validate_ip(ip):
    ipv4_pattern = r'^((\d{1,3}\.){3}\d{1,3})$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        for part in parts:
            if not (0 <= int(part) <= 255):
                return "Bukan IP Address"
        return "IPv4"

    if re.match(ipv6_pattern, ip):
        return "IPv6"

    return "Bukan IP Address"

def main():
    N = int(input("Berapa kali Anda ingin menginput? : "))
    var = [input(f"Masukkan input ke {i + 1} : ") for i in range(N)]

    results = [validate_ip(ip) for ip in var]

    for result in results:
        print(result)

main()
