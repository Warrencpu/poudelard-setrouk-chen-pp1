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


def actualiser_points_maisons(maisons, nom_maisons, points):
      if nom_maisons in maisons:
          maisons[nom_maisons] =+ points
          print("La maison ", nom_maisons, "a maintenant un total de ", maisons[nom_maisons], 'points !')
      else:
          print("Cette maisons n'existe pas")

def afficher_maison_gagnante(maisons):
    score_max = 0
    for a,b in maisons.items():
        if score_max < maisons[a]:
            score_max = maisons[a]
            maions_gagn = a
    print(maions_gagn)


def repartition_maisons(joueur, questions):
      ptm = {"Gryphondor" : 0,
             "Serpantard" : 0,
             "Serdaigle" : 0 ,
             "Poufsoufle" : 0 }
      ptm['Gryffondor'] = joueur["Attributs"][ "Courage" ]
      ptm['Serdaigle'] = joueur["Attributs"]["Intelligence"]
      ptm['Poufsouffle'] = joueur["Attributs"]["Loyauté"]
      ptm['Serpendtard'] = joueur["Attributs"]["Ambition"]
      for i in range(len(questions)):
          choix = demander_choix(questions[i][0], questions[i][1])
          ptm[questions[i][2][choix]] += 3

      return afficher_maison_gagnante(ptm)


maisons = {
    "Gryffondor": 0,
    "Serpentard": 456,
    "Poufsouffle": 0,
    "Serdaigle": 0
}
questions = [
    (
        "Tu vois un ami en danger. Que fais-tu ?",
        ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de laide", "Je reste calme et jobserve"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Quel trait te décrit le mieux ?",
        ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Face à un défi difficile, tu...",
        ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    )
]

Att = {"Courage" : 0,
       "Ambition" : 0,
       "Loyauté" : 0,
       "Intelligence" : 0}

