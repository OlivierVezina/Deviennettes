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
    cpt = 1
    while True:
        if cpt <= 10:
            saisie = input(f"Essaie {cpt}: ")
            if saisie.lstrip('-+').isdigit():
                guess = int(saisie)
                if guess == nbRandom:
                    print("Bravo, vous avez deviné le nombre")
                    break
                elif guess < nbRandom:
                    print("Votre nombre est trop petit...")
                    cpt = cpt + 1
                    continue
                else:
                    print("Votre nombre est trop grand...")
                    cpt = cpt + 1
                    continue
            else:
                print("Erreur: Entrer un nombre entier svp")
                continue
        else:
            print("Désolé, vous avez échoué après 10 tentatives ")
            print(f"Le nombre choisi était: {nbRandom}")
            break


if __name__ == '__main__':
    main()
