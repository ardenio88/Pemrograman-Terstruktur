hargabuah = {'apel': 5000,
             'jeruk': 8500,
             'mangga': 7800,
             'duku': 6500}

totalharga = 0
lanjut = "o"


def programtambah():
    print('\nNama buah yang ingin dibeli :', end='')
    namabuah = input()
    print('Berapa KG                   :', end='')
    berapakg = int(input())
    global hargatambahan
    hargatambahan = berapakg * hargabuah[namabuah]
    global totalharga
    totalharga += hargatambahan
    global lanjutan
    lanjutan = input("Beli buah lainnya (y/n)?")


while True:
    print("Menu:\nA. Tambah Data\nB. Beli Buah\nC. Hapus Data Buah")
    pilihan = input("Pilihan Menu = ")
    if pilihan == "A":
        print('Masukkan Nama Buah : ', end='')
        namanew = input()
        if namanew in hargabuah.keys():
            print("Maaf Buah sudah ada")
        else:
            print('Masukkan Harga Satuan : ', end='')
            harganew = int(input())
            hargabuah[namanew] = harganew
            for x, y in hargabuah.items():
                print('-' + x + '(Harga Rp ' + str(y) + ')')
    if pilihan == "B":
        for x, y in hargabuah.items():
            print('-' + x + '(Harga Rp ' + str(y) + ')')
        print('\nNama buah yang ingin dibeli :', end='')
        namabuah = input()
        print('Berapa KG                   :', end='')
        berapakg = int(input())
        hargatambahan = berapakg * hargabuah[namabuah]
        totalharga += hargatambahan
        lanjutan = input("Beli buah lainnya (y/n)?")
        if lanjutan == "y":
            programtambah()
        if lanjutan == "n":
            print('------------------------------')
            print('Total harga :', totalharga)
            break
    if pilihan == "C":
        print('Masukkan Nama Buah = ', end='')
        namahps = input()
        if namahps not in hargabuah.keys():
            print("Maaf Buah Tidak ada di Daftar Menu")
        else:
            del hargabuah[namahps]
