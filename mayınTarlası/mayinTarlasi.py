# Basit mayın tarlası oyunu
import random

boyut = 0
while True:
    puan = 0
    boyut = int(input("Matris icin 10'dan buyuk boyut giriniz:"))
    if boyut < 10:
        boyut = int(input("Matris icin 10'dan buyuk boyut giriniz:"))
    else:
        break

gizli_mod = []
for i in range(boyut):
    gizli_mod.append("?" * boyut)
mayin_sayi = (boyut * boyut) * 3 // 10
acik_mod = []
for i in range(boyut):
    acik_mod.append("&" * boyut)

# mayın yerlestirme
for i in range(mayin_sayi):
    x = random.randint(0, boyut - 1)
    y = random.randint(0, boyut - 1)
    while True:
        if acik_mod[x][y] == "&":
            break
        else:
            x = random.randint(0, boyut - 1)
            y = random.randint(0, boyut - 1)
    degisken = acik_mod[x]
    degisken = degisken[0:y:] + "X" + degisken[y + 1::]
    acik_mod[x] = degisken

mayinlar = acik_mod.copy()
for i in range(boyut):
    for j in range(boyut):
        if acik_mod[i][j] == "X":
            degisecek_yer = mayinlar[i]
            degisecek_yer = degisecek_yer[0:j:1] + "X" + degisecek_yer[j + 1::1]
            mayinlar[i] = degisecek_yer
        else:
            degisecek_yer = mayinlar[i]
            degisecek_yer = degisecek_yer[0:j:1] + " " + degisecek_yer[j + 1::1]
            mayinlar[i] = degisecek_yer

while True:
    sayac = 0
    while True:
        secim = int(input("Gormek istediginiz modu secin\n 1] Gizli mod\n 2] Acik mod\nSeciminiz:"))
        # gizli mod
        if secim == 1:
            for i in gizli_mod:
                print(" ".join(i))
            break
        # acik mod
        elif secim == 2:
            for i in acik_mod:
                print(" ".join(i))
            break
        else:
            secim = input("Lutfen gecerli bir secim giriniz!:")

    x, y = input("Satir ve sutun no giriniz:(0,0 seklinde):").split(",")
    x = int(x)
    y = int(y)
    while True:
        if acik_mod[x][y] == " ":
            print("Bu koordinatı daha önce seçtiniz")
            x, y = input("Satir ve sutun no giriniz:(0,0 seklinde):").split(",")
            x = int(x)
            y = int(y)
            continue
        else:
            break

    if x < boyut and x >= 0 and y < boyut and y >= 0:

        if acik_mod[x][y] == "X":
            print("Sectiğiniz koordinatta mayın var! KAYBETTINIZ!!")
            print("Puan:", puan)
            for i in mayinlar:
                print(" ".join(i))

            print("1)Oyuna devam")
            print("2)CIKIS")
            secim = input("Seçim yapın:")



        else:  # bosluk secme durumu
            if puan == int(boyut * boyut * 0.7):
                print("Oyunu kazandınız!Puanıız:", puan)
                print("1)Oyuna devam")
                print("2)CIKIS")
                secim = input("Seçim yapın:")
                continue
            else:
                break

            puan += 1

            # Acik mod silme :
            bosluk_yapma = acik_mod[x]
            bosluk_yapma = bosluk_yapma[0:y:1] + " " + bosluk_yapma[y + 1::1]
            acik_mod[x] = bosluk_yapma

            # Gizli mod silme :
            bosluk_yapma = gizli_mod[x]
            bosluk_yapma = bosluk_yapma[0:y:1] + " " + bosluk_yapma[y + 1::1]
            gizli_mod[x] = bosluk_yapma

            sayac = 0
            # köşe
            if (x == 0 and y == 0) or (x == 0 and y == boyut - 1) or (x == boyut - 1 and y == 0) or (
                    x == boyut - 1 and y == boyut - 1):
                # sol üst köşe
                sayac = 0
                if x == 0 and y == 0:
                    if acik_mod[0][1] == "X":
                        sayac += 1
                    if acik_mod[1][0] == "X":
                        sayac += 1
                    if acik_mod[1][1] == "X":
                        sayac += 1

                # sağ üst köşe

                elif x == 0 and y == boyut - 1:

                    if acik_mod[0][boyut - 2] == "X":
                        sayac += 1
                    if acik_mod[1][boyut - 2] == "X":
                        sayac += 1
                    if acik_mod[1][boyut - 1] == "X":
                        sayac += 1

                # sol alt köşe
                elif x == boyut - 1 and y == 0:
                    if acik_mod[boyut - 1][1] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][1] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][0] == "X":
                        sayac += 1

                # sağ alt köşe
                elif x == boyut - 1 and y == boyut - 1:
                    if acik_mod[boyut - 1][boyut - 2] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][boyut - 1] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][boyut - 2] == "X":
                        sayac += 1
                print("Sectiginiz koordinatin cevresinde {} tane mayin vardir".format(sayac))

            # kenar durumu
            elif [(x == 0 and y != 0) or (x == 0 and y != boyut - 1)] or [
                (y == 0 and x != 0) or (y == 0 and x != 0)] or [
                (x == boyut - 1 and y != 0) or (x == boyut - 1 and y != boyut - 1)] or [
                (y == boyut - 1 and x != 0) or (y == boyut - 1 and x != boyut - 1)]:
                # üst kenar
                if [(x == 0 and y != 0) or (x == 0 and y != boyut - 1)]:
                    if acik_mod[0][y - 1] == "X":
                        sayac += 1
                    if acik_mod[0][y + 1] == "X":
                        sayac += 1
                    if acik_mod[1][y - 1] == "X":
                        sayac += 1
                    if acik_mod[1][y] == "X":
                        sayac += 1
                    if acik_mod[1][y + 1] == "X":
                        sayac += 1

                # alt kenar   #her seferinde doğru çalışmıyo
                if [(x == boyut - 1 and y != 0) or (x == boyut - 1 and y != boyut - 1)]:
                    if acik_mod[boyut - 1][y - 1] == "X":
                        sayac += 1
                    if acik_mod[boyut - 1][y + 1] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][y - 1] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][y] == "X":
                        sayac += 1
                    if acik_mod[boyut - 2][y + 1] == "X":
                        sayac += 1

                # sol  kenar
                if (y == 0 and x != 0) or (y == 0 and x != 0):
                    if acik_mod[x - 1][0] == "X":
                        sayac += 1
                    if acik_mod[x + 1][0] == "X":
                        sayac += 1
                    if acik_mod[x - 1][1] == "X":
                        sayac += 1
                    if acik_mod[x][1] == "X":
                        sayac += 1
                    if acik_mod[x + 1][1] == "X":
                        sayac += 1

                # sağ kenar
                elif (y == boyut - 1 and x != 0) or (y == boyut - 1 and x != boyut - 1):
                    if acik_mod[x - 1][boyut - 1] == "X":
                        sayac += 1
                    if acik_mod[x + 1][boyut - 1] == "X":
                        sayac += 1
                    if acik_mod[x - 1][boyut - 2] == "X":
                        sayac += 1
                    if acik_mod[x][boyut - 2] == "X":
                        sayac += 1
                    if acik_mod[x + 1][boyut - 2] == "X":
                        sayac += 1
                print(sayac)
                break

            # ortada olma durumu
            else:
                if acik_mod[x - 1][y - 1] == "X":
                    sayac += 1
                if acik_mod[x][y - 1] == "X":
                    sayac += 1
                if acik_mod[x + 1][y - 1] == "X":
                    sayac += 1
                if acik_mod[x - 1][y] == "X":
                    sayac += 1
                if acik_mod[x + 1][y] == "X":
                    sayac += 1
                if acik_mod[x - 1][y + 1] == "X":
                    sayac += 1
                if acik_mod[x][y + 1] == "X":
                    sayac += 1
                if acik_mod[x + 1][y + 1] == "X":
                    sayac += 1
                print(sayac)
    else:
        print("Girdiğiniz degerler oyun alanı dışında kaldı. ")
        x, y = input("Satir ve sutun no (0,0) olacak sekilde girin:").split(",")
