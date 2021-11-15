hargabuah = {'apel': 5000,
             'jeruk': 8500,
             'mangga': 7800,
             'duku': 6500}
print('Nama buah yang ingin dibeli :', end='')
namabuah = input()
print('Berapa KG                   :', end='')
berapakg = int(input())
print('------------------------------')
totalhrg = berapakg * hargabuah[namabuah]
print('Total harga :', totalhrg)
