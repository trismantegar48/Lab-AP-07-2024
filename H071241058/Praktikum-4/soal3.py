def tekateki_mtk():
    angka = input("Masukkan angka: ")
    if not angka.isdigit() or int(angka) <= 0:
        print("Input tidak valid")
        return
    angka = int(angka)
    langkah = 0
    while angka != 1 or langkah == 0:
        if angka % 2 == 0:
            angka = angka // 2
        else:
            angka = angka * 3 + 1
        langkah += 1    
        print(angka)  
    print(f"jumlah langkah: {langkah}")    

tekateki_mtk()                