def main():
    total_jarak = 0
    bahaya_terdeteksi  = False

    while True:
        user_input = input("Masukkan langkah (meter) atau 0 untuk selesai: ")
        
        if user_input == "0":
            break
        try:
            langkah_jarak = int(user_input)
            if langkah_jarak < 0:
                print("Input tidak valid. Masukkan bilangan bulat.")
                continue
            
            total_jarak += langkah_jarak
            
            if langkah_jarak > 20:
                bahaya_terdeteksi = True
            
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            continue

    # Output hasil
    print(f"Total jarak: {total_jarak} meter")
    
    if bahaya_terdeteksi:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Ada bahaya: Tidak")
        if total_jarak == 50:
            print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
        else:
            print("Tidak menemukan harta karun. Coba lagi!")

main()