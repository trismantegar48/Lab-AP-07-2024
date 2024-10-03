def hitung_total_jarak():
    total_jarak = 0

    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if langkah == 0:
                break
            if langkah < 0:
                print("Input tidak valid. Masukkan bilangan bulat.")
                continue
            total_jarak += langkah
            
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
    
    print(f"Total jarak: {total_jarak} meter.")

    
    if langkah > 20:
        bahaya = "ya"
        keputusan = "tidak aman untuk menggali harta karun. coba lagi!"
    elif total_jarak == 50:
        bahaya = "tidak"
        keputusan = "aman untuk menggali harta karun."
    else:
        keputusan = "tidak menemukan harta karun"
    
    print(f"Ada bahaya: {bahaya}")
    print(f"Keputusan: {keputusan}")

hitung_total_jarak()