import random

def error(nb,mot):
    print ("")
    print ("")
    if nb == 1:
        print ("")
        print ("")
        print ("")
        print ("")
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
        print ("")
        print ("vous avez perdu")
        print ("le mot était", mot)
        print ("")

def str_to_list(mot):
    liste = []
    for i in range (0, len(mot)):
        liste.append(mot[i])
    return liste

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
    ListeMots = ["cage", "noir", "fraise", "voiture", "baleine", "pomme", "chien", "souris", "cheuveux", "pantalon", "chemise", "chaussure", "pied", "main", "bras", "tête", "oeil", "nez", "bouche", "oreille", "doigt", "jambe", "genou", "coude", "épaule", "poignet", "poing", "ventre", "dos", "cou", "fesse", "cuisse", "talon", "orteil", "pouce", "annulaire", "majeur", "index", "auriculation", "pouce", "poumon", "coeur", "foie", "rein", "estomac", "intestin", "cerf", "biche", "renard", "loup", "ours", "tigre", "lion", "girafe", "zèbre", "singe", "chimpanzé", "gorille", "éléphant", "rhinocéros", "hippopotame", "crocodile", "serpent", "tortue", "lac", "jaune", "mort", "vivant", "port", "porc", "vache", "poule", "coq", "poussin", "pigeon", "mouette", "canard", "oie", "chèvre", "organe", "matraque", "pistolet", "fusil", "mitraillette", "grenade", "bombe", "missile", "avion", "hélicoptère", "char", "tank", "sous-marin", "bateau", "navire", "voilier", "oiseau", "Balle", "forge", "ile", "plage", "mer", "trace", "piste", "poussière", "sable", "pierre", "roche", "montagne", "colline", "plaine", "forêt", "arbre", "fleur", "herbe", "champ", "champignon", "nuage", "ciel", "étoile", "soleil", "lune", "planète", "univers", "galaxie", "système solaire", "étoile filante"]
    ListeLettre = []
    mot = ListeMots[random.randint(0, len(ListeMots) - 1)]

    LettresUtilisees = []
    MotsEssaye = []
    erreur = 0
    LettresTrouvees = []
    
    for i in range (0, len(mot)):
        LettresTrouvees.append("_")
    ListeLettre = str_to_list(mot)
    print ("jeux du pendu")

    print(LettresTrouvees)
    
    while erreur < 6:
        print ("")
        print("Lettres utilisées :", LettresUtilisees)
        print("Mots essayés :", MotsEssaye)
        lettre = input("entrez une lettre ou un mot(pour donner un reponse) : ")
        if len(lettre) > 1:
            print ("c'est un mot")
            if lettre == mot:
                print ("vous avez gagné")
                break
            else:
                MotsEssaye.append(lettre)
                print ("ce n'est pas dans le bon mot")
                erreur = erreur + 1
                print ("il vous reste", 6 - erreur, "erreur(s)")
                print ("")
                print (LettresTrouvees)
                print ("")
                error(erreur)
        else:
            if lettre in mot:
                print ("la lettre est dans le mot")
                LettresTrouvees = afficher_lettre(lettre, ListeLettre, LettresTrouvees)
                print ("")
                print (LettresTrouvees)
                print ("")
            else:
                LettresUtilisees.append(lettre)
                print ("la lettre n'est pas dans le mot")
                erreur = erreur + 1
                print ("il vous reste", 6 - erreur, "erreur(s)")
                print ("")
                print (LettresTrouvees)
                print ("")
                error(erreur, mot)
    