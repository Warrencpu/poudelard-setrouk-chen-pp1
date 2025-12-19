from poudelardd.univers.maison import repartition_maisons
from poudelardd.univers.personnage import*
import random

def apprendre_sorts(joueur,load_fichier='../data/sorts.json'):
    print("Tu commences tes cours de magie a Poudlard")
    print("Tu viens d'apprendre le sortilege :")
    if random.choice = "Offensif":
        joueur['Sortilege']['Offensif'] += 1
    if random.choice = "Defensif":
        joueur['Sortilege']['Defensif'] += 1


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    questions = load_fichier(chemin_fichier)
    input("Bienvenue au quiz de magie de Poudelard ! ;]")
    for i in range (4):
        points = 0
        ques = random.choice(questions)
        q = demander_texte(questions[ques["question"]])
        input("1.",q)
        rep = demander_texte("->")
        bn_rep = True
        for i in ques["reponse"]:
            if rep[i] != ques[i]:
                bn_rep = False
        if bn_rep == True:
            input("Vous avez la bonne reponse UwU , + 25 points pour votre maison")
            points += 25
        else:
            input("Mauvaise réponse `(*>﹏<*)′, la bonne reponse était {} ".format(ques["reponse"]))
        input("score obtenu = {} points".format(points))



joueur = initialiser_personnage("Pottah","Harry",{"Courage": 0,
            "Intelligence": 0,
            "Loyauté" : 0,
            "Ambition": 0})

quiz_magie(joueur)