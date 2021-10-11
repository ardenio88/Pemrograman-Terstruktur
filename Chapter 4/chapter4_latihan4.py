import math
jarakab = 125
kecepatanab = 62
waktuab = int(jarakab/kecepatanab)*60
istirahatb = 45
jarakbc = 256
kecepatanbc = 70
waktubc = int(jarakbc/kecepatanbc)*60
totalwaktumenit = waktuab+istirahatb+waktubc
totalwaktujamdesimal = totalwaktumenit/60
waktubelakang = math.floor((6+totalwaktujamdesimal) % 1 / 0.25*15)
totalwaktujam = math.floor(totalwaktumenit/60) + waktubelakang/100
waktudepan = math.floor(6+totalwaktujamdesimal)
print("waktu yang dibutuhkan dalam menit = " + str(totalwaktumenit))
print("waktu yang dibutuhkan dalam jam = " + str(totalwaktujam))
print("perkiraan waktu Pak amir sampai = " + str(waktudepan) + '.' + str(waktubelakang))
