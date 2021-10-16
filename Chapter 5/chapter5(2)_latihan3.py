banyak = 0
sum = 0
for i in range(100):
    bil = i + 1
    if bil % 2 != 0:
        banyak += 1
        sum += bil
        print(bil)
print("Banyak bilangan ganjil = " + str(banyak))
print("Jumlah bilangan ganjil = " + str(sum))
