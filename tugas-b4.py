print('Tugas Praktikum 4'.center(35))
nama = 'Baso Rahmat Hidayah. R'
nim  = '231031041'
prodi= 'Sistem Informasi B'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''

print()
str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON

print('str1 =' , str1)
a = str1.upper()                    # Membuat string menjadi huruf besar
b = a.strip('NEUMANN')              # Menghilangkan kata NEUMAN dalam string
c = 'NEUMANN ' + b.upper()          # Menambahkan kata neuman yang hilang tadi ke awalan string
print('output =',c)

print()

str2 = 'duFort Frankel Von Neumann'
#output: dfv neumann

print('str2 =', str2)
a = str2.lower()                    # Membuat string menjadi huruf kecil
b = a[19:]                          # Menampilkan index string ke 19 sampai akhir
c = 'dfv ' + b                      # Menambahkan kata 'dfv' ke string
print('output =', c)

print()

str3 = 'duFort Frankel Von Neumann'
#output: DUFORT F V N

print('str3 =', str3)
a = str3.upper()                    # Membuat string menjadi uppercase/huruf besar
b = a[0:6]                          # Menampilkan index 0 sampai 6
c = a[7]                            # Menampilkan index 7
d = a[15]                           # Menampilkan index 5
e = a[19]                           # Menampilkan index 19, cara susah
print('output =', b,c,d,e)          # Menampilkan semua variabel yg berisi index string

print()

str4 = 'duFOrt Frankel Von Neumann'
#output: N duFort f v

print('str4 =', str4)
a = str4.title()                    # Mengubah string jadi huruf kecil
b = a.replace('D','d') 
c = b.replace('f','F')              # Variabel a dan b merubah output menjadi 'duFort Frankel Von Neumann'
d = b.lower()                       # Mengubah variabel b menjadi lowercase
e = a[19]                           # Mengambil index ke 19 dari variabel a = 'N'
f = c[0:6]                          # Menagambil index dari 0 sampai 6 variabel c = 'duFort'
g = d[7]                            # Mengambil index ke 7 dari variabel d = 'f'
h = d[15]                           # Mengambil index ke 15 dari variabel d = 'v'
print('output =', e,f,g,h)

print()

str5 = 'DuFort Frankel Von Neumann'
#output: NEUMANN d f v

print('str5 =', str5)
a = str5.replace(str5, 'Neumann')   # Hanya menyisakan kata 'Neumann'
b = str5.lower()                    # Mengubah variabel str5 menjadi lowercase/huruf kecil
c = a.upper()                       # Mengubah variabel a = 'Neumann' menjadi uppercase/huruf besar
d = b[0]                            # Mengambil index ke 0 dari variabel b 
e = b[7]                            # Mengambil index ke 7 dari variabel b
f = b[15]                           # Mengambil index ke 15 dari variabel b
print('output =', c,d,e,f)

print()

str6 = 'duFort Frankel Von Neumann'
#output: NEUMANN DFV

print('str6 =', str6)
a = str5.replace(str5, 'Neumann')   # Hanya menyisakan kata 'Neumann'
b = str5.upper()                    # Mengubah variabel str5 menjadi uppercase/huruf besar
c = a.upper()                       # Mengubah variabel a = 'Neumann' menjadi uppercase/huruf besar
d = b[0]                            # Mengambil index ke 0 dari variabel b 
e = b[7]                            # Mengambil index ke 7 dari variabel b
f = b[15]                           # Mengambil index ke 15 dari variabel b
print('output =', c,d+e+f)

print()

str7 = '@duFort Frankel Von Neumann$'
#output: duFort Frankel Von NEUMANN

print('str7 =', str7)
a = str7.strip('@$')                # Menghilangkan tanda baca
b = a.strip('Neumann')              # Menghilangkan kata 'Neumann' dalam variabel a
c = str7.replace(str7, 'Neumann')   # Menyisakan kata 'Neumann' dalam variabel str7
d = c.upper()                       # Mengubah variabel c = 'Neumann' dangan upppercase 
print('output =', b+d)              # Menampilkan var b dan d  

print()

str8 = '#duFort@Frankel@Von@Neumann$'
#output: duFort Frankel Von Neumann

print('str8 =', str8)
a = str8.strip('#$')                # Menghapus tanda # dan $
b = a.replace('@',' ')              # Mengganti tanda @ dengan spasi
print('output =', b)

print()

str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
#output: duFort Frankel Von Neumann

print('str9 =',str9)
a = str9.strip('@$')                # Menghapus tanda paling kanan dan kiri
b = a.replace('@#^', ' ')           # Mengubah tanda yg memisahkan kalimat 1 dan 2 menjadi spasi
c = b.replace('*#(', ' ')           # Mengubah tanda yg memisahkan kalimat 2 dan 3 menjadi spasi
d = c.replace('(#(', ' ')           # Mengubah tanda yg memisahkan kalimat 3 dan 4 menjadi spasi
print('output =', d) 

print()

str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
#output: duFort Frankel Von Neumann

print('str10 =',str10)
a = str10.strip('@^')               # Menghapus tanda paling kiri dan kanan
b = a.replace('@!^',' ')            # Mengubah tanda yg memisahkan kalimat 1 dan 2 menjadi spasi
c = b.replace('!1(',' ')            # Mengubah tanda yg memisahkan kalimat 2 dan 3 menjadi spasi
d = c.replace('(!(',' ')            # Mengubah tanda yg memisahkan kalimat 3 dan 4 menjadi spasi
e = d.title()                       # Mengubah variabel d menjadi title atau semua kalimat diawali dengan uppercase
f = e.replace('D','d')              # Mengubah kata D menjadi d
g = f.replace('f','F')              # Mengubah kata f menjadi F
print('output =', g)