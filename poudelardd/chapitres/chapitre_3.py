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
    while len(joueur["Sortilèges"]) != 5:
        i = random.randint(0, len(sorts) - 1)
        sort = sorts[i]
        deja_pris = False
        for s in joueur["Sortileges"]:
            if s == sort:
                deja_pris = True
        if deja_pris == True:
            continue
        if sort["type"] == "offensif":
            if offensif < 1:
                joueur["Sortileges"].append(sort)
                offensif = offensif + 1
                print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
        if sort["type"] == "defensif":
            if defensif < 1:
                joueur["sortileges"].append(sort)
                defensif = defensif + 1
                print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
        if sort["type"] == "utilitaire":
            if utilitaire < 3:
                joueur["Sortileges"].append(sort)
                utilitaire = utilitaire + 1
                print("Sort appris :", sort["nom"], "(" + sort["type"] + ")")
    print("")
    print("Recapitulatif :")
    for sort in joueur["Sortileges"]:
        print(sort["nom"])
        print("type :", sort["type"])
        print("description :", sort["description"])
        print("")


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    questions_total = load_fichier(chemin_fichier)
    input("Bienvenue au quiz de magie de Poudelard ! ;]")
    score_total = 0
    for t in range (4):
        question_choisie = random.choice(questions_total)
        input("1. {}".format(question_choisie["question"]))
        reponse = demander_texte("->")
        bn_rep = True
        for i in range (len(reponse)) :
            if reponse[i] != question_choisie["reponse"][i] :
                bn_rep = False
        if bn_rep is True:
            input("Vous avez la bonne réponse UwU , + 25 points pour vôtre maison")
            score_total += 25
        else:
            input("Mauvaise réponse `(*>﹏<*)′, la bonne reponse était {} ".format(ques["reponse"]))
    input("score obtenu = {} points".format(score_total))
    joueur["score"] = score_total




def lancer_chapitre_3 (joueur) :
    apprendre_sorts(joueur)
    quiz_magie(joueur)
