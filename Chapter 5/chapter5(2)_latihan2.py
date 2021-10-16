bil = 0
banyak = 0
while(bil <= 100):
    if(bil % 2 != 0):
        print(bil)
        banyak += 1
    bil += 1
print("Banyak Bilangan Ganjil : " + str(banyak))