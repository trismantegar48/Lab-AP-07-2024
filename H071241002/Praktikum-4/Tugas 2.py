def input_jarak():
    while True:
        try:
            jarak = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            return jarak
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

def berburu_harta():
    total_jarak = 0
    bahaya_terdeteksi = False
    
    while True:
        jarak = input_jarak()
        
        if jarak < 0:
            print("Langkah tidak dapat negatif. Permainan dihentikan.")
            break
        elif jarak == 0:
            break
        
        total_jarak += jarak
        
        if jarak > 20:
            bahaya_terdeteksi = True
    
    print(f"Total jarak: {total_jarak} meter")
    if bahaya_terdeteksi:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        if total_jarak == 50:
            print("Aman! Kamu tepat menemukan harta karun dan menang!")
        else:
            print("Tidak menemukan harta karun. Coba lagi!")

berburu_harta()