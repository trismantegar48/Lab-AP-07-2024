import re
def adress(ip):
    ipv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    ipv6 = r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$'
    if re.match(ipv4,ip):
        return "Ipv4"
    elif re.match(ipv6,ip):
        return "Ipv6"
    else:
        return "Bukan Ip adress"

try:    
    N = int(input("Masukkan jumlah baris: "))
    if N <= 0:
        print("Masukkan angka yang lebih dari 0")    
    else:
        for _ in range(N):
           ip = input("Masukkan alamat ip adress: ")
           if ip == "" or ip == " ":
               print("This line has trailing whitespace")
           else:
               print(adress(ip))
except ValueError:
    print("input tidak valid")