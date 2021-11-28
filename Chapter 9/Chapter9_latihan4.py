import random
def shufflestring(x, n):
    i = 0
    malist = []
    while i < n:
        shuff = ''.join(random.sample(x,len(x)))
        if shuff not in malist:
            malist.append(shuff)
            i += 1
    print(malist)

shufflestring("akua",10)