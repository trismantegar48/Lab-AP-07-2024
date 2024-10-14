def Kriptografi(teks, pergeseran):  
    teks_enkripsi = ""  
    
    for karakter in teks:  
        if karakter.isupper():  
            teks_enkripsi += chr((ord(karakter) + pergeseran - 65) % 26 + 65)  
        elif karakter.islower():  
            teks_enkripsi += chr((ord(karakter) + pergeseran - 97) % 26 + 97)  
        else:  
            teks_enkripsi += karakter  
            
    return teks_enkripsi  
 
input_teks = input("Masukkan string yang akan dienkripsi: ")  
pergeseran = int(input("Masukkan jumlah pergeseran (bilangan bulat positif): "))  

hasil = Kriptografi(input_teks, pergeseran)  

print("--------------------------------------------")
print("Text:", input_teks)
print("Shift:", pergeseran)
print("Cipher:", hasil)