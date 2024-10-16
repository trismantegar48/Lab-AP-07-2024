def acronym(kalimat):
    words = kalimat.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return print(acronym)

acronym("Negara Kesatauan Republik Indonesia")
acronym("Azizi Shafa Asadel, Walaupun Kamu Sudah Tidak Di JKT Lagi, Kamu Tetap Menjadi Oshiku Satu Satunya")
