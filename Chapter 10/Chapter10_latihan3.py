try:
    file = input('Masukkan Direktori\t:')
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

    print(datamhs)
except FileNotFoundError:
    print('maaf file tidak ditemukan')
