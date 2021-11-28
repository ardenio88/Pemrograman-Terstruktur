def starformation(n):
    space = 2*n-1
    for x in range(n):
        print(('*'*(2*x+1)).center(space))


def starformation2(n):
    j = n-1
    space = 2 * n - 1
    for x in range(n):
        print(('*'*(2*j+1)).center(space))
        j -= 1


starformation(5)
starformation2(4)
