''' SOAL
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan Alat Tulis Kantor (ATK). Pilih 5 barang ATK dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [Nama Lengkap,
         mahasiswa@ith.ac.id,
         PT. ABC Design,
         JL. BALAIKOTA NO.1,
         PAREPARE,
         Nama Kasir,
         25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list 5 barang:
djual = [['Barang1','Barang2','Barang3','Barang4','Barang5'],
         ['B2001','B2002','B2003','B2004','B2005'],
         [55,25,150,5,10],
         [2,2,2,2,2]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing

                                   PT. ABC DESIGN
                            JL. BALAIKOTA NO.1 PAREPARE
                            e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|-|--   13    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   B2001       | Barang1           |      Rp27000,-|    2   |     Rp54000,-|
2   B2002       | Barang2           |      Rp75000,-|    2   |    Rp150000,-|
3   B2003       | Barang3           |      Rp12000,-|    2   |     Rp24000,-|
4   B2004       | Barang4           |      Rp10000,-|    2   |     Rp20000,-|
5   B2005       | Barang5           |       Rp3000,-|    2   |      Rp6000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           10   |    Rp254000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|-----------------------------------77--------------------------------------|
Summary:
Harga tertinggi adalah    : Rp750000,- (B2002 - Barang 2)
Harga terendah  adalah    : Rp3000,-   (B2005 - Barang 5)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023




                                                          NAMA LENGKAP      
                                                          ------------
                                                             MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Baso Rahmat Hidayah. R
NIM\t\t: 231031041
Kelas\t\t: Sistem Informasi B''')

#Answer in below

mdata = ['Baso Rahmat Hidayah. R',
         'basorahmat11@gmail.com',
         'PT. ABC Design',
         'JL. BALAIKOTA NO.1',
         'PAREPARE',
         'Ahmad',
         '3 Mei 2005']

djual = [['Pulpen','Buku','Spidol','Pensil','Stabilo'],
         ['B2001','B2002','B2003','B2004','B2005'],
         [5,5,10,3,5],
         [2,2,2,2,2]]


print()
sp=77

print(mdata[2].center(sp))
aa= mdata[3],mdata[4]
ab= ' '.join(aa)
print(ab.center(sp))
ac= 'e-Mail: '+mdata[1]
r = 1000
print(ac.center(sp))
print()
print()

print(f'''MANAJER           : {mdata[0]}
KASIR             : {mdata[-2]}
Tanggal Pembelian : {mdata[-1]}''')
print('-'*sp)
print('No. '+'|'+'Kode Barang'.center(13)+'|'+'Nama Barang'.center(19)+'|'+'H. Satuan'.center(15)+'|'+'Jumlah'.center(8)+'|'+'Total'.center(14))
print('2.  '+'|'+djual[0][0].center(13)+'|'+djual[1][0].center(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][0]}'.center(14))
print('1.  '+'|'+djual[0][1].center(13)+'|'+djual[1][1].center(19)+'|'+f'Rp{djual[2][1]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][1]}'.center(14))
print('3.  '+'|'+djual[0][2].center(13)+'|'+djual[1][2].center(19)+'|'+f'Rp{djual[2][2]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][2]}'.center(14))
print('4.  '+'|'+djual[0][3].center(13)+'|'+djual[1][3].center(19)+'|'+f'Rp{djual[2][3]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][3]}'.center(14))
print('5.  '+'|'+djual[0][4].center(13)+'|'+djual[1][4].center(19)+'|'+f'Rp{djual[2][4]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][4]}'.center(14))
print('-'*sp)

harga_satuan = (djual[2][0] + djual[2][1] + djual[2][2] + djual[2][3] + djual[2][4]) * r 
total_jumlah = sum(djual[3])
total_hasil = (djual[2][0] + djual[2][1] + djual[2][2] + djual[2][3] + djual[2][4]) * r * 2
print(f'SUBTOTAL: |     Rp{harga_satuan},-|   {total_jumlah}   |  Rp{total_hasil},- |'.rjust(77))

print('-'*sp)
rata_rata = (sum(djual[2]) / total_jumlah) * 2 * r
print(f'''Summary: 
Harga tertinggi adalah    : Rp{r*max(djual[2])},-  ({djual[1][2]} - {djual[0][2]})
Harga terendah adalah     : Rp{r*min(djual[2])},-   ({djual[1][3]} - {djual[0][3]})
Harga Rata-Rata pembelian : Rp{float(rata_rata):.2f}''')


print()
ca= mdata[4].capitalize()
aac= ca,mdata[-1]
aaj= ' '.join(aac)
aau= aaj.replace('pare','pare,')
print(aau.rjust(77))
print()
print()
print()
print()
print(mdata[0].rjust(77),'')
print(('-'*22).rjust(77))
print('MANAJER'.rjust(70))