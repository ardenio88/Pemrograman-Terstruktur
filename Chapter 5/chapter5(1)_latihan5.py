kodekaryawan = input("Masukkan kode karyawan:")
namakaryawan = input("Masukkan nama karyawan:")
tipegolongan = input("Masukkan golongan:")
statuskaryawan = input("Masukkan status:")
jumlahanak = 0
tunjanganmenikah = 0
tunjangananak = 0
if statuskaryawan == "Menikah":
    jumlahanak = input("Masukkan jumlah anak:")
else:
    statuskaryawan = "Belum Menikah"
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
if statuskaryawan == "Menikah":
    tunjanganmenikah = gajipokok*(10/100)
if int(jumlahanak) > 0:
    tunjangananak = int(jumlahanak)*(gajipokok*(5/100))
elif jumlahanak == "-":
    tunjangananak = 0
gajikotor = gajipokok + tunjanganmenikah + tunjangananak
gajipotongan = gajikotor*(potongan/100)

print("==================================")
print("   STRUK RINCIAN GAJI KARYAWAN    ")
print("----------------------------------")
print("Nama Karyawan     :" + namakaryawan + "(" + kodekaryawan + ")")
print("Golongan          :" + tipegolongan)
print("Status Menikah    :" + statuskaryawan)
print("Jumlah Anak       :" + str(jumlahanak))
print("----------------------------------")
print("Gaji Pokok        :" + "Rp " + str(gajipokok))
print("Tunjangan Menikah :" + "Rp " + str(tunjanganmenikah))
print("Tunjangan Anak    :" + "Rp " + str(tunjangananak))
print("----------------------------------+")
print("Gaji Kotor        :" + "Rp " + str(gajikotor))
print("Potongan" + "("+str(potongan)+"%)    :" + "Rp " + str(gajipotongan))
print("----------------------------------")
print("Gaji Bersih        :" + "Rp " + str(gajikotor-gajipotongan))
