print("Konversi Detik Ke jam")
detik = int(input("masukan detik :" ))

jam = (detik // 3600)
menit = (detik - (jam * 3600))//60
detik = (detik -(jam * 3600)- (menit * 60))

print("%02d : %02d : %02d " % (jam, menit, detik))