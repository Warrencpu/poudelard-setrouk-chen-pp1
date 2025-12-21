from poudelardd.univers.maison import actualiser_points_maisons
from poudelardd.univers.personnage import*
import json
import random

def apprendre_sorts(joueur, chemin_fichier="./data/sorts.json"):
    lst_sorts = load_fichier(chemin_fichier)
    offensif = 0
    defensif = 0
    utilitaire = 0
    input("tu commence tes cours de magie à Poudlard...")
    while len(joueur["Sortilèges"]) < 5:
        i = random.randint(0, len(lst_sorts)-1 )
        sort = lst_sorts[i]
        deja_pris = False
        for s in joueur["Sortilèges"]:
            if s == sort:
                deja_pris = True
        if deja_pris == False:
            if sort["type"] == "Offensif":
                if offensif < 1:
                    joueur["Sortilèges"].append(sort)
                    offensif = offensif + 1
                    print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
            if sort["type"] == "Défensif":
                if defensif < 1:
                    joueur["Sortilèges"].append(sort)
                    defensif = defensif + 1
                    print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
            if sort["type"] == "Utilitaire":
                if utilitaire < 3:
                    joueur["Sortilèges"].append(sort)
                    utilitaire = utilitaire + 1
                    print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
                    input("Appuyer sur entrée pour continuer...")
    input("Tu as terminé ton apprentissage de base à Poudlard ! ")
    input("Voici les sortilèges que tu maîtrises désormais : ")
    for sort in joueur["Sortilèges"]:
        print(sort["nom"])
        print("type :", sort["type"])
        print("description :", sort["description"])
        print("")


def quiz_magie(joueur, chemin_fichier="./data/quiz_magie.json"):
    questions_total = load_fichier(chemin_fichier)
    input("Bienvenue au quiz de magie de Poudelard ! ;]")
    score_total = 0
    for t in range (4):
        question_choisie = random.choice(questions_total)
        input("1. {}".format(question_choisie["question"]))
        reponse = demander_texte("->")
        bn_rep = True
        for i in range (len(reponse)) :
            if len(reponse) != len(question_choisie["reponse"]) or reponse[i] != question_choisie["reponse"][i] :
                bn_rep = False
        if bn_rep is True:
            input("Vous avez la bonne réponse UwU , + 25 points pour vôtre maison")
            score_total += 25
        else:
            input("Mauvaise réponse `(*>﹏<*)′, la bonne reponse était {} ".format(question_choisie["reponse"]))
    input("score obtenu = {} points".format(score_total))
    actualiser_points_maisons(joueur, joueur["maison_j"],score_total)




def lancer_chapitre_3 (joueur) :
    apprendre_sorts(joueur)
    quiz_magie(joueur)
    input("Vous avez fini le chapitre 3 !")
