from datetime import *
tgl1 = datetime.date(datetime.now())
try:
    tglinput = input("Masukkan tanggal yang ingin dicari(YYYY-MM-DD):")
    a = tglinput.split("-")
    tglbaru = date(int(a[0]), int(a[1]), int(a[2]))


    def diffdate(x):
        perbedaanhari = tgl1 - x
        return perbedaanhari.days


    print('Selisih hari dari sekarang dan tanggal yang diinput adalah', diffdate(tglbaru), 'hari')
except ValueError:
    print('Maaf Input Tidak Valid')
