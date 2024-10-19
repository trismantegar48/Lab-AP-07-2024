def mencari_hartakarun():
    total_jarak = 0
    bahaya = False
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if langkah < 0:
                print("Input tidak valid. Mohon masukkan bilangan bulat")
                continue
            elif langkah == 0:
                break
            else:
                total_jarak += langkah
                
                if langkah > 20:
                    bahaya = True         
        except ValueError:
            print("Input tidak valid. Mohon masukkan bilangan bulat")   
            
    print(f"Total jarak: {total_jarak} meter")        
    
    if bahaya is True :
        print("Ada bahaya: Ya")
        print("Disarankan untuk tidak menggali")
    else:
        print("Ada bahaya: Tidak")
        
    if total_jarak > 50 or total_jarak < 50:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!") 
    else:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")    

mencari_hartakarun()