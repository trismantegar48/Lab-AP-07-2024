
def acronym(kalimat):
    potongan_kata = kalimat.split(" ")
    akronim = ''.join(kata[0].upper() for kata in potongan_kata)
    print(akronim)

acronym("negara kesatuan republik indonesia")
