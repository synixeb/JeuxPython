import random
import time

def genererNombre(longueur):
    nombre = ""
    for i in range(0, longueur):
        nombre += str(random.randint(0, 9))
    print("Le nombre à retenir est ",nombre)
    time.sleep(5)

    for i in range(0, 50):
        print("")
    return nombre

def demanderNombre():
    nombre = str(input("Quel est le nombre ? : "))
    return nombre

def comparaison(nombre1, nombre2):
    if nombre1 == nombre2:
        return True
    else:
        return False

def jeux():
    i=1
    while True:
        if comparaison(genererNombre(i), demanderNombre()) == False:
            print("Dommage tu as perdu")
            break
        else:
            print("Bravo tu as reussi")
            i += 1
    print("Tu as reussi a retenir ", i, " chiffres")
jeux()