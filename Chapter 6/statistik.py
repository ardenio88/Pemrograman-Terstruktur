def sum(*mydata):
    jumlah = 0
    for data in mydata:
        jumlah += data
    return jumlah


def average(*mydata):
    i = 0
    for data in mydata:
        i += 1
    hasil = sum(*mydata)/i
    return hasil


def maximal(*mydata):
    nilaimax = max(*mydata)
    return nilaimax


def minimum(*mydata):
    nilaiminimum = min(*mydata)
    return nilaiminimum
