import os
import random
import pyconio

def jatekoslepes(a, b, tabla):
    megy = True
    while megy:
        lepes = input("Kérem adja meg azt a pozíciót ahová kíván tenni x-et (1-{0}): ".format(a*b))
        try:
            lepes = int(lepes)
            if (lepes > 0) and (lepes < a*b+1):
                if ures(tabla, lepes):
                    megy = False
                    karakterir (tabla, "X", lepes)
                else:
                    print("Sajnálom a mező már foglalt!")
            else:
                print("Kérem 1 és {0} közötti egész számot adjon meg!".format(a*b))
        except:
            print("Kérem számot adjon meg!")

def karakterir(tabla, karakter, poz):
    tabla[poz-1] = karakter

def geplepes(tabla, a, b, c, tele):
    tablamasolat = tabla.copy()
    if c >= 4:
        d = 3
    else:
        d = 2

    for e in range (len(tabla)):
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "O"
            if nyert(tablamasolat, "O", a, b, c):
                return karakterir(tabla, "O", e+1)
            else:
                tablamasolat = tabla.copy()

    for e in range (len(tabla)):
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "X"
            if nyert(tablamasolat, "X", a, b, c):
                return karakterir(tabla, "O", e+1)
            else:
                tablamasolat = tabla.copy()

    for e in range (len(tabla)):
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "X"
            if nyert(tablamasolat, "X", a, b, c-1):
                return karakterir(tabla, "O", e+1)
            else:
                tablamasolat = tabla.copy()
    

    for e in range (len(tabla)):
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "O"
            tablamasolata = tablamasolat.copy()
            for t in range (len(tabla)):
                if ures(tablamasolata, t+1):
                    tablamasolata[t] = "O"
                    if nyert(tablamasolata, "O", a, b, d):
                        return karakterir(tabla, "O", t+1)
                    else:
                        tablamasolata = tablamasolat.copy()
            tablamasolat = tabla.copy()

    if tele < 2:
        lista = []
        for e in range (len(tabla)):
            if tabla[e] == "X":
                if e % b == 0:
                    if e+b+1 > 0 and e-b+1 <= a*b and ures(tabla, e+b+1):
                        lista.append(e+b+1)
                    if e-b+1 > 0 and e-b+1 <= a*b and ures(tabla, e-b+1):
                        lista.append(e-b+1) 
                    lista.append(e+1)
                elif (e+1) % b == 0:
                    if e-b-1 > 0 and e-b+1 <= a*b and ures(tabla, e-b-1):
                        lista.append(e-b-1)
                    if e+b-1 > 0 and e-b+1 <= a*b and ures(tabla, e+b-1):
                        lista.append(e+b-1)
                    lista.append(e-1)
                else:
                    if e-b > 0 and e-b <= a*b and ures(tabla, e-b):
                        lista.append(e-b)
                    if e+b > 0 and e+b <= a*b and ures(tabla, e+b):
                        lista.append(e+b)
                
                r = random.randrange(len(lista))
                lepes = lista[r]
                return karakterir(tabla, "O", lepes)

        lista = []
        for e in range (len(tabla)):
            if tabla[e] == "O":
                if (e+1) > 0 and (e+1) < a*b and ures(tabla, e+2):
                    lista.append(e+1)
                if (e-1) > 0 and (e-1) < a*b and ures(tabla, e):
                    lista.append(e-1)
                if (e+b) > 0 and (e+b) < a*b and ures(tabla, e+b+1):
                    lista.append(e+b)
                if (e-b) > 0 and (e-b) < a*b and ures(tabla, e-b+1):
                    lista.append(e-b)

        r = random.randrange(len(lista))
        lepes = lista[r]
        return karakterir(tabla, "O", lepes)

def ures(tabla, lepes):
    if tabla[lepes-1] == "X" or tabla[lepes-1] == "O":
        return False
    else:
        return True

def tablakeszites(a, b, tabla):
    for e in range(a):
        for j in range(b):
            if tabla[e*a+j] == "X":
                print("|{}{:<4}{}".format(pyconio.textcolors[pyconio.RED], tabla[e*a+j] ,pyconio.textcolors[pyconio.WHITE]), end ="")
            elif tabla[e*a+j] == "O":
                print("|{}{:<4}{}".format(pyconio.textcolors[pyconio.GREEN], tabla[e*a+j] ,pyconio.textcolors[pyconio.WHITE]), end ="")
            else:
                print("|{:<4}".format(tabla[e*a+j]), end ="")
        print("|")
        print(j*"-----"+"------")

def mentes(jatekos, szamitogep):
    print("Jó játék volt :)")
    kerdes = int(input("Szeretnéd elmenteni a játék eredményét? 1 = igen, 0 = Nem \n "))
    if kerdes == 1:
        with open('mentes.txt', 'w') as f:
            jatekos = str(jatekos)
            szamitogep = str(szamitogep)
            f.write(jatekos + "\n")
            f.write(szamitogep)
    main()

def betoltes():
    allas = []
    with open('mentes.txt') as f:
        for sor in f:
            sor = sor.rstrip("\n")
            allas.append(sor)
    
    f.close()

    print("Az állás {0}-{1}".format(int(allas[0]), int(allas[1])))
    return allas

def nyert(tabla, karakter, a, b, nyeres):
    for e in range(len(tabla)):
        if e % b == 0:
            #ellenőrzés átlósan \ (lefelé)
            if tabla[e] == karakter:
                db = 1
            else:
                continue 
            for t in range(b+1, (nyeres+1)*b, b+1):
                if not (e + t) >= a*b:
                    if tabla[e + t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break 

            if db >= nyeres:
                return True

        if tabla[e] == karakter:            
            #ellenőrzés átlósan \ (balra haldva felfelé)
            
            db = 1
            for t in range(b+1, (nyeres+1)*b, b+1):
                if not (e - t) < 0:
                    if tabla[e - t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break

            #ellenőrzés átlósan \ (jobbra haladva lefelé)

            for t in range(b+1, (nyeres+1)*b, b+1):
                if not (e + t) >= a*b:
                    if tabla[e + t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break

            if db >= nyeres: 
                return True 

            #ellenőrzés átlósan / (balra haladva lefelé)

            db = 1
            for t in range(b-1, (nyeres+1)*b, b-1):
                if not (e + t) >= (a*b)-1:
                    if tabla[e + t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break

            #ellenőrzés átlósan / (balra haladva felfelé)  #3-as esetén nem jó, alszom rá!
            for t in range(b-1, (nyeres+1)*b, b-1):
                if not (e - t) < 0:
                    if tabla[e - t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break

            if db >= nyeres: 
                return True 

            db = 1
            #vízszintes ellenőrzés:
            for t in range(1, nyeres+1):  #balra
                if not (e - t) < 0:
                    if tabla[e-t] == karakter and not (e-t+1) %  b == 0:
                        db += 1
                    else:
                        break
                else:
                    break
            for t in range(1, nyeres+1):   #jobbra
                if not (e + t) >= a*b:
                    if tabla[e+t] == karakter and not (e+t) %  b == 0:
                        db += 1
                    else:
                        break
                else:
                    break
            if db >= nyeres:
                return True

            #ellenőrzés függőleges:
            db = 1
            for t in range(b, (nyeres+1)*b, b):
                if not (e - t) < 0:
                    if tabla[e - t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break
            for t in range(b, (nyeres+1)*b, b):
                if not (e + t) >= a*b:
                    if tabla[e + t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break

            if db >= nyeres: 
                return True
                       
def jatek(jatekos, szamitogep):
    os.system("cls")
    a = int(input("Hányas legyen? (pl. 5) "))
    b = a
    while a < 2:
        print("Legalább 3x3-asnak kell lennie!")
        a = int(input("Hányas legyen? (pl. 5) "))
    if a == 3:
        nyeres = 3
    elif a == 4:
        nyeres = 4
    else:
        nyeres = 5
    ujra = True
    while ujra:
        tele = 0
        tabla = []
        for e in range(1, a*b+1):
            tabla.append(e)
        while tele < (a*b):
            os.system("cls")
            tablakeszites(a, b, tabla)
            
            if not (nyert(tabla, "O", a, b, nyeres) and not tele >= (a*b)):  #JAVÍTANI!!!!!!!!!!!!!!!!!!!  O -->  X
                jatekoslepes(a, b, tabla)
                os.system("cls")
                tablakeszites(a, b, tabla)
                tele += 1

            else:
                os.system("cls")
                tablakeszites(a, b, tabla)
                szamitogep += 1
                print("Az állás {0}-{1}".format(jatekos, szamitogep))
                print("Az O jelű nyert! Egy visszavágó? 1 = igen, 0 = Nem")
                ujra = int(input())
                if ujra == 1:
                    jatek(jatekos, szamitogep)
                else:
                    mentes(jatekos, szamitogep)

            if not (nyert(tabla, "X", a, b, nyeres)) and not tele >= (a*b):
                #jatekoslepes(a, b, tabla)
                geplepes(tabla, a, b, nyeres, tele)
                os.system("cls")
                tablakeszites(a, b, tabla)
                tele += 1

            else:
                os.system("cls")
                tablakeszites(a, b, tabla)
                jatekos += 1
                print("Az állás {0}-{1}".format(jatekos, szamitogep))
                print("Az X jelű nyert! Egy visszavágó? 1 = igen, 0 = Nem")
                ujra = int(input())
                if ujra == 1:
                    jatek(jatekos, szamitogep)
                else:
                    mentes(jatekos, szamitogep)
        os.system("cls")
        tablakeszites(a, b, tabla)
        print("Döntetlen! Visszavágó? 1 = igen, 0 = Nem")
        ujra = int(input())
        if ujra == 1:
            jatek(jatekos, szamitogep)
        else:
            mentes(jatekos, szamitogep)
         
    os.system("cls")

def main():
    os.system("cls")
    print("1. Új játék",
      "2. Előző játék betöltése, és játék",
      "9. Kilepes",
      sep="\n")

    allas = []
    i = int(input())
    while i != 9:
        if i == 2:
            allas = betoltes()
            jatekos = int(allas[0])
            szamitogep = int(allas[1])
            jatek(jatekos, szamitogep)
        elif i == 1:
            jatek(0, 0)
        i = int(input())

main()
