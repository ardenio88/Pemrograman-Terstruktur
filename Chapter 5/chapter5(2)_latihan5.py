from random import randint
kunci = randint(0, 100)
print("-              Welcome to the game                -")
print("+ Saya telah memilih angka bulat antara 0 s/d 100 +")
print("~          $ guess it and win the prize $         ~")
print("#                777 GOOD LUCK 777                #")
while True:
    jawaban = input("Masukkan angka : ")
    if (int(jawaban) < kunci):
        print()
        print("TOO SMALL")
        print()
    if (int(jawaban) > kunci):
        print()
        print("TOO BIG")
        print()
    if (int(jawaban) == kunci):
        print("--------------------------")
        print("$$$      JACKPOT       $$$")
        print("CONGRATS ON $7777777 PRIZE")
        print("$$$      JACKPOT       $$$")
        print("--------------------------")
        break
