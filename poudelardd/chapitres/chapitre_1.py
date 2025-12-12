from poudelardd.univers.personnage import initialiser_personnage
from poudelardd.utilis.input_utils import demander_texte, demander_nombre


def creer_personnage():
    attr = {"courage": 0,
            "intelligence": 0,
            "loyauté" : 0,
            "ambition": 0}
    nom = initialiser_personnage(demander_texte(input("quel est votre nom"))
    prenom =demander_texte(input("quel est votre prenom"))
    print("Choisissez vos attributs")
    attr[courage]=demander_nombre("niveau de courage (1-10) ",1,10)
    attr[intelligence]=demander_nombre("niveau d'intelligence (1-10) ", 1, 10)
    attr[loyauté]=demander_nombre("niveau de loyauté (1-10) ", 1, 10)
    attr[ambition]=demander_nombre("niveau d'ambition (1-10) ", 1, 10)
    perso = initialiser_personnage(nom,prenom,attr)
    return perso
