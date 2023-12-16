print('praktikum-5')

nim = [2,3,1,0,3,1,0,4,1]
print(nim)

# akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])

# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6]',nim[-6])
print('item indeks 5: [-4]',nim[-4])
print('item indeks -7: [2]',nim[2])
print('item indeks 2: [-7]',nim[-7])

# akses indeks batas
print('item indeks : ',nim[1:])
print(f'item indeks 1,2..... : {nim[1:]}')
print(f'item indeks 3,4..... : {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[-1]}')
print(f'item indeks [:4]: {nim[-5]}')

# pengirisan
print(f'item indeks 1:2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')

# Nested List
kelas = [('Kalkulus',2),
         ('Pemrograman',3)]
kelas.append(('Agama Islam',2))
kelas.append(('Bahasa Indonesia',2))
kelas.append(('Pancasila',2))

print()

# Mata kuliah 1 : Mata kuliah 1 dengan 2 sks
print(f'Mata Kuliah 1 : {kelas[0][0]} dengan {kelas[0][1]} sks')

# Mata kuliah 2 : Mata kuliah 2 dengan 3 sks
print(f'Mata Kuliah 2 : {kelas[1][0]} dengan {kelas[1][1]} sks')

# Mata kuliah 3 : Mata kuliah 3 dengan 2 sks
print(f'Mata Kuliah 3 : {kelas[2][0]} dengan {kelas[2][1]} sks')

# Mata kuliah 4 : Mata kuliah 4 dengan 2 sks
print(f'Mata Kuliah 4 : {kelas[3][0]} dengan {kelas[3][1]} sks')

# Mata kuliah 5 : Mata kuliah 5 dengan 2 sks
print(f'Mata Kuliah 5 : {kelas[4][0]} dengan {kelas[4][1]} sks')

print()

data = [('Baso',2023,'Aktif'),
        (76,98,89,97,99),
        [2,3,2,2,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa : Baso
print(f'Nama mahasiswa : {data[0][0]}')

# Inisial Baso : B
print(f'Inisial nama : {data[0][0][0]}')

# NIM Baso : 231031041
nim_int = int(''.join(map(str, nim))) 
print(f'NIM {data[0][0]} : {nim_int}')

# Program Baso : S1-Reguler Sistem Informasi B
print(f'Program {data[0][0]} : {data[3][0]} {data[3][1]}')

# Angkatan Baso : Ganjil-2023
print(f'Angkatan {data[0][0]} : {data[3][2]}-{data[0][1]}')

# Total sks Baso adalah : 11
print(f'Total sks {data[0][0]} adalah : {sum(data[2])}')

# Jumlah Nilai Baso : 5
print(f'Jumlah Nilai {data[0][0]} : {len(data[2])}')

# Nilai tertinggi Baso : 99
print(f'NIlai tertinggi {data[0][0]} : {max(data[1])}')

# Nilai terendah Baso : 76
print(f'NIlai terendah {data[0][0]} : {min(data[1])}')

# Rata-rata nilai Baso : 91.8
rata = sum(data[1]) / len(data[1])
print(f'Rata-rata nilai {data[0][0]} : {rata}')
