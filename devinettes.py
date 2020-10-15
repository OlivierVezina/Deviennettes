#!/usr/bin/env python3

"""
    Jeu de devinette

    par: Olivier Vezina
"""
from random import randrange

nbEssai = 0
nbParties = 1
MAX_ESSAIS = 10
WIN = "GGG"
LOST = "PPP"


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
    liste = []
    cpt = 1
    global nbEssai
    while True:
        if cpt <= MAX_ESSAIS:
            nbEssai += 1
            saisie = input(f"Essaie {cpt}: ")
            if saisie == LOST:
                print(f"Désolé, vous avez échoué après {cpt} tentatives")
                print(f"Le nombre choisi était: {nbRandom}")
                recommencer()
            elif saisie == WIN:
                liste.append("GGG")
                print("Bravo, vous avez deviné le nombre")
                print(f"Votre séquence gagnante est : {liste} ")
                recommencer()
            else:
                if saisie.lstrip('-+').isdigit():
                    guess = int(saisie)
                    liste.append(guess)
                    if guess == nbRandom:
                        print("Bravo, vous avez deviné le nombre")
                        print(f"Votre séquence gagnante est : {liste} ")
                        recommencer()
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
            recommencer()


def recommencer():
    """
        Methode qui demande a l'utilisateur veut recommencer une partie
    """
    global nbParties
    while True:
        choix = input(f"Voulez-vous rejouer? [O/N] ")
        if choix.upper() == "O" or choix == "oui":
            nbParties += 1
            print()
            print()
            devinette()
        elif choix.upper() == "N" or choix == "non":
            moyenne = nbEssai / nbParties
            print("Au revoir")
            print(f"Nombre de parties jouées: {nbParties}")
            print(f"Nombre d'essais était: {nbEssai}")
            print(f"Moyenne d'essais par partie: {moyenne} ")
            exit()
        else:
            print("Choix invalide")
            continue


if __name__ == '__main__':
    main()
