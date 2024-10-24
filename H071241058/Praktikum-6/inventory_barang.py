inventori = {}

while True:
  print(
    "== Menu Inventori Barang ==\n"
    "1. Tambah Barang\n"
    "2. Hapus Barang\n"
    "3. Tampilkan Barang\n"
    "4. Cari Barang\n"
    "5. Update Barang\n"
    "6. Keluar"     
  )
  pilihan = input("Pilih Opsi (1-6): ")
  
  if pilihan == "1" :
    kode = input("Masukkan kode barang: ")
    if kode in inventori:
      print("Kode barang sudah ada. Gunakan update jika ingin memperbarui.")
    else:  
      nama = input("Masukkan nama barang: ")
      jumlah = input("Masukan jumlah barang: ")
      harga = input("Masukkan harga per unit: ")
      inventori[kode] = {"nama" : nama, "jumlah" : jumlah, "harga": harga}
      print("Barang berhasil ditambahkan")
    print()  
        
      
  elif pilihan == "2" :
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    if kode in inventori :
      del inventori[kode]
      print("Barang berhasil dihapus")
    else:
      print("Kode barang tidak ditemukan")  
    print()  
    
  elif pilihan == "3":
    if inventori:
      for kode, info in inventori.items():
        print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
    else:
      print("Inventori kosong.")
    print()
    
  elif pilihan == "4":
    cari = input("Cari berdasarkan (1) kode atau (2) Nama: ") 
    if  cari == "1":
      kode = input("Masukkan kode barang: ")
      if kode in inventori:
        info = inventori[kode]
        print(f"kode: {kode}, nama: {info['nama']}, jumlah: {info['jumlah']}, harga per unit: {info['harga']}")
      else:
        print("Barang tidak ada, mohon masukkan kode/nama dengan benar atau tambahkan barang jika tidak ada") 
    elif cari == "2":
      nama = input("Masukkan nama barang: ")
      ditemukan = False
      for kode, info in inventori.items():
        if info["nama"] == nama:
          print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
          ditemukan = True
      if not ditemukan :
        print("Barang tidak ditemukkan")  
    else:
      print("Opsi tidak valid")
    print()         
    
  elif pilihan == "5":
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    if kode in inventori:
      jumlah_baru = input("Masukkan jumlah baru: ")
      harga_baru = input("Masukkan harga per unit baru: ")
      
      if jumlah_baru :
        inventori[kode]["jumlah"] = jumlah_baru
      if harga_baru :  
        inventori[kode]["harga"] = harga_baru
        
      print("Barang berhasil diperbarui")  
    else:
      print("Kode barang tidak ditemukan")  
    print()  
  
  elif pilihan == "6":
    print("Terimakasih telah menggunakan program inventori")  
    break      

  else:
    print("Opsi tidak valid, silahkan masukkan input yang benar")
    print()
    