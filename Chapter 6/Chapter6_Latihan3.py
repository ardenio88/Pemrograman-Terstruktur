def faktorialc(a, b):
    hasilafac = 1
    aminb = a - b
    hasilaminbfac = 1
    hasilbfac = 1
    for x in range(1, a+1):
        hasilafac *= x
    for y in range(1, aminb+1):
        hasilaminbfac *= y
    for z in range(1, b+1):
        hasilbfac *= z
    hasilakhir = hasilafac / (hasilaminbfac * hasilbfac)
    print('Hasil soal Kombinasi', a, b, 'adalah', hasilakhir)


def faktorialp(a, b):
    hasilafac = 1
    aminb = a - b
    hasilaminbfac = 1
    for x in range(1, a+1):
        hasilafac *= x
    for y in range(1, aminb+1):
        hasilaminbfac *= y
    hasilakhir = hasilafac / hasilaminbfac
    print('Hasil soal Permutasi', a, b, 'adalah', hasilakhir)


faktorialc(5, 3)
faktorialp(10, 7)
