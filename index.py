data_buku = {
    "buku1":{
        "judul":"New Resident Yogyakarta",
        "penulis":"Raisyamq",
        "tahun_terbit":2025
    }
    }

while True:
    print("MENU")
    print("1. List Buku")
    print("2. Tambah Buku")
    print("3. Tambah Data")
    print("4. Ubah Data")
    print("5. Hapus data")
    print("6. Keluar")
    menu = input("Pilih menu (1-6): ")

    if menu == "1":
            print(data_buku)

    elif menu == "2":
        while True:
            input_judul = input("masukkan judul buku: ")
            if input_judul == "selesai":
                break
            else:
                jumlah_buku = 1
                jumlah_buku = jumlah_buku + 1
                buku_baru = "buku" + str(jumlah_buku)
                input_penulis = input("masukkan nama penulis: ")
                input_tahun_terbit = input("masukkan tahun terbit buku: ")
                data_buku[buku_baru] = {
                    "judul":input_judul,
                    "penulis":input_penulis,
                    "tahun_terbit":input_tahun_terbit
                }
                print(data_buku[buku_baru]) 
                
    elif menu == "3":
        print("Daftar Buku")
        print(data_buku)
        while True:
            buku = input("Masukkan buku yang ingin di ganti: ")
            if buku == "selesai":
                break
            if buku in data_buku:
                key = input("masukkan data baru: ")
                value = input("masukkan "+key+": ")
                data_buku[buku][key] = value
                print("Daftar Buku")
                print(data_buku)
            else:
                print("buku tidak ada")

    elif menu == "4":
        print("Daftar Buku")
        print(data_buku)
        while True:
            ubah = input("masukkan buku yang ingin di ubah: ")
            if ubah in data_buku:
                while True:
                    key = input("masukkan data yang ingin di ubah: ")
                    if key in data_buku[ubah]:
                        value = input("masukkan "+key+" yang baru: ")
                        data_buku[ubah][key] = value
                        print("Daftar Buku")
                        print(data_buku)
                        break
                    else:
                        print("data tidak ada")
                        continue
            elif ubah == "selesai":
                break
            else:
                print("buku tidak ada")

    elif menu == "5":
        while True:
            print("daftar buku: ")
            print(data_buku)
            print("Ketik 'selesai' kalau sudah tidak ingin menghapus data lagi.")
            hapus = input("Masukkan buku yang datanya ingin di hapus dari daftar buku: ")
            if hapus == "selesai":
                break
            elif hapus in data_buku:
                for key in data_buku:
                    key_hapus = input("masukkan data buku yang ingin di hapus: ")
                    del data_buku[hapus][key_hapus]
                    print("berhasil menghapus data dari data buku.")
                    break
            else:
                print(hapus, "tidak ditemukan di data buku.")  

    elif menu == "6":
        print("exit")
        break
    else:
        print("Pilihan tidak ada, input lagi.")
