def palindrom(input_str):
    
    String = ''.join(filter(str.isalnum, input_str)).lower()

    if String == String[::-1]:
        print(f"Kata/kalimat '{input_str}' adalah Palindrom")
    else:
        print(f"Kata/kalimat '{input_str}' Bukan Palindrom")

palindrom(input("Masukkan Kata/Kalimat : ")) 
