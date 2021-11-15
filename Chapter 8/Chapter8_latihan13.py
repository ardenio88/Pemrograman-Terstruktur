nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80}, {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90}, {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30}, {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}]


def sortdnilaiakhir():
    i = 0
    for x in range(len(nilaiMhs)):
        nilaiakhir = (nilaiMhs[i]['mid'] + nilaiMhs[i]['uas']*2)/3
        nilaiMhs[i]['akhir'] = nilaiakhir
        i += 1
    print(sorted(nilaiMhs, key=lambda x: x['akhir'], reverse=True))


sortdnilaiakhir()
