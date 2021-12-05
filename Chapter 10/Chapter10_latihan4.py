file = input('masukkan direktori\t:')
myfile = open(file, 'r')
teks = myfile.readlines()
convteks = []
datamhs = {}
for x in teks:
    convteks.append((x.strip()))

for y in convteks:
    splitteks = y.split("|")
    dictambah = {'nim': splitteks[0], 'nama': splitteks[1], 'alamat': splitteks[2]}
    datamhs[splitteks[0]] = dictambah

try:
    print('masukkan NIM mahasiswa/i yang dicari: ', end='')
    nimmhs = input()
    datadicari = datamhs[nimmhs]
    print('Data Mahasiswa')
    print('NIM\t\t:', datadicari['nim'])
    print('nama\t:', datadicari['nama'])
    print('alamat\t:', datadicari['alamat'])
except KeyError:
    print('Maaf, NIM yang dicari tidak ditemukan / salah input')
