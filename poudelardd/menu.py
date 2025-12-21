from poudelardd.chapitres.chapitre_1 import lancer_chapitre1
from poudelardd.chapitres.chapitre_2 import lancer_chapitre_2
from poudelardd.chapitres.chapitre_3 import lancer_chapitre_3
from poudelardd.utilis.input_utils import demander_choix


def afficher_menu_principal():
    lst =[" Lancer le Chapitre 1 - L'Arrivée dans le monde magique."," Lancer le Chapitre 2 - Le voyage vers Poudlard."," Lancer le Chapitre 3 - Les cours et la decouverte de Poudlard."," Quitter le jeu"]
    return lst

def lancer_choix_menu():
    maisons = {"Gryphondor" : 0,
               "Serpentard": 0,
               "Serdaigle": 0,
               "Poufsoufle": 0}
    choix_valide = False
    while choix_valide ==False:
        choix = demander_choix("Bienvenue ! Par quel chapitre souhaitez-vous commencer ? ",afficher_menu_principal())
        if choix == 1:
            personnage = lancer_chapitre1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage)
            choix_valide = True
        elif choix == 4:
            print("Merci d'avoir éssayé notre jeu , aurevoir!")
            choix_valide = True
        else:
            print("Vous ne pouvez pas commencer par ce chapitre")


