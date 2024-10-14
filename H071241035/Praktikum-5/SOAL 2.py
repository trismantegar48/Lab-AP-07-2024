def akronim(kalimat):
    kata_kata = kalimat.split()
    hasil_akronim = ''.join([kata[0].upper() for kata in kata_kata])
    return hasil_akronim  
try:   
    kalimat_input = input("Masukkan Kalimat: ")  
    if not kalimat_input:  
        raise ValueError() 
except:  
    kalimat_input = "Negara Kesatuan Republik Indonesia"  

akronim_output = akronim(kalimat_input)

print(f"akronim dari kalimat '{kalimat_input}' adalah '{akronim_output}'.")
