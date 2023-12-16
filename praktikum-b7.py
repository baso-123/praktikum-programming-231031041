import os
os.system('cls')

a = True

while a :
    jawab = input('Apakah ingin lanjutkan? (yes/no) : ')
    if jawab == 'yes' :
        
        os.system('cls')
        print('Selamat datang lagi')
        a = True
        
    elif jawab == 'no' :
        
        print('Sampai ketemu lagi :D')
        a = False
        
    else :
        
        os.system('cls')
        print('Jangan aneh-aneh deh :D')
        a = True
