mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
mhs1 = []
mhstgl = []

for x in range(len(mhs)):
       mhs1.append(mhs[x].split(':'))
for y in range(len(mhs1)):
       ok = (mhs1[y][2].split("-"))
       hasil = [ok[2], ok[1], ok[0]]
       mhstgl.append("/".join(hasil))
print("="*62)
print('NIM'.ljust(7), end='')
print('NAMA MAHASISWA'.ljust(22), end='')
print("TGL LAHIR".ljust(20), end='')
print("TEMPAT LAHIR")
print("-"*62)
for z in range(len(mhs1)):
       print(mhs1[z][0].ljust(7), end='')
       print(mhs1[z][1].ljust(22), end='')
       print(mhstgl[z].ljust(20), end='')
       print(mhs1[z][3])
print("-"*62)
