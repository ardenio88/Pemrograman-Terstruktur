data = ['apel', 'rambutan', 'jeruk', 'durian']
datatup = tuple(data)


def sortstringbychar(x):
    datasort = sorted(x, key=len, reverse=True)
    return datasort


print(sortstringbychar(datatup))
