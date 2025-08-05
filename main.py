"Program Manajemen Kontak"

kontak1 = {'nama' : "andi", 'HP' : '08123456', 'email': "andi@gmail.com"}
kontak2 = {'nama' : "dell", 'HP' : '08123789', 'email': "del@gmail.com"}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4):")

    if pilihan == '1':
        # melihat semua kontak
        # pass
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]},{item["HP"]},{item["email"]}')
        else:
            print("Kontak masih kosong!")
    elif pilihan == '2':
        # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru:")
        HP = input("masukkan nomor hp kontak yang baru:")
        email = input("Masukkan emial kontak yang baru:")
        kontak_baru = {'nama': nama, 'HP': HP, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")
    elif pilihan == '3':
        # menghapus kontak
        print("\n")
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]},{item["HP"]},{item["email"]}')
        else:
            print("Kontak masih kosong!")
            continue

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus")

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")