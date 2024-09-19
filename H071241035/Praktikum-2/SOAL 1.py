# input panjang sisi segitiga dari pengguna
a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))


if a + b > c and a + c > b and b + c > a:

    # jenis segitiga
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or b == c or a == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")












































# # input
# a = float(input("Masukkan panjang sisi pertama: "))
# b = float(input("Masukkan panjang sisi kedua: "))
# c = float(input("Masukkan panjang sisi ketiga: "))

# # cek apakah bisa membentuk segitiga yang valid dengan memeriksa kondisi satu-satu secara terpisah
# if a + b > c:
#     if a + c > b:
#         if b + c > a:
#             # Menentukan jenis segitiga
#             if a == b == c:
#                 print("Segitiga Sama Sisi")
#             elif a == b:
#                 print("Segitiga Sama Kaki")
#             elif b == c:
#                 print("Segitiga Sama Kaki")
#             elif a == c:
#                 print("Segitiga Sama Kaki")
#             else:
#                 print("Segitiga Sembarang")
#         else:
#             print("Tidak dapat membentuk segitiga yang valid")
#     else:
#         print("Tidak dapat membentuk segitiga yang valid")
# else:
#     print("Tidak dapat membentuk segitiga yang valid")
