def zeedventure():
    data_jarak = []
    status = "Tidak"
    while True:
        try:
            input_langkah = int(input("Masukkan Langkah (Meter) Atau 0 Untuk Selesai :"))
        except ValueError:
            print("Input Tidak Valid")
        if input_langkah == 0:
            break
        if input_langkah < 0:
            print("Input Tidak Valid")

        if input_langkah > 20:
            status = "Ya"

        data_jarak.append(input_langkah)

    if not data_jarak:
        print("Anda tidak melakukan perjalanan")
    else:
        total_jarak = sum(data_jarak)
        print(f"Total jarak: {total_jarak} meter")

        print(f"Ada Bahaya : {status}")

        if total_jarak >= 50 and status == "Tidak":
            keputusan = "Aman! Kamu tepat menemukan harta karun dan menang!!"
        elif total_jarak < 50 and status == "Ya":
            keputusan = "Tidak aman untuk menggali harta karun. Coba lagi!"
        else:
            keputusan = "Tidak menemukan harta karun. Coba lagi!"
            
        print(f"Keputusan : {keputusan}")

print(''' 
██████████████████████████████████████████████████████████████████████
█░▄▄░▄█▄─▄▄─█▄─▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█▄─▀█▄─▄█─▄─▄─█▄─██─▄█▄─▄▄▀█▄─▄▄─█
██▀▄█▀██─▄█▀██─▄█▀██─██─██▄▀▄███─▄█▀██─█▄▀─████─████─██─███─▄─▄██─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
      ''')
print("")
zeedventure()
