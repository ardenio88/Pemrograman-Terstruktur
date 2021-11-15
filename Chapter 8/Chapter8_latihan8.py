hargabuah = {'apel': 5000,
             'jeruk': 8500,
             'mangga': 7800,
             'duku': 6500}

def rataharga():
    rata = sum(hargabuah.values())/len(hargabuah)
    print('harga rata-rata dari satuan harga buah adalah: Rp',rata)

rataharga()