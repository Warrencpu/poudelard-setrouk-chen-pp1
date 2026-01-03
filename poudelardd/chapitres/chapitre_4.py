from poudelardd.chapitres.chapitre_3 import apprendre_sorts
from poudelardd.univers.personnage import initialiser_personnage
from poudelardd.utilis.input_utils import demander_choix, load_fichier
import random


def initialiser_voldemor():
    attributs = {"Courage": 0,
           "Intelligence": 2,
           "Loyauté": 0,
           "Ambition": 1000000}
    voldemor = initialiser_personnage("Lord","Voldemor", attributs)
    diff = demander_choix("Quel difficulté choisissez-vous",["Simple","Moyen","Difficile"])
    lst_sorts = load_fichier("../data/sorts.json")
    if diff == 1:
        for i in range (9):
            c = random.randint(0, len(lst_sorts)-1 )
            voldemor["Sortilèges"].append(lst_sorts[c])
    else:
        voldemor["Sortilèges"] = [{
            "nom": "Nox",
            "description": "Éteint la lumière produite par Lumos.",
            "type": "Utilitaire"
        }, {"nom": "Aparecium",
            "description": "Rend visible l'encre invisible.",
            "type": "Utilitaire"
        }, {"nom": "Obliviate",
            "description": "Efface des souvenirs spécifiques de la mémoire d'une personne.",
            "type": "Utilitaire"
        }, {"nom": "Expelliarmus",
            "description": "Désarme un adversaire.",
            "type": "Défensif"
        }, {"nom": "Avada Kedavra",
            "description": "Provoque la mort instantanée de la cible.",
            "type": "Offensif"
        },{"nom": "Petrificus Totalus",
        "description": "Pétrifie complètement la cible.",
        "type": "Offensif"
        },{"nom": "Rennervate",
        "description": "Réanime une personne assommée ou inconsciente.",
        "type": "Défensif"
        } ]

    return voldemor


def manche(joueur1, joueur2):
    Sort_caracteristiques = {"Utilitaire": [ 0, 1, -1],
                             "Offensif": [ -1, 0, 1],
                             "Défensif": [ 1, -1, 0]}
    attaque = demander_choix("quel sort souhaitez vous lancer",joueur1["Sortilèges"])
    input("Vous avez choisi {} ({})".format(joueur1["Sortilèges"][attaque-1]["nom"],joueur1["Sortilèges"][attaque-1]["type"]))
    sort_ennemi = random.choice(joueur2["Sortilèges"])
    input("Voldemort a utilisé {} ({})".format(sort_ennemi["nom"],sort_ennemi["type"]))
    if sort_ennemi["type"]== "Utilitaire":
        puissance = Sort_caracteristiques[joueur1["Sortilèges"][attaque-1]["type"]][0]
    elif sort_ennemi["type"]== "Offensif":
        puissance = Sort_caracteristiques[joueur1["Sortilèges"][attaque-1]["type"]][1]
    elif sort_ennemi["type"]== "Défensif":
        puissance = Sort_caracteristiques[joueur1["Sortilèges"][attaque-1]["type"]][2]
    return puissance, attaque, sort_ennemi



def lancer_partie(joueur1,joueur2):
    input("Vous arrivez au milieu de la cour de l'école et se tien devant vous...")
    input("Lord Voldemort ! :-O")
    input("Vous pouvez le battre d'une seule facon , en lui donnant 3 coups fatales a l'aide de vos sorts !")
    pv_v = pv_j = 2
    fin = False
    while (pv_v > 0 and pv_j !=0) or (pv_v != 0 and pv_j > 0):
        puissance, attaque , sort_ennemi = manche(joueur, voldemort)
        if puissance == 1:
            pv_v = pv_v -1
            input("Votre sort est très efficace")
        elif puissance == -1:
            input("Votre sort est plus faible")
            pv_j = pv_j - 1
        else:
            input("Votre sort n'a aucun effet")
        joueur1["Sortilèges"].pop(attaque-1)
        for j in range (len(joueur2["Sortilèges"])-2):
            if joueur2["Sortilèges"][j] == sort_ennemi:
                joueur2["Sortilèges"].pop(j)
        print("Score _ Voldemort : ",pv_v,"{} : {}".format(joueur1["Prenom"],pv_j))
    if pv_v == 0:
        print("Vous avez gagné")
    else :
        print("Vous avez perdu")

def lancer_chapitre4(joueur):
    Voldemort = initialiser_voldemor()
    lancer_partie(joueur,Voldemort)
    input("Vous avez fini le chapitre 4")


attributs = {"Courage": 0,
           "Intelligence": 2,
           "Loyauté": 0,
           "Ambition": 1000000}
joueur = initialiser_personnage("Prout","caca",attributs)
apprendre_sorts(joueur)

voldemort = initialiser_voldemor()

lancer_partie(joueur,voldemort)