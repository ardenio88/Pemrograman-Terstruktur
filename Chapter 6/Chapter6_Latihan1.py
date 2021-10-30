def ispythagoras(a, b, c):
    if c**2 == a**2 + b**2:
        triplepythagoras = True
    else:
        triplepythagoras = False
    if triplepythagoras is True:
        print('a =', a, ',b =', b, ',c =', c, '  --> True')
    else:
        print('a =', a, ',b =', b, ',c =', c, '  --> False')


ispythagoras(3, 4, 5)
ispythagoras(5, 9, 12)
ispythagoras(8, 6, 10)
ispythagoras(7, 8, 11)
ispythagoras(60, 91, 109)
