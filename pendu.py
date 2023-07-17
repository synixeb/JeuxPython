import random

ListeMots = ["voiture", "ordinateur", "python", "programmation", "pendu", "boucle", "variable", "fonction", "liste"]

mot = random.choice(ListeMots)
ListeLettre = []
LettresUtilisees = []

def error(nb):
    print ("")
    print ("")
    if nb == 1:
        print ("____")
    elif nb == 2:
        print (" |")
        print (" |")
        print (" |")
        print (" |")
        print ("____")
    elif nb == 3:
        print (" |/")
        print (" |")
        print (" |")
        print (" |")
        print ("____")
    elif nb == 4:
        print ("  ________")
        print (" |/")
        print (" |")
        print (" |")
        print (" |")
        print ("____")
    elif nb == 5:
        print ("  ________")
        print (" |/     |")
        print (" |")
        print (" |")
        print (" |")
        print ("____")
    elif nb == 6:
        print ("  ________")
        print (" |/     |")
        print (" |      O")
        print (" |     -|-")
        print (" |     / \\")
        print ("____")


def str_to_list(mot):
    liste = []
    for i in range (0, len(mot)):
        liste.append(mot[i])
    return liste
ListeLettre = str_to_list(mot)

def list_to_str(liste):
    mot = ""
    for i in range (0, len(liste)):
        mot = mot + liste[i]
    return mot

def afficher_lettre(lettre, ListeLettre, LettresTrouvees):
    for i in range (0, len(ListeLettre)):
        if lettre == ListeLettre[i]:
            LettresTrouvees[i] = lettre
        elif ListeLettre[i] != "_":
            pass
        else:
            LettresTrouvees[i] = "_"
    return LettresTrouvees

def jeux():
    erreur = 0
    LettresTrouvees = []

    print(LettresTrouvees)
    for i in range (0, len(mot)):
        LettresTrouvees.append("_")

    print ("jeux du pendu")
    print (mot)
    
    while erreur < 6:
        print ("")
        print("Lettres utilisées :", LettresUtilisees)
        lettre = input("entrez une lettre : ")
        if len(lettre) > 1:
            print ("c'est un mot")
            if lettre == mot:
                print ("vous avez gagné")
                exit()
        else:
            if lettre in mot:
                print ("la lettre est dans le mot")
                LettresTrouvees = afficher_lettre(lettre, ListeLettre, LettresTrouvees)
                print (LettresTrouvees)
            else:
                LettresUtilisees.append(lettre)
                print ("la lettre n'est pas dans le mot")
                erreur = erreur + 1
                print ("il vous reste", 6 - erreur, "erreur(s)")
                error(erreur)
    
jeux()