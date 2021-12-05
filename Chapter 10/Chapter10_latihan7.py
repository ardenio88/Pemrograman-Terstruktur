try:
    namafile = input("Masukkan directory\t:")
    kurang = int(input("Sandi - langkah?\t:"))
    hasil = []
    myfile = open(namafile, 'r')
    teks = myfile.readline()


    def undocaesar(n):
        # nama file baru optional / dapat menggunakan input
        myfile1 = open('e:/sandi_encrypted.txt', 'w+')
        if " " in teks:
            char = teks.split(" ")
            for x in range(len(char)):
                lis = list(char[x])
                gantichr = []
                for y in range(len(lis)):
                    tambah = chr(ord(lis[y]) - n)
                    gantichr.append(tambah)
                hasil.append(''.join(gantichr))
            myfile1.write(' '.join(hasil))
        else:
            lis = list(teks)
            xox = []
            for y in range(len(lis)):
                tambah = chr(ord(lis[y]) - n)
                xox.append(tambah)
            hasil.append(''.join(xox))
            myfile1.write(hasil[0])
        myfile.close()
        myfile1.close()
        lihathasil = input('ingin melihat hasil?(y/n):')
        if lihathasil == 'y':
            print(' '.join(hasil))


    undocaesar(kurang)
except FileNotFoundError:
    print('maaf file tidak ditemukan')
