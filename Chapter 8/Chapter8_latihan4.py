
listsayur = ['bayam', 'kangkung', 'wortel', 'selada']


def tambahdata():
    sayurtambah = input('Sayur yang ingin ditambahkan :')
    listsayur.append(sayurtambah)


def hapusdata():
    try:
        sayurhapus = input('Sayur yang ingin dihapus :')
        listsayur.remove(sayurhapus)
    except ValueError:
        print('Sayur tidak terdapat di data')


def datasayur():
    no = 1
    for x in range(len(listsayur)):
        print(str(no)+".", listsayur[x])
        no += 1


while True:
    print("\nMenu:\nA. Tambah Data Sayur\nB. Hapus Data Sayur\nC. Tampilkan Data Sayur\nD. Akhiri Sesi\n")
    pilihan = input("Pilihan Anda:")
    if pilihan == "A":
        tambahdata()
    if pilihan == "B":
        hapusdata()
    if pilihan == "C":
        datasayur()
    if pilihan == "D":
        break
