def acronym(kalimat):
    kata_kata = kalimat.split()
    singkatan = ''.join(kata.upper()[0] for kata in kata_kata)
    return singkatan
print(acronym("Negara Kesatuan Republik Indonesia"))