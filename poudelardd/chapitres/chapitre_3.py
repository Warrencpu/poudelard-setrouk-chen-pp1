from poudelardd.univers.maison import repartition_maisons
from poudelardd.univers.personnage import*
import json
import random

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    fichier = open(chemin_fichier, "r", encoding="utf-8")
    sorts = json.load(fichier)
    fichier.close()
    offensif = 0
    defensif = 0
    utilitaire = 0
    while len(joueur["sortileges"]) != 5:
        i = random.randint(0, len(sorts) - 1)
        sort = sorts[i]
        deja_pris = False
        for s in joueur["sortileges"]:
            if s == sort:
                deja_pris = True
        if deja_pris == True:
            continue
        if sort["type"] == "offensif":
            if offensif < 1:
                joueur["sortileges"].append(sort)
                offensif = offensif + 1
                print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
        if sort["type"] == "defensif":
            if defensif < 1:
                joueur["sortileges"].append(sort)
                defensif = defensif + 1
                print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
        if sort["type"] == "utilitaire":
            if utilitaire < 3:
                joueur["sortileges"].append(sort)
                utilitaire = utilitaire + 1
                print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
    print("")
    print("Recapitulatif :")
    for sort in joueur["sortileges"]:
        print(sort["nom"])
        print("type :", sort["type"])
        print("description :", sort["description"])
        print("")


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

def lancer_chapitre_3 (joueur) :
    apprendre_sorts(joueur,chemin_fichier="../data/sorts.json")
    quiz_magie(joueur,chemin_fichier="..data/quiz_magie.json")
