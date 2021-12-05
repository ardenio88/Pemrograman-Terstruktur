# variable teks dibawah optional/ dapat menggunakan input
teks = "i think i love you"
hasil = []


def password(n):
    # nama file baru optional / dapat menggunakan input
    myfile = open('e:/sandi1.txt', 'w+')
    if " " in teks:
        char = teks.split(" ")
        for x in range(len(char)):
            lis = list(char[x])
            gantichr = []
            for y in range(len(lis)):
                tambah = chr(ord(lis[y])+n)
                gantichr.append(tambah)
            hasil.append(''.join(gantichr))
        myfile.write(" ".join(hasil))
    else:
        lis = list(teks)
        gantichr = []
        for y in range(len(lis)):
            tambah = chr(ord(lis[y]) + n)
            gantichr.append(tambah)
        hasil.append(''.join(gantichr))
        myfile.write(hasil[0])
    myfile.close()
    lihathasil = input('ingin melihat hasil?(y/n)\t:')
    if lihathasil == 'y':
        print(' '.join(hasil))


password(3)
