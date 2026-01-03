from poudelardd.utilis.input_utils import demander_choix


def actualiser_points_maisons(maisons, nom_maisons, points):
    if nom_maisons in maisons:
        maisons[nom_maisons] = maisons[nom_maisons] + points
        print("La maison ", nom_maisons, "a maintenant un total de ", maisons[nom_maisons], 'points !')
    else:
        print("Cette maisons n'existe pas")


def afficher_maison_gagnante(maisons):
    score_max = 0
    for a, b in maisons.items():
        if score_max < maisons[a]:
            score_max = maisons[a]
            maions_gagn = a
    return maions_gagn


def repartition_maisons(joueur, questions):
    ptm = {"Gryffondor": 0,
           "Serpentard": 0,
           "Serdaigle": 0,
           "Poufsouffle": 0}
    ptm['Gryffondor'] = joueur["Attributs"]["Courage"]*2
    ptm['Serdaigle'] = joueur["Attributs"]["Intelligence"]*2
    ptm['Poufsouffle'] = joueur["Attributs"]["Loyauté"]*2
    ptm['Serpentard'] = joueur["Attributs"]["Ambition"]*2
    for i in range(len(questions)):
        choix = demander_choix(questions[i][0], questions[i][1])
        ptm[questions[i][2][choix-1]] += 3

    joueur["houses_pts"]=ptm