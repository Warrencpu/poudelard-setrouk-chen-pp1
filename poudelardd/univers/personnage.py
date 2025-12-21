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
        if cle == "Inventaire" or cle == "Sortilèges":
            print(cle ," :")
            for i in joueur[cle]:
                print(i , end =" ")
        elif cle == "Attributs" :
            print(cle," :")
            for key in joueur["Attributs"].keys() :
                print("- ",key," :" ,joueur["Attributs"][key])
        else:
            print(cle," :",joueur[cle])


def modifier_argent(joueur, montant):
  joueur["Argent"] = joueur["Argent"] + montant
  return joueur


def ajouter_objet(joueur,cle, objet):
  joueur[cle].append(objet)




