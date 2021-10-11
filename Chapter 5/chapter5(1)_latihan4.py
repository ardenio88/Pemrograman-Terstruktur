kodekaryawan = input("Masukkan kode karyawan:")
namakaryawan = input("Masukkan nama karyawan:")
tipegolongan = input("Masukkan golongan:")
gajipokok = 0
potongan = 0
# GOLONGAN WAJIB KAPITAL
if tipegolongan == "A":
    gajipokok = 10000000
    potongan = 2.5
elif tipegolongan == "B":
    gajipokok = 8500000
    potongan = 2
elif tipegolongan == "C":
    gajipokok = 7000000
    potongan = 1.5
elif tipegolongan == "D":
    gajipokok = 5500000
    potongan = 1
gajipotongan = gajipokok*(potongan/100)
print("==================================")
print("   STRUK RINCIAN GAJI KARYAWAN    ")
print("----------------------------------")
print("Nama Karyawan     :" + namakaryawan + "(" + kodekaryawan + ")")
print("Golongan          :" + tipegolongan)
print("----------------------------------")
print("Gaji Pokok        :" + "Rp " + str(gajipokok))
print("Potongan" + "("+str(potongan)+"%)    :" + "Rp " + str(gajipotongan))
print("----------------------------------")
print("Gaji Bersih        :" + "Rp " + str(gajipokok-gajipotongan))
