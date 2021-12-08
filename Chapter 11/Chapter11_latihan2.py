from datetime import *
dataall = []
myfile = open('dataperpus.txt', 'w+')
lagi = 'y'


def inputmember():
    kodemem = input('masukkan kode member\t:')
    namamem = input('masukkan nama member\t:')
    bukumem = input('masukkan nama buku\t\t:')
    tanggal = datetime.date(datetime.now())
    retur = tanggal + timedelta(days=7)
    dataplus = [kodemem, namamem, bukumem, str(tanggal), str(retur)]
    dataall.append(dataplus)
    global lagi
    lagi = input("input lagi(y/n)\t\t:")
    print()


while lagi == 'y':
    inputmember()
else:
    for x in range(len(dataall)):
        myfile.write('|'.join(dataall[x])+"\n")
    myfile.close()
