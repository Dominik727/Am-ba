import os
import random
import jatek
import pyconio

def mentes(jatekos, szamitogep):
    print("Jó játék volt :)")
    kerdes = input("Szeretnéd elmenteni a játék eredményét? 1 = igen, 0 = Nem \n ")
    try:
        kerdes = int(kerdes)
        if kerdes == 1:
            with open('mentes.txt', 'w') as f:
                jatekos = str(jatekos)
                szamitogep = str(szamitogep)
                f.write(jatekos + "\n")
                f.write(szamitogep)
            os.system("cls")
            jatek.main()
        elif kerdes == 0:
            os.system("cls")
        else:
            os.system("cls")
            print("Kérem 1 vagy 0 értéket írjon be!")
            mentes(jatekos, szamitogep)
    except:
        print("Kérem ne szöveget írjon be!")
        mentes(jatekos, szamitogep)

def betoltes():
    allas = []
    with open('mentes.txt') as f:
        for sor in f:
            sor = sor.rstrip("\n")
            allas.append(sor)
    
    f.close()

    print("Az állás {0}-{1}".format(int(allas[0]), int(allas[1])))
    return allas

def elkezdes():
    print("Ki kezdjen?",
            "1 = Számítógép",
            "2 = Játékos",
            "3 = 2 játékos mód",
            sep="\n")
    a = input()
    try:
        a = int(a)
        if a == 1:
            return 1
        elif a == 2:
            return 0
        elif a == 3:
            return 2
        else:
            os.system("cls")
            print("1 vagy 2 írható be!")
            elkezdes()
    except:
        os.system("cls")
        print("Kérem számot írjon be!")
        elkezdes()

def bekeres():
    i = input()
    try:
        return int(i)
    except:
        os.system("cls")
        print("Kérem számot adjon meg!")
        jatek.main()