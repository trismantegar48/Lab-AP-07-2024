import re

def validate_ip():
    ipv4_pattern = r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'

    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    
    z = int(input())
    for _ in range(z):
        ip = input().strip()
        
        if re.match(ipv4_pattern, ip):
            print("IPv4")
        elif re.match(ipv6_pattern, ip):
            print("IPv6")
        else:
            print("Bukan IP Address")

validate_ip()