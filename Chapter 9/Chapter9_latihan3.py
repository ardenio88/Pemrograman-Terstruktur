def starformation(n):
    global space
    space = 2*n-1
    for x in range(n):
        print(('*'*(2*x+1)).center(space))


def starformation2(n):
    j = n-1
    for x in range(n):
        print(('*'*(2*j+1)).center(space))
        j -= 1

def starformation3(n):
    if n % 2 == 0:
        starformation(n//2)
        starformation2(n//2)
    else:
        starformation((n//2)+1)
        starformation2((n//2))


starformation3(8)
