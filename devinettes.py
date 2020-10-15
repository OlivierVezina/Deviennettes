#!/usr/bin/env python3

"""
    Jeu de devinette

    par: Olivier Vezina
"""
from random import randrange

def main():
    """

    Fonction principale
    """
    print("Bonjour, je m'appelle Pedro CallMe")
    print("J'ai choisi un nombre entier entr 1 et 100")
    print("Pouvez-vous le deviner?")
    devinette()


def devinette():
    """
        Fonction pour deviner le nombre
    """
    nbRandom = randrange(1, 101)
    cpt = 0
    while True:
        cpt = cpt + 1
        guess = int(input(f"Essaie {cpt}:"))
        if guess == nbRandom:
            print("Bravo, vous avez deviné le nombre")
            break
        elif guess < nbRandom:
            print("Votre nombre est trop petit...")
            continue
        else:
            print("Votre nombre est trop grand...")
            continue


if __name__ == '__main__':
    main()
