import random
import os
import time

suppr = False

def RussianRoulette():
    x = random.randint(1, 6)
    if x == 1:
        print("tu es mort")
        Perdu()
    else:
        print("tu as eu de la chance")

def Perdu():
    if suppr == False:
        print("tu es mort")
    else:
        file = 'teslaDeath.jpg'
        location = 'C:/Users/Evan/Pictures/image'
        path = os.path.join(location, file)

        print(path)
        os.remove(path)
        print("tu es mort")

def jeux():
    print("on va jouer a la roulette russe")
    rep = input("tu veux jouer ? (oui/non) : ")
    if rep == "oui":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        RussianRoulette()

    elif rep == "non":
        print("Trouillard je vais le faire pour toi")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        Perdu()
        print("voila c'est fait")

    else:
        print("je n'ai pas compris")
