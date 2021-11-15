bil = [2, 4, 5, 6, 7]
biltup = tuple(bil)


def kuadrat(x):
    hasilkuad = []
    for i in range(len(x)):
        hasilkuad.append(x[i]**2)
    return hasilkuad


print(kuadrat(biltup))
