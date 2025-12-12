from input.untils.py import *

def initialiser_personnage(nom,prenom,attributs):
  joueur = {"Nom":nom,
            "Prenom": prenom,
            "Argent":100 ,
            "Inventaire": [],
            "Sortilèges": [],
            "Attributs": attributs}
  return joueur

def afficher_personnage(joueur ):
      for cle in joueur.keys():
          print(cle,joueur[cle])

  def modifier_argent(joueur, montant):
  joueur[Argent] = joueur[Argent] + montant
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
      for i in range(4):
          if score_max < maisons[i]:
              score_max = maisons[i]
      for i in range(4):
          if score_max == maisons[i]:
              print(maisons[i], " est gagnante")

  def repartition_maisons(joueurs, questions):
      pointm = {"Gryphondor" : 0,
                "Serpantard" : 0,
                "Serdaigle" : 0,
                "Poufsoufle" : 0 }
      pointm[Gryphondor] = joueur[atrributs[0]]* 2
      pointm[Serdaigle] = joueur[atrributs[1]] *2
      pointm[Poufsoufle] = joueur[atrributs[2]]*2
      pointm[Serpandtard] = joueur[atrributs[3]] *2
      for i in range(questions):
          choix = demander_choix(questions[i][0], questions[i][1])
          pointm[question[i[choix]]] =+ 3
      maisonfinal = afficher_maison_gagante(pointm)
      return maisonfinal