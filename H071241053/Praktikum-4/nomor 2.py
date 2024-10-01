def periksa_bahaya(langkah_list):
    for langkah in langkah_list:
        if langkah > 20:
            return True
    return False

def harta_karun():
    langkah_list = []
    bahaya_terdeteksi = False
    
    while True:
        try:
            langkah = int(input("Masukkan jarak langkah (meter): "))
            
            if langkah == 0:
                bahaya_terdeteksi = periksa_bahaya(langkah_list)
                break

            langkah_list.append(langkah)

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            continue

    total_jarak = sum(langkah_list)
    print(f"Total jarak: {total_jarak} meter")

    if bahaya_terdeteksi:
        print("Ada bahaya = Ya")
    else:
        print("Ada bahaya = Tidak")

    if total_jarak == 50 and not bahaya_terdeteksi:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    elif bahaya_terdeteksi:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

harta_karun()
