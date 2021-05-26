import os
os.system('color a')
setting = int(input("Apakah library Numpy dan Matplotlib sudah anda install? 1: Ya, 2: Tidak>>"))
if setting == 1:
    os.system('pip install numpy')
    os.system('pip install matplotlib')
else:
    print("Baik kita lanjutkan!")
os.system('python code/contoh.py')
k=input("Tekan ENTER untuk exit") 