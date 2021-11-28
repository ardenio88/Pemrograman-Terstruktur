nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80}, {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50}, {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

print("="*40)
print('NIM'.ljust(7), end='')
print('NAMA'.ljust(15), end='')
print('N.MID'.ljust(9), end='')
print('N.UAS')
print("-"*40)

for x in range(len(nilai)):
    print(nilai[x]['nim'].ljust(7), end='')
    print(nilai[x]['nama'].upper().ljust(15), end='')
    print(str(nilai[x]['mid']).ljust(9), end='')
    print(str(nilai[x]['uas']))

print("-"*40)
