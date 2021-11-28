def ubahhuruf(teks, a, b):
    listteks = list(teks)
    jumlahloop = listteks.count(a)
    i = 0
    while i < jumlahloop:
        lokasi = listteks.index(a)
        listteks[lokasi] = b
        i += 1
    print(''.join(listteks))


ubahhuruf('MATEMATIKA', 'T', 'S')
