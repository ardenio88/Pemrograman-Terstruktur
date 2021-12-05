myfile = open('e:/datamhs.txt', 'w+')
dataall = []


def tambahdata():
    print('Masukkan NIM\t:', end='')
    nim = input()
    print('Masukkan Nama\t:', end='')
    nama = input()
    print('Masukkan Alamat\t:', end='')
    alamat = input()
    datatambah = [nim, nama, alamat]
    dataall.append(datatambah)


tambahdata()
while True:
    print('')
    lagi = input("Buat lagi?(y/n)\t:")
    print('')
    if lagi == "y":
        tambahdata()
    elif lagi == "n":
        print(dataall)
        for x in range(len(dataall)):
            myfile.write('|'.join(dataall[x]) + "\n")
        myfile.close()
        break
    else:
        print("maaf input tidak valid")
