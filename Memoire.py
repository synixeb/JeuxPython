import random
#Liste des mots deja generes
ListeMots = []

#Chances d'avoir un nouveau mot (Exemple : 3 = 30%) 10 = 100% si superieur a 10 la chance est aleatoire
chanceNouveauMot = 3
if chanceNouveauMot > 10:
    chanceNouveauMot = random.randint(1, 10)

#Longueur des mots (Exemple : 5 = xxxxx)
longueurMot = 5

def genererMots():
    mot = []
    mot = ajoutConsonne(mot)
    for i in range(0, longueurMot - 1):
        if random.randint(1, 4) == 1:
            mot = ajoutConsonne(mot)
        else:
            mot = ajoutVoyelle(mot)
    ListeMots.append(mot)
    return mot

def ajoutConsonne(mot):
    consonne = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n","p", "q", "r", "s", "t", "v", "w", "x", "z"]
    mot.append(consonne[random.randint(0, len(consonne) - 1)])
    return mot

def ajoutVoyelle(mot):
    voyelle = ["a", "e", "i", "o", "u", "y"]
    mot.append(voyelle[random.randint(0, len(voyelle) - 1)])
    return mot

def ConvertListetoString(mot):
    Mot = "".join(mot)
    return Mot

def ancienMot():
    mot = ListeMots[random.randint(0, len(ListeMots) - 1)]
    return mot

def jeux():
    y = 0
    erreur = 0

    while erreur == 0:
        if random.randint(1, 10) <= chanceNouveauMot:
            mot = ancienMot()
            mot = ConvertListetoString(mot)
            print(mot)
            rep = input("Ce mot est-il nouveau ? (o/n) : ")
            if rep == "o":
                print ("C'est faux")
                erreur = 1
            elif rep == "n":
                print ("Bravo tu as reussi")
                for i in range(0, 50):
                    print("")
                y += 1
            else:
                print("Erreur, veuillez entrer o ou n")
        else:
            mot = genererMots()
            mot = ConvertListetoString(mot)
            print(mot)
            rep = input("Ce mot est-il nouveau ? (o/n) : ")
            if rep == "o":
                print ("Bravo tu as reussi")
                for i in range(0, 50):
                    print("")
                y += 1
            elif rep == "n":
                print ("C'est faux")
                erreur = 1
            else:
                print("Erreur, veuillez entrer o ou n")

    print("Tu as reussi a retenir ", y, " mots")

jeux()