import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def teka_teki(input_angka):
    if not isinstance(input_angka, int) or input_angka <= 0:
        raise ValueError("Input harus berupa bilangan bulat positif.")
    
    jumlah_langkah = 0
    nilai_angka = input_angka
    
    while nilai_angka != 1:
        if nilai_angka % 2 == 0:
            nilai_angka //= 2
        else:
            nilai_angka = (nilai_angka * 3) + 1
        
        jumlah_langkah += 1
        print(f"{nilai_angka}", end="\n")
        
        if jumlah_langkah > 1000:
            print("\nPeringatan: Proses dihentikan karena terlalu banyak langkah.")
            break
    
    print(f"\nJumlah langkah: {jumlah_langkah}")

def judul_gacor():
    print('''
    ██████  
        ██ 
       ▄███  
       ▀▀    
       ██    

            ''')
    print("")

def main():
    judul_gacor()
    while True:
        try:
            input_angka = int(input('Masukkan angka: '))
            teka_teki(input_angka)
            break
        except ValueError as zee:
            print(f"Error: {zee}")
        except Exception as zee:
            print(f"Terjadi kesalahan yang tidak terduga: {zee}")

if __name__ == "__main__":
    main()