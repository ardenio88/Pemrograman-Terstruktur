nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80}, {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50}, {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]


for x in range(len(nilai)):
    nilaiakhir = (nilai[x]['mid'] + nilai[x]['uas']*2)//3
    nilai[x]['akhir'] = nilaiakhir
for y in range(len(nilai)):
    if nilai[y]['akhir'] >= 60:

        nilai[y]['lulus'] = 'LULUS'
    else:
        nilai[y]['lulus'] = 'TIDAK LULUS'
print("="*60)
print('NIM'.ljust(7), end='')
print('NAMA'.ljust(15), end='')
print('N.MID'.ljust(9), end='')
print('N.UAS'.ljust(8), end='')
print('N.AKHIR'.ljust(12), end='')
print('STATUS')
print("-"*60)

i = 0
for x in range(len(nilai)):
    print(nilai[i]['nim'].ljust(7), end='')
    print(nilai[i]['nama'].upper().ljust(15), end='')
    print(str(nilai[i]['mid']).ljust(9), end='')
    print(str(nilai[i]['uas']).ljust(8), end='')
    print(str(nilai[i]['akhir']).ljust(12), end='')
    print(str(nilai[i]['lulus']))
    i += 1
print("-"*60)
