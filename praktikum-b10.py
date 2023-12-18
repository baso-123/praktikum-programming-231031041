import os
os.system('cls')
def judul() :
    print('Program Menghitung Volume dan Luas Permukaan'. center(45))
    print('Bangun Ruang Balok'. center(45))
    print()

def inputan() :
    panjang = float(input('Masukkan Panjang : '))
    lebar   = float(input('Masukkan Lebar   : '))
    tinggi  = float(input('Masukkan Tinggi  : '))
    return panjang,lebar,tinggi
    
def hitung(panjang,lebar,tinggi) :
    volume = panjang*lebar*tinggi
    luas_permukaan = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
    luas_non_tutup = luas_permukaan - panjang*lebar
    return volume,luas_permukaan,luas_non_tutup

def tampilan(pesan,nilai) :
    print(f'Nilai {pesan} : {nilai} ')
    
def pilihan() :
    pilih = input('Apakah lanjut? [yes/no] : ')
    if pilih == 'yes' : 
        a = True
    else :
        a = False
        print('Terima Kasih')
    return a

def main() :
    judul()                                                             # Judul
    panjang,lebar,tinggi = inputan()                                    # Inputan
    volume,luas_permukaan,luas_non_tutup = hitung(panjang,lebar,tinggi) # Hitung
    # Tampilan
    tampilan('Volume',volume)
    tampilan('Luas Permukaan',luas_permukaan)
    tampilan('Luas Permukaan Tanpa Tutup',luas_non_tutup)               
    a = pilihan()                                                       # Pilihan
    return a

a = True
while a :
    a = main()