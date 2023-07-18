# Authors: Evan <>
def choix(rep):
    if rep == 0:
        print("Quitter")
        exit()
    elif rep == 1:
        print("Memoire")
        import Memoire 
        Memoire.jeux()
    elif rep == 2:
        print("Motus")
        import motus 
        motus.jeux()
    elif rep == 3:
        print("MemoireNum")
        import MemoireNum
        MemoireNum.jeux()
    elif rep == 4:
        print("ExerciseCalcul")
        import ExerciseCalcul
        ExerciseCalcul.jeux()
    elif rep == 5:
        print("RussianRoulette")
        import RussianRoulette
        RussianRoulette.jeux()
    elif rep == 6:
        print("Pendu")
        import pendu
        pendu.jeux()
    else:
        print("Erreur, veuillez entrer un nombre entre 0 et 6")
        jeux()

def jeux():
    print("Bienvenue dans le programme de choix du jeux")
    while True:
        if input("Voulez-vous jouer ? (o pour oui) : ") == "o":
            print("Bienvenue dans le programme de choix du jeux")
            print("Voici la liste des jeux : ")
            print("0 : Quitter")
            print("1 : Memoire")
            print("2 : Motus")
            print("3 : MemoireNum")
            print("4 : ExerciseCalcul")
            print("5 : RussianRoulette")
            print("6 : Pendu")
            rep = int(input("Quel jeux voulez-vous jouer ? : "))
            if rep >= 0 and rep < 7:
                choix(rep)
            else:
                print("Erreur, veuillez entrer un nombre entre 1 et 6")
                jeux()
        else:
            print("Numero de jeux non disponible")

