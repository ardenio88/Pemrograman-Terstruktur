try:
    print('PROGRAM PENGHITUNG BANYAK BILANGAN GANJIL & GENAP')
    file = input('masukkan direktori nama file\t:')
    myfile = open(file, 'r')
    ganjil = 0
    genap = 0
    teks = myfile.readlines()
    convteks = []
    numbers = []
    for i in teks:
        numbers.append((i.strip()).split('|'))
    myfile.close()
    for x in range(len(numbers)):
        for y in numbers[x]:
            convteks.append(y)
    print(convteks)
    for z in convteks:
        if int(z) % 2 == 0:
            genap += 1
        else:
            ganjil += 1
    print('Jumlah angka genap\t:', genap)
    print('Jumlah angka ganjil\t:', ganjil)
except FileNotFoundError:
    print('Maaf File tidak ditemukan')
except ValueError:
    print('Maaf Data yang diinginkan belum sesuai')
