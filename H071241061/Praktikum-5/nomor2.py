def acronym(s):
    words = s.split()
   
    acronyms = ''
    
    for word in words:
        acronyms += word[0].upper() 
    
    return acronyms 

a = input('Masukkan Kalimat: ')
print(acronym(a)) 
