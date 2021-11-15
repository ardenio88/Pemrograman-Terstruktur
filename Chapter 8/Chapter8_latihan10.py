hargabuah = {'apel': 5000,
             'jeruk': 8500,
             'mangga': 7800,
             'duku': 6500}

totalharga = 0


def programtambah():
    print('Nama buah yang ingin dibeli :', end='')
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
    print('Nama buah yang ingin dibeli :', end='')
    namabuah = input()
    print('Berapa KG                   :', end='')
    berapakg = int(input())
    hargatambahan = berapakg * hargabuah[namabuah]
    totalharga += hargatambahan
    lanjutan = input("Beli buah lainnya (y/n)?")
    if lanjutan == "y":
        programtambah()
    if lanjutan =="n":
        print('------------------------------')
        print('Total harga :', totalharga)
        break