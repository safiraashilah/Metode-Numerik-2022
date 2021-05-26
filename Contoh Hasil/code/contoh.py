#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Metode Setengah Interval [Python 3.7]
def setengah_interval(X1,X2):
        print(" =========================================================\n",
             "Metode Setengah Interval Modul 2 Metode Numerik\n",
             "Nama: Satria Ginanjar \n",
             "NIM: 26050118130065 \n",
             "Kelas: Oseanografi B \n",
             "=========================================================\n")
        X1 = X1
        X2 = X2
        error = 1
        iterasi = 0
        while(error > 0.0001):
            iterasi +=1
            FXi = (float(X1)**3)+(float(X1)**2)-(3*X1)-3
            FXii = (float(X2)**3)+(float(X2)**2)-(3*X2)-3
            Xt = (X1 + X2)/2
            FXt = (float(Xt)**3)+(float(Xt)**2)-(3*Xt)-3
            if FXi * FXt > 0:
                X1 = Xt
            elif FXi * FXt < 0:
                X2 = Xt
            else:
                print("Akar Penyelesaian: ", Xt)      
            if FXt < 0:
                error = FXt * (-1)
            else:
                error = FXt
            if iterasi > 1000:
                print("Angka tak hingga")
                break
            print(iterasi, "|", FXi, "|", FXii, "|", Xt, "|", FXt, "|", error)
        print("Jumlah Iterasi: ", iterasi)
        print("Akar persamaan adalah: ", Xt)
        print("Toleransi Error: ", error)
        
# Metode Interpolasi Linier [Python 3.7]
def interpolasi_linier(X1):
        print(" =========================================================\n",
             "Metode Interpolasi Linier Modul 2 Metode Numerik\n",
             "Nama: Satria Ginanjar \n",
             "NIM: 26050118130065 \n",
             "Kelas: Oseanografi B \n",
             "=========================================================\n")
        X1 = X1
        X2 = X1 + 1
        error = 1
        iterasi = 0
        while(error > 0.0001):
            iterasi +=1
            FX1 = (float(X1)**3)+(float(X1)**2)-(3*X1)-3
            FX2 = (float(X2)**3)+(float(X2)**2)-(3*X2)-3
            Xt = X2 - ((FX2/(FX2-FX1)))*(X2-X1)
            FXt = (float(Xt)**3)+(float(Xt)**2)-(3*Xt)-3
            if FXt*FX1 > 0:
                X2 = Xt
                FX2 = FXt
            else:
                X1 = Xt
                FX1 = FXt  
            if FXt < 0:
                error = FXt * (-1)
            else:
                error = FXt
            if iterasi > 1000:
                print("Angka tak hingga")
                break
            print(iterasi, "|", FX1, "|", FX2, "|", Xt, "|", FXt, "|", error)
        print("Jumlah Iterasi: ", iterasi)
        print("Akar persamaan adalah: ", Xt)
        print("Toleransi Error: ", error)
        
# Metode Secant [Python 3.7]
def secan(X1):
        X1 = X1
        X2 = X1 - 1
        error = 1
        iterasi = 0
        while(error > 0.0001):
            iterasi +=1
            FX1 = (float(X1)**3)+(float(X1)**2)-(3*X1)-3
            FXmin = (float(X2)**3)+(float(X2)**2)-(3*X2)-3
            X3 = X1 - ((FX1)*(X1-(X2)))/((FX1)-(FXmin))
            FXplus = (float(X3)**3)+(float(X3)**2)-(3*X3)-3
            if FXplus < 0:
                error = FXplus * (-1)
            else:
                error = FXplus
            if error > 0.0001:
                X2 = X1
                X1 = X3
            else:
                print("Selesai")
            if iterasi > 1000:
                print("Angka tak hingga")
                break
            print(iterasi, "|", FX1, "|", FXmin, "|", X3, "|", FXplus, "|", error)
        print("Jumlah Iterasi: ", iterasi)
        print("Akar persamaan adalah: ", X3)
        print("Toleransi Error: ", error)

# Metode Newton-Rapson [Python 3.7]
def newton_rapson(X1):
        X1 = X1
        iterasi = 0
        akar = 1

        while (akar > 0.0001):
            iterasi += 1
            Fxn = (float(X1)**3)+(float(X1)**2)-(3*X1)-3
            Fxxn = (float(3*X1)**2)+(float(2*X1))-(3)
            xnp1 = X1 - (Fxn/Fxxn)
            fxnp1 = (xnp1**3)+(xnp1**2)-(3*xnp1)-3
            Ea = ((xnp1-X1)/xnp1)*100
            if Ea < 0.0001:
                X1 = xnp1
                akar = Ea*(-1)
            else:
                akar = xnp1
                print("Nilai akar adalah: ", akar)
                print("Nilai error adalah: ", Ea)
            if iterasi > 1000:
                break
            print(iterasi, "|", X1, "|", xnp1, "|", akar, "|", Ea)
        print("Jumlah Iterasi: ", iterasi)
        print("Akar persamaan adalah: ", xnp1)
        print("Toleransi Error: ", akar)   
print("Kode penggunaan akar-akar persamaan: \n",
      "1. Metode Setengah Interval \n",
      "2. Metode Interpolasi Linier \n",
      "3. Metode Secant \n",
      "4. Metode Newton-Rapson \n")
setting = int(input("Masukkan kode penggunaan akar-akar persamaan: "))
if (setting == 1):
    X1 = float(input("Masukkan Nilai Pertama Setengah Interval: "))
    X2 = float(input("Masukkan Nilai Kedua Setengah Interval: "))
    X = setengah_interval(X1,X2)
    print(X)
elif(setting == 2):
    X1 = float(input("Masukkan Nilai X1 untuk Interpolasi Linier: "))
    X = interpolasi_linier(X1)
    print(X)
elif(setting == 3):
    X1 = float(input("Masukkan Nilai X1 untuk Secant: "))
    X = interpolasi_linier(X1)
    print(X)
else:
    X1 = float(input("Masukkan Nilai X1 untuk Newton Rapson: "))
    X = interpolasi_linier(X1)
    print(X)


# In[ ]:




