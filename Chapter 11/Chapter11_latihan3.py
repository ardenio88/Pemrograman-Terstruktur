from datetime import *
try:
    # mengambil alamat teks data yang ingin diambil
    datainput = input("masukkan direktori/nama file\t:")
    myfile = open(datainput, 'r')
    teks = myfile.readlines()
    convteks = []
    data = {}
    # memisahkan \n
    for i in teks:
        convteks.append((i.strip()))
    # membuat dictionary
    for x in range(len(convteks)):
        splitteks = convteks[x].split("|")
        data[splitteks[0]] = convteks[x]
    # mengambil data dictionary
    kodemem = input("masukkan kode member\t:")
    member = data[kodemem].split("|")
    # mengambil data max retur dari dictionary ke format date
    a = member[4].split('-')
    tglmax = date(int(a[0]), int(a[1]), int(a[2]))
    # membuat data kapan member retur dan keterlambatannya
    memberkembali = datetime.date(datetime.now())
    terlambat = (memberkembali - tglmax).days
    if terlambat <= 0:
        haritelat = 0
        denda = 0
    else:
        haritelat = terlambat
        denda = 2000 * terlambat
    # output akhir
    print('\nData Peminjaman Buku\nKode member'.ljust(52), ':', member[0], '\nNama member'.ljust(31), ':', member[1])
    print('Judul buku'.ljust(30), ':', member[2])
    print('tanggal mulai peminjaman'.ljust(30), ':', member[3], '\ntanggal maks peminjaman'.ljust(31), ':', member[4])
    print('tanggal pengembalian'.ljust(30), ':', str(memberkembali))
    print('Terlambat'.ljust(30), ':', haritelat, 'Hari')
    print('Denda'.ljust(30), ': Rp', denda)
except FileNotFoundError:
    print('Maaf File Tidak Ditemukan')
except KeyError:
    print('Maaf Member Tidak Ditemukan')
