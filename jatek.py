import pyconio
import os
import lepesek
import NHF

def jatek(jatekos, szamitogep, kezdes):
    os.system("cls")
    igaz = True
    while igaz:
        a = input("Hányas legyen? (pl. 5x5 esetén: 5) ")
        try:
            a = int(a)
            if a >= 5 and a <= 25:
                nyeres = 5
                break
            elif a == 3:
                nyeres = 3
                break
            elif a == 4:
                nyeres = 4
                break
            elif a <= 2:
                print("legalább 3x3-asnak kell lennie!")
            else:
                os.system("cls")
                print("legfeljebb 25x25-ös lehet!")
        except:
            os.system("cls")
            print("Kérem számot írjon be!")
    b = a
    ujra = True
    nyer = 0
    while ujra:
        tele = 0
        tabla = []
        for e in range(1, a*b+1):
            tabla.append(e)
        while tele < (a*b):
            os.system("cls")
            lepesek.tablakeszites(a, b, tabla)
            
            if not (nyert(tabla, "O", a, b, nyeres)):
                if kezdes == 1:
                    lepesek.geplepes(tabla, a, b, nyeres, tele)
                else:
                    lepesek.jatekoslepes(a, b, tabla, "X")
                os.system("cls")
                lepesek.tablakeszites(a, b, tabla)
                tele += 1
            else:
                os.system("cls")
                lepesek.tablakeszites(a, b, tabla)
                szamitogep += 1
                print("Az állás {0}-{1}".format(jatekos, szamitogep))
                print("Az O jelű nyert!")
                igaz = True
                while igaz:
                    ujra = input("Egy visszavágó? 1 = igen, 0 = Nem\n")
                    try:
                        ujra = int(ujra)
                        if ujra == 1:
                            jatek(jatekos, szamitogep, kezdes)
                            igaz = False
                        elif ujra == 0:
                            NHF.mentes(jatekos, szamitogep)
                            tele = a*b
                            ujra = False
                            nyer = 1
                            igaz = False
                        else:
                            os.system("cls")
                            print("Kérem 1-et vagy 0-t írjon be!")
                    except:
                        os.system("cls")
                        print("Kérem számot írjon be!")

            if tele >= (a*b):
                break

            if not (nyert(tabla, "X", a, b, nyeres)):
                if kezdes == 1:
                    lepesek.jatekoslepes(a, b, tabla, "X")
                elif kezdes == 2:
                    lepesek.jatekoslepes(a, b, tabla, "O")
                else:
                    lepesek.geplepes(tabla, a, b, nyeres, tele)
                os.system("cls")
                lepesek.tablakeszites(a, b, tabla)
                tele += 1

            else:
                os.system("cls")
                lepesek.tablakeszites(a, b, tabla)
                jatekos += 1
                print("Az állás {0}-{1}".format(jatekos, szamitogep))
                print("Az X jelű nyert!")
                igaz = True
                while igaz:
                    ujra = input("Egy visszavágó? 1 = igen, 0 = Nem\n")
                    try:
                        ujra = int(ujra)
                        if ujra == 1:
                            jatek(jatekos, szamitogep, kezdes)
                            igaz = False
                        elif ujra == 0:
                            NHF.mentes(jatekos, szamitogep)
                            tele = a*b
                            ujra = False
                            nyer = 1
                            igaz = False
                        else:
                            os.system("cls")
                            print("Kérem 1-et vagy 0-t írjon be!")
                    except:
                        os.system("cls")
                        print("Kérem számot írjon be!")

        if not nyer == 1:
            os.system("cls")
            lepesek.tablakeszites(a, b, tabla)
            print("Az állás {0}-{1}".format(jatekos, szamitogep))
            print("Döntetlen!")
            igaz = True
            while igaz:
                ujra = input("Egy visszavágó? 1 = igen, 0 = Nem\n")
                try:
                    ujra = int(ujra)
                    if ujra == 1:
                        jatek(jatekos, szamitogep, kezdes)
                        igaz = False
                    elif ujra == 0:
                        NHF.mentes(jatekos, szamitogep)
                        tele = a*b
                        ujra = False
                        nyer = 1
                        igaz = False
                    else:
                        os.system("cls")
                        print("Kérem 1-et vagy 0-t írjon be!")
                except:
                    os.system("cls")
                    print("Kérem számot írjon be!")
         
    os.system("cls")

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
                if nyeres == 3 and e == 2:
                    break
                if not (e - t) < 0:
                    if tabla[e - t] == karakter:
                        db += 1
                        if (e-t) % b == 0:
                            break
                    else:
                        break
                else:
                    break

            #ellenőrzés átlósan \ (jobbra haladva lefelé)

            for t in range(b+1, (nyeres+1)*b, b+1):
                if not (e + t) >= a*b:
                    if tabla[e + t] == karakter:
                        db += 1
                        if (e+t+1) % b == 0:
                            break
                    else:
                        break
                else:
                    break

            if db >= nyeres: 
                return True 

            #ellenőrzés átlósan / (balra haladva lefelé)

            db = 1
            for t in range(b-1, (nyeres+1)*b, b-1):
                if nyeres == 3 and e == 6:
                    break
                if not (e + t) >= (a*b)-1:
                    if tabla[e + t] == karakter:
                        db += 1
                    else:
                        break
                else:
                    break

            #ellenőrzés átlósan / (balra haladva felfelé)
            for t in range(b-1, (nyeres+1)*b, b-1):
                if nyeres == 3 and e == 8:
                    break
                if not (e - t) <= 0:
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

def nyertgep(tabla, karakter, a, b, c):
    g = None
    h = None
    lepes = []
    for e in range (len(tabla)):
        if e % b == 0:
            #ellenőrzés átlósan \ (lefelé)
            if tabla[e] == karakter:
                db = 1
            else:
                continue 
            for t in range(b+1, (c+1)*b, b+1):
                if not (e + t) >= a*b:
                    if lepesek.ures(tabla, e+t+1) or tabla[e + t] == karakter:
                        db += 1
                        if t == b+1 and lepesek.ures(tabla, e+t+1):
                            g = t+1
                    else:
                        break
                else:
                    break

            if db >= c:
                if not g == None:
                    lepes.append(g)

        #vízszintes
        if tabla[e] == karakter:
            db = 1
            for t in range(1, c):   #jobbra
                if not (e + t) >= a*b:
                    if (lepesek.ures(tabla, e+t+1) or tabla[e+t] == karakter) and (not (e+t) %  b == 0):
                        db += 1
                        if t == 1 and lepesek.ures(tabla, e+t+1):
                            g = e+t+1
                    else:
                        break
                else:
                    break
            for t in range(1, c):  #balra
                if not (e - t) < 0:
                    if (lepesek.ures(tabla, e-t+1) or tabla[e-t] == karakter) and (not (e-t+1) %  b == 0):
                        db += 1
                        if t == 1 and lepesek.ures(tabla, e-t+1):
                            h = e-t+1
                    else:
                        break
                else:
                    break
            if db >= c:
                if not g == None:
                    lepes.append(g)
                if not h == None:    
                    lepes.append(h)
                
            #függőleges
            db = 1
            for t in range(b, c*b, b):   #lefele
                if not (e + t) >= a*b:
                    if (lepesek.ures(tabla, e+t+1) or tabla[e+t] == karakter) and (not (e+t) %  b == 0):
                        db += 1
                        if t == b and lepesek.ures(tabla, e+t+1):
                            g = e+t+1
                    else:
                        break
                else:
                    break
            for t in range(b, c*b, b):  #felfele
                if not (e - t) < 0:
                    if (lepesek.ures(tabla, e-t+1) or tabla[e-t] == karakter) and (not (e-t+1) %  b == 0):
                        db += 1
                        if t == b and lepesek.ures(tabla, e-t+1):
                            h = e-t+1
                    else:
                        break
                else:
                    break
            if db >= c:
                if not g == None:
                    lepes.append(g)
                if not h == None:    
                    lepes.append(h)

            #ellenőrzés átlósan \ (balra haldva felfelé)
            
            db = 1
            for t in range(b+1, (c+1)*b, b+1):
                if c == 3 and e == 2:
                    break
                if not (e - t) < 0:
                    if lepesek.ures(tabla, e-t+1) or tabla[e - t] == karakter:
                        db += 1
                        if t == b+1 and lepesek.ures(tabla, e-t+1):
                            g = e-t+1
                        if (e-t) % b == 0:
                            break
                    else:
                        break
                else:
                    break

            #ellenőrzés átlósan \ (jobbra haladva lefelé)

            for t in range(b+1, (c+1)*b, b+1):
                if not (e + t) >= a*b:
                    if lepesek.ures(tabla, e+t+1) or tabla[e + t] == karakter:
                        db += 1
                        if t == b+1 and lepesek.ures(tabla, e+t+1):
                            h = e+t+1
                        if (e+t+1) % b == 0:
                            break
                    else:
                        break
                else:
                    break

            if db >= c: 
                if not g == None:
                    lepes.append(g)
                if not h == None:    
                    lepes.append(h)

            #ellenőrzés átlósan / (balra haladva lefelé)  ---------------> ez itt rossz
            db = 1
            for t in range(b-1, (c+1)*b, b-1):
                if c == 3 and e == 6:
                    break
                if not (e + t) >= (a*b)-1:
                    if lepesek.ures(tabla, e+t+1) or tabla[e + t] == karakter:
                        db += 1
                        if t == b-1 and lepesek.ures(tabla, e+t+1):
                            g = e+t+1
                        if (e+t) % b == 0:
                            break
                    else:
                        break
                else:
                    break

            #ellenőrzés átlósan / (balra haladva felfelé)
            for t in range(b-1, (c+1)*b, b-1):
                if c == 3 and e == 8:
                    break
                if not (e - t) <= 0:
                    if lepesek.ures(tabla, e-t+1) or tabla[e - t] == karakter:
                        db += 1
                        if t == b-1 and lepesek.ures(tabla, e-t+1):
                            h = e-t+1
                        if (e-t+1) % b == 0:
                            break
                    else:
                        break
                else:
                    break

            if db >= c: 
                if not g == None:
                    lepes.append(g)
                if not h == None:    
                    lepes.append(h)
    return lepes

def main():
    pyconio.settitle('Amőba V 1.0')
    kezdes = 0
    print("1. Új játék",
      "2. Előző játék betöltése és játék",
      "3. Beállítások",
      "9. Kilépés",
      sep="\n")

    allas = []
    i = NHF.bekeres()
    while i != 9:
        if i == 2:
            try:
                allas = NHF.betoltes()
                jatekos = int(allas[0])
                szamitogep = int(allas[1])
                jatek(jatekos, szamitogep, kezdes)
            except:
                os.system("cls")
                print("Nincs mentett állás!")
                main()
        elif i == 1:
            jatek(0, 0, kezdes)
        elif i == 3:
            os.system("cls")
            kezdes = NHF.elkezdes()
            os.system("cls")
        else:
            print("Kérem a megadott számok közül válasszon!")
        print("1. Új játék",
            "2. Előző játék betöltése és játék",
            "3. Beállítások",
            "9. Kilepes",
            sep="\n")
        i = NHF.bekeres()

main()
