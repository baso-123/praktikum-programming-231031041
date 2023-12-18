pwd_benar = 'si23b'
a = True
i = 0
limit = 3

while a :
        i += 1
        pwd = input('Masukkan password : ')
        if pwd == pwd_benar :
            print('Selamat Anda login')
            a = False
        else :
            print('Password salah')
            if i == limit :
                a = False
                print('Anda kehabisan kesempatan')
            else :
                print(f'Kesempatan Anda tersisa {limit-i} kali')