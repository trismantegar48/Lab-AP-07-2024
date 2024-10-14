def buat_akronim(s):
    akronim = ''.join([kata[0].upper() for kata in s.split()])
    print(akronim)

buat_akronim("Negara Kesatuan Republik Indonesia")  

