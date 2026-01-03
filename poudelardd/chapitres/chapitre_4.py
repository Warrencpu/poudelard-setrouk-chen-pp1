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
    lst_sorts = load_fichier("./data/sorts.json")
    voldemor["PV"] = 2
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
        if diff == 3:
            voldemor["PV"] = 5

    return voldemor

def Attaques(joueur1,attaque,sort_ennemi):
    Sort_caracteristiques = {"Utilitaire": [["Utilitaire", 0], ["Offensif", 1], ["Défensif", -1]],
                             "Offensif": [["Utilitaire", -1], ["Offensif", 0], ["Défensif", 1]],
                             "Défensif": [["Utilitaire", 1], ["Offensif", -1], ["Défensif", 0]]}
    cpt = 0
    for i in Sort_caracteristiques[joueur1["Sortilèges"][attaque-1]["type"]]:
        if i[0] == sort_ennemi["type"]:
            puissance = Sort_caracteristiques[joueur1["Sortilèges"][attaque - 1]["type"]][cpt][1]
        cpt = cpt+ 1
    return puissance


def probabilités(joueur1, joueur2):
    for i in range (len(joueur1["Sortilèges"])):
        cpt_u = cpt_d = cpt_o = 0
        for j in joueur2["Sortilèges"]:
            if j["type"] == "Utilitaire":
                cpt_u = cpt_u + 1
            elif j["type"] == "Défensif":
                cpt_d = cpt_d + 1
            elif j["type"] == "Offensif":
                cpt_o = cpt_o + 1
        cp_total = cpt_u + cpt_d +cpt_o
        if joueur1["Sortilèges"][i]["type"] == "Utilitaire":
            joueur1["Sortilèges"][i]["Probabilités"] = cpt_o *100 // cp_total
        elif joueur1["Sortilèges"][i]["type"]== "Défensif":
            joueur1["Sortilèges"][i]["Probabilités"] = cpt_u*100 // cp_total
        if joueur1["Sortilèges"][i]["type"]== "Offensif":
            joueur1["Sortilèges"][i]["Probabilités"] = cpt_d*100 //cp_total


def manche(joueur1, joueur2):
    probabilités(joueur1,joueur2)
    tb = []
    for i in range(len(joueur1["Sortilèges"])):
        tb.append("sortilège {} ({}) avce {}% de réussite".format(joueur1["Sortilèges"][i]["nom"],joueur1["Sortilèges"][i]["type"],joueur1["Sortilèges"][i]["Probabilités"]))
    print(tb)
    attaque = demander_choix("quel sort souhaitez vous lancer",tb)
    input("Vous avez choisi {} ({})".format(joueur1["Sortilèges"][attaque-1]["nom"],joueur1["Sortilèges"][attaque-1]["type"]))
    sort_ennemi = random.choice(joueur2["Sortilèges"])
    input("Voldemort a utilisé {} ({})".format(sort_ennemi["nom"],sort_ennemi["type"]))
    puissance = Attaques(joueur1,attaque,sort_ennemi)

    return puissance, attaque, sort_ennemi


def lancer_partie(joueur1,joueur2):
    input("Vous arrivez au milieu de la cour de l'école et se tien devant vous...")
    input("Lord Voldemort ! :-O")
    input("Vous pouvez le battre d'une seule facon , en lui donnant 3 coups fatales a l'aide de vos sorts !")
    pv_j = 2
    pv_v = joueur2["PV"]
    while ((pv_v > 0 and pv_j !=0) or (pv_v != 0 and pv_j > 0)) or (joueur1["Sortilèges"] != [] or joueur2["Sortilèges"] != []) :
        puissance, attaque , sort_ennemi = manche(joueur1, joueur2)
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
    elif pv_j == 0 :
        print("Vous avez perdu")
    else:
        print("Vous et votre adversaire vous étes effondrée de fatigue")

def lancer_chapitre4(joueur):
    Voldemort = initialiser_voldemor()
    lancer_partie(joueur,Voldemort)
    input("Vous avez fini le chapitre 4")


