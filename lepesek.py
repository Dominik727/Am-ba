import os
import random
import jatek
import pyconio

def jatekoslepes(a, b, tabla, karakter):
    megy = True
    while megy:
        lepes = input("Kérem adja meg azt a pozíciót ahová kíván tenni {0}-t (1-{1}): ".format(karakter, a*b))
        try:
            lepes = int(lepes)
            if (lepes > 0) and (lepes < a*b+1):
                if ures(tabla, lepes):
                    megy = False
                    karakterir (tabla, karakter, lepes)
                else:
                    print("Sajnálom a mező már foglalt!")
            else:
                print("Kérem 1 és {0} közötti egész számot adjon meg!".format(a*b))
        except:
            print("Kérem számot adjon meg!")

def karakterir(tabla, karakter, poz):
    tabla[poz-1] = karakter

def ures(tabla, lepes):
    if tabla[lepes-1] == "X" or tabla[lepes-1] == "O":
        return False
    else:
        return True

def geplepes(tabla, a, b, c, tele):
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
                    lista.append(e+2)
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
        if lista == []:
            lepes = (a*b) // 2
            lista.append(lepes)
            lista.append(lepes+2)
            lista.append(lepes-1)
            lista.append(lepes-b+1)
            lista.append(lepes+b+1)
        r = random.randrange(len(lista))
        lepes = lista[r]
        return karakterir(tabla, "O", lepes)

    for e in range (len(tabla)): #nyer O esete
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "O"
            if jatek.nyert(tablamasolat, "O", a, b, c):
                return karakterir(tabla, "O", e+1)
            else:
                tablamasolat = tabla.copy()

    for e in range (len(tabla)): #Nyer X esete
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "X"
            if jatek.nyert(tablamasolat, "X", a, b, c):
                return karakterir(tabla, "O", e+1)
            else:
                tablamasolat = tabla.copy()

    for e in range (len(tabla)): #ez itt rossz
        if ures(tablamasolat, e+1):
            tablamasolat[e] = "X"
            if jatek.nyert(tablamasolat, "X", a, b, c-1):
                return karakterir(tabla, "O", e+1)
            else:
                tablamasolat = tabla.copy()    

    lista = jatek.nyertgep(tabla, "O", a, b, c)
    r = random.randrange(len(lista))
    lepes = lista[r]
    return karakterir(tabla, "O", lepes)

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

