from poudelardd.chapitres.chapitre_3 import apprendre_sorts
from poudelardd.univers.personnage import initialiser_personnage
from poudelardd.utilis.input_utils import  demander_choix
import random


def initialiser_voldemor():
    attributs = {"Courage": 0,
           "Intelligence": 2,
           "Loyauté": 0,
           "Ambition": 1000000}
    voldemor = initialiser_personnage("Lord","Voldemor", attributs)
    sorts = [{
        "nom": "Lumos Solem",
        "description": "Produit une lumière très puissante simulant celle du soleil.",
        "type": "Utilitaire"
    },
    {
        "nom": "Aparecium",
        "description": "Rend visible l'encre invisible.",
        "type": "Utilitaire"
    },
    {
        "nom": "Obliviate",
        "description": "Efface des souvenirs spécifiques de la mémoire d'une personne.",
        "type": "Utilitaire"
    },{
        "nom": "Expelliarmus",
        "description": "Désarme un adversaire.",
        "type": "Défensif"
    },{
        "nom": "Avada Kedavra",
        "description": "Provoque la mort instantanée de la cible.",
        "type": "Offensif"
    }]
    voldemor["Sortilèges"] = sorts

"""def calcul_probabilité(sort_joueur,sort_ennemi):
    Sort_caracteristiques = {"Utilitaire" : [0,1,-1],"Offensif" : [-1, 0 , 1], "Defensif" : [1, -1 , 0]}
    for i in range(len(sort_joueur)):"""


def manche(joueur1, joueur2):
    Sort_caracteristiques = {"Utilitaire": [ 0, 1, -1],
                             "Offensif": [ -1, 0, 1],
                             "Défensif": [ 1, -1, 0]}
    attaque = demander_choix("quel sort souhaitez vous lancer",joueur["Sortilèges"])
    sort_ennemi = random.choice(joueur2["Sortilèges"])
    input("Voldemort a utilisé {}".format(sort_ennemi))
    if sort_ennemi["type"]== "Utilitaire":
        puissance = Sort_caracteristiques[joueur["Sortilèges"][attaque-1]["type"]][0]
    elif sort_ennemi["type"]== "Offensif":
        puissance = Sort_caracteristiques[joueur["Sortilèges"][attaque-1]["type"]][1]
    elif sort_ennemi["type"]== "Défensif":
        puissance = Sort_caracteristiques[joueur["Sortilèges"][attaque-1]["type"]][2]
    print(puissance)
    if puissance == 0:
        print("ex-aequo")
    elif puissance == 1:
        print("Vous gagné cette manche")
    elif puissance == -1 :
        print("Vous avez perdu cette manche")


def est_gagnant(puissance):
    if puissance == 1 :
        gagant = True


def lancer_partie():
    #Lance une partie de 3 manche

def lancer_chapitre4(joueur):







attributs = {"Courage": 0,
           "Intelligence": 2,
           "Loyauté": 0,
           "Ambition": 1000000}
joueur = initialiser_personnage("Prout","caca",attributs)
apprendre_sorts(joueur)
voldemor = initialiser_voldemor()
voldemor = initialiser_personnage("Lord","Voldemor", attributs)

voldemor["Sortilèges"] = [{"nom": "Lumos Solem",
        "description": "Produit une lumière très puissante simulant celle du soleil.",
        "type": "Utilitaire"
    },
    {
        "nom": "Aparecium",
        "description": "Rend visible l'encre invisible.",
        "type": "Utilitaire"
    },
    {
        "nom": "Obliviate",
        "description": "Efface des souvenirs spécifiques de la mémoire d'une personne.",
        "type": "Utilitaire"
    },{
        "nom": "Expelliarmus",
        "description": "Désarme un adversaire.",
        "type": "Défensif"
    },{
        "nom": "Avada Kedavra",
        "description": "Provoque la mort instantanée de la cible.",
        "type": "Offensif"
    }]


manche(joueur,voldemor)