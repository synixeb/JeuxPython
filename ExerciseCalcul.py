import random

#Valeur maximale des nombres
valeurMax = 100

def calculAleatoire():
    x = random.randint(1, valeurMax)
    y = random.randint(1, valeurMax)
    z = random.randint(1, 4)
    if z == 1:
        print(x, "+", y)
        return x + y
    elif z == 2:
        print(x, "-", y)
        return x - y
    elif z == 3:
        print(x, "*", y)
        return x * y
    elif z == 4:
        print(x, "/", y)
        return x / y
    
def demandeUtilisateur():
    rep = int(input("Quel est le resultat de ce calcul ? : "))
    if isinstance(rep, int):
        return rep
    else:
        print("Erreur, veuillez entrer un nombre")
        demandeUtilisateur()

def comparaison(x, y):
    if x == y:
        return True
    else:
        return False
    
def affichageResultat(x):
    if x == True:
        print("Bravo tu as reussi")
    else:
        print("Dommage tu as perdu")

def calculMental():
    x = calculAleatoire()
    y = demandeUtilisateur()
    z = comparaison(x, y)
    affichageResultat(z)

def jeux():
    while True:
        if input("Voulez-vous faire un calcul mental ? (O/N) : ") == "O":
            calculMental()
        else:
            break

jeux()