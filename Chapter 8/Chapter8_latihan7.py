hargabuah = {'apel': 5000,
             'jeruk': 8500,
             'mangga': 7800,
             'duku': 6500}
sort_harga = sorted(hargabuah.items(), key=lambda x:x[1], reverse=True)
for x in sort_harga:
    print(x[0])