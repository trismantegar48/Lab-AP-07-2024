def process_number(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        print(float(n))  
        steps += 1
    return steps

def main():
    try:
        n = int(input("Masukkan angka: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Input tidak valid")
        return

    steps = process_number(n)
    print(f"Jumlah langkah: {steps}")

main()
