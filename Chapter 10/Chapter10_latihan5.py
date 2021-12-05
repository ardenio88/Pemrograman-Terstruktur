myfile = open('e:/listnum.txt', 'r')
teks = myfile.readlines()
convteks = []
ok = []
for i in teks:
    convteks.append((i.strip()))
print(convteks)

for x in range(len(convteks)):
    ok.append((convteks[x]).split("|"))
myfile2 = open('e:/hasil.txt', 'w+')
for y in range(len(ok)):
    hasil = int(ok[y][0]) + int(ok[y][1])
    myfile2.write(str(hasil)+"\n")
