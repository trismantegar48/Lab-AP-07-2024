def langkah_aman(langkah):
    if langkah > 20:
        return False
    return True

def treasure_hunt():
    Total_langkah = 0
    deteksi_behaya = False

    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))

            if langkah == 0:
                break
            elif langkah < 0:
                print("Input tidak valid. Masukkan bilangan bulat.")
                continue

            if not langkah_aman(langkah):
                print("Ada bahaya: Ya")
                deteksi_behaya = True
            else:
                print("Ada bahaya: Tidak")

            Total_langkah += langkah
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    print(f"Total jarak: {Total_langkah} meter")

    if Total_langkah == 50 and not deteksi_behaya:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif deteksi_behaya:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

treasure_hunt()
