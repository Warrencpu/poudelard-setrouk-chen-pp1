from poudelardd.chapitres.chapitre_1 import lancer_chapitre1
from poudelardd.utilis.input_utils import demander_choix


def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 - L'Arrivée dans le monde magique.")
    print("2. Lancer le Chapitre 2 - Le voyage vers Poudlard.")
    print("3. Lancer le Chapitre 3 - Les cours et la decouverte de Poudlard.")
    print("4. Quitter le jeu")

def lancer_choix_menu():
    maisons = {"Gryphondor" : 0,
               "Serpentard": 0,
               "Serdaigle": 0,
               "Poufsoufle": O}
    choix_valide = False
    while choix_valide ==False:
        choix = demander_choix(afficher_menu_principal(),["1","2","3","4"])
        if choix == "1":
            choix_valide = True
            personnage = lancer_chapitre1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage)
        elif choix == "2":
            print("Aurevoir")
            choix_valide = True
        else:
            print("Vous ne pouvez pas commencer par ce chapitre")


