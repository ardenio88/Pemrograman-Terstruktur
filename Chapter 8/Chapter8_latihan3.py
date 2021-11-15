berapa = int(input('Berapa banyak nama mahasiswa yang ingin di input :'))
listnama = []
jumlah = 0
jumlah2 = 0
while jumlah < berapa:
    inputuser = input('Nama Mahasiswa:')
    listnama.append(inputuser)
    jumlah += 1
listnama.sort()
for x in range(len(listnama)):
    print(listnama[x], '('+str(len(listnama[x])), 'karakter)')
    