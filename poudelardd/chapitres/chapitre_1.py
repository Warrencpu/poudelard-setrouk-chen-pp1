from poudelardd.univers.personnage import initialiser_personnage
from poudelardd.utilis.input_utils import demander_texte, demander_nombre, load_fichier, demander_choix

def intro():
    input("Bienvenue dans le monde des sorciers")
    input("Une menace qui pèse sur l'école de Poudelard et toi seulement peu y remedier")
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
        print(" Tant mieu ptit loupiaux")
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui! ")

#5
def acheter_fourniture(personnage):

    catalogue = {
        "0": ("Quitter la boutique", 0),
        "1": ("Baguette magique", 35),
        "2": ("Robe de sorcier", 20),
        "3": ("Chaudron en étain", 15),
        "4": ("Manuel de potions", 25),
        "5": ("Plume magique", 5),
        "6": ("Livre enchanté", 30),
        "7": ("Balance de cuivre", 10),
        "8": ("Cape d'invisibilité", 100)
    }

    achats = []
    choix = ""

    print("Le caissier vous reconnaît et vous offre 100 galions.")
    personnage["Argent"] += 100

    while choix != "0":

        print("\n Boutique du Chemin de Traverse")
        print("Vous avez {} galions.".format(personnage["Argent"]))

        for obj in catalogue:
            nom, prix = catalogue[obj]
            if obj == "0":
                print("{} : {}".format(obj, nom))
            else:
                print("{} : {} pour {} galions".format(obj, nom, prix))

        choix = input("Votre choix : ")

        if choix not in catalogue:
            print("Choix invalide.")
            continue

        nom_objet, prix = catalogue[choix]

        if choix == "0":
            print("Vous sortez de la boutique.")
            continue

        if personnage["Argent"] < prix:
            print("Fonds insuffisants pour {}.".format(nom_objet))
            continue

        personnage["Argent"] -= prix
        personnage["Inventaire"].append(nom_objet)
        achats.append(nom_objet)

        print("{} a été ajouté à votre inventaire.".format(nom_objet))
        print("Argent restant : {} galions.".format(personnage["Argent"]))

    print("\nRésumé de vos achats :")
    for objet in achats:
        print("- " + objet)

    return personnage



    objets=load_fichier(poudelardd/data/inventaire.json)
    print("Bienvenue sur le Chemin de Traverse ! ")
    print("Vous devez acheter trois objets obligatoires : Une baguette magique, une robe de sorcier et un manuel de potions.")
    print("Vous avez 100 galions.")


def lancer_chapitre1():
    intro()
    personnage = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(personnage)
    acheter_fourniture(personnage)
    print("Vous avez fini le chapitre 1 (✿◡‿◡)")
    return personnage

