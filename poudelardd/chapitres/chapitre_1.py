from poudelardd.univers.personnage import initialiser_personnage
from poudelardd.utilis.input_utils import demander_texte, demander_nombre, load_fichier, demander_choix

def intro():

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
def acheter_fourniture ():
    argent= 100


    objets=load_fichier(poudelardd/data/inventaire.json)
    print("Bienvenue sur le Chemin de Traverse ! ")
    print("Vous devez acheter trois objets obligatoires : Une baguette magique, une robe de sorcier et un manuel de potions.")
    print("Vous avez 100 galions.")

perso = creer_personnage()
rencontrer_hagrid(perso)