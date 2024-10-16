def akronim(a):

    words = a.split()
    akronim = ''.join([word[0].upper() for word in words])
    return akronim

kalimat = "jonas baka"
print(akronim(kalimat)) 