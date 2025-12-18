from poudelardd.utilis.input_utils import *


def initialiser_personnage(nom,prenom,attributs):
  joueur = {"Nom":nom,
            "Prenom": prenom,
            "Argent":100 ,
            "Inventaire": [],
            "Sortilèges": [],
            "Attributs": attributs}
  return joueur

def afficher_personnage(joueur):
    for cle in joueur.keys():
        print(cle,joueur[cle])

def modifier_argent(joueur, montant):
  joueur["Argent"] = joueur["Argent"] + montant
  return joueur


def ajouter_objet(joueur,cle, objet):
  joueur[cle].append(objet)




