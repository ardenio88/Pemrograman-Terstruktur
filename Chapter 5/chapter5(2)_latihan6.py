from random import randint
kunci = randint(0, 100)
health = 100
print("-              Welcome to the game                -")
print("+ Saya telah memilih angka bulat antara 0 s/d 100 +")
print("~          $ guess it and win the prize $         ~")
print("*           x you have 100 health bar x           *")
print("#                777 GOOD LUCK 777                #")
while True:
    print("[" + str(health) + "]")
    jawaban = input("Masukkan angka : ")
    if (int(jawaban) < kunci):
        print()
        print("!!! TOO SMALL !!!")
        print("Health -2")
        print()
        health -= 2
    if (int(jawaban) > kunci):
        print()
        print("!!! TOO BIG !!!")
        print("Health -2")
        print()
        health -= 2
    if (health <= 0):
        print("GAME OVER")
        break
    if (int(jawaban) == kunci):
        print("--------------------------")
        print("$$$      JACKPOT       $$$")
        print("CONGRATS ON $7777777 PRIZE")
        print("$$$      JACKPOT       $$$")
        print("--------------------------")
        print("SCORE : " + str(health))
        break
