berapa = int(input('Berapa banyak bilangan yang ingin di input :'))
bilbul = []
jumlah = 0
while jumlah < berapa:
    inputuser = int(input('bilangan bulat:'))
    bilbul.append(inputuser)
    jumlah += 1
bilbul.sort(reverse=True)
print(bilbul)