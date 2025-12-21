from poudelardd.chapitres.chapitre_2 import joueur
from poudelardd.univers.personnage import initialiser_personnage, modifier_argent, afficher_personnage, ajouter_objet
from poudelardd.utilis.input_utils import demander_texte, demander_nombre, load_fichier, demander_choix

def intro():
    input("Bienvenue dans le monde des sorciers")
    input("Une menace qui pèse sur l'école de Poudelard et toi seulement peux y remedier")
    input("Nous vous souhaitons une bonne partie , Bonne chance ☆*: .｡. o(≧▽≦)o .｡.:*☆")


def creer_personnage():
    attr = {"Courage": 0,
            "Intelligence": 0,
            "Loyauté" : 0,
            "Ambition": 0}
    nom =demander_texte("quel est votre nom")
    prenom = demander_texte("quel est votre prenom")
    print("Choisissez vos attributs")
    for a, b  in attr.items():
        b = demander_nombre("niveau de {} (1-10) ".format(a),1,10)
        attr[a] = b
    return initialiser_personnage(nom,prenom,attr)


#3
def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... « Cher élève")
    choix = demander_choix("Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! ",["oui","non"])
    if choix == 1:
        print("Bienvenue a Poudelard")
    if choix == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » Le monde magique ne saura jamais que vous existiez... Fin du jeu. ")
        exit(0)

#4
def rencontrer_hagrid(personnage):
    choix = demander_choix("Hagrid : 'Salut{} ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse. EGH T'veux m'suivre dans cte aventure pti".format(personnage["Prenom"]),["oui","non"])
    if choix == 1:
        print(" Tant mieux ptit loupiaux")
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui! ")

#5

def acheter_fourniture(personnage):
    catalogue = load_fichier("../data/inventaire.json")
    objet_obligatoire = ["Baguette magique","Robe de sorcier","Manuel de potions",]

    print("   Boutique du Chemin de Traverse")
    print("Vous avez {} galions.".format(personnage["Argent"]))

    for obj in catalogue:
        nom_obj, prix = catalogue[obj]
        print("{} : {}  : {} galions".format(obj, nom_obj, prix))

    while objet_obligatoire != []:
        print("\n vous avez {} galions".format(personnage["Argent"]))
        print("Objets obligatoires à acheter ", objet_obligatoire)
        choix = str(demander_nombre("Entrez le numéro de l'objet à acheter", 1, 8))
        if catalogue[choix][1] > personnage["Argent"]:
            print("Vous n'avez pas assez d'argent")
            exit(0)

        obj_present = False
        for i in range(len(objet_obligatoire)):
            if catalogue[choix][0] == objet_obligatoire[i]:
                obj_present = True
                ind = i
        if obj_present == True:
            del objet_obligatoire[ind]

        modifier_argent(personnage, -catalogue[choix][1])
        ajouter_objet(personnage,"Inventaire",catalogue[choix][0])

        print("vous avez acheté : {} (-{} galions)".format(catalogue[choix][0], catalogue[choix][1]))
    print("Vous avez acheté tous les objets obligatoires !")

    animaux = {"1":["Chouette",20],
               "2":["Chat",15],
               "3":["Rat",10],
               "4":["Crapaud",5]}

    print("\n vous avez {} galions".format(personnage["Argent"]))
    print("Voici les animaux disponibles")
    for obj in animaux:
        nom_obj, prix = animaux[obj]
        print("{} : {}  : {} galions".format(obj, nom_obj, prix))
    choix = str(demander_nombre("Quel animal voulez-vous ?",1,4))

    if animaux[choix][1] > personnage["Argent"]:
        print("Vous n'avez pas asser d'argent")
        exit(0)

    print("Vous avez choisi {} (-{} galions)".format(animaux[choix][0], animaux[choix][1]))
    modifier_argent(personnage, -animaux[choix][1])

    ajouter_objet(personnage,"Inventaire",animaux[choix[0]])


    input("Tous les objets obligatoires ont été achetés , Voici votre inventaire final")

    afficher_personnage(personnage)




def lancer_chapitre1():
    intro()
    personnage = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(personnage)
    acheter_fourniture(personnage)
    print("Vous avez fini le chapitre 1 (✿◡‿◡)")
    return personnage

