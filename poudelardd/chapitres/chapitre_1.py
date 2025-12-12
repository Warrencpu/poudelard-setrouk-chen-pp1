from poudelardd.univers.personnage import initialiser_personnage
from poudelardd.utilis.input_utils import demander_texte, demander_nombre, load_fichier


def creer_personnage():
    attr = {"courage": 0,
            "intelligence": 0,
            "loyauté" : 0,
            "ambition": 0}
    nom = initialiser_personnage(demander_texte(input("quel est votre nom"))
    prenom =demander_texte(input("quel est votre prenom"))
    print("Choisissez vos attributs")
    attr[courage]=demander_nombre("niveau de courage (1-10) ",1,10)
    attr[intelligence]=demander_nombre("niveau d'intelligence (1-10) ", 1, 10)
    attr[loyauté]=demander_nombre("niveau de loyauté (1-10) ", 1, 10)
    attr[ambition]=demander_nombre("niveau d'ambition (1-10) ", 1, 10)
    perso = initialiser_personnage(nom,prenom,attr)
    return perso
#3
def recevoir_lettre():
    lettre=int(input("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... « Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! » Souhaitez-vous accepter cette invitation et partir pour Poudlard ? 1. Oui, bien sûr ! 2. Non, je préfère rester avec l’oncle Vernon... "))
    if lettre == 1:
       print("Votre choix:", lettre)
    elif lettre == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » Le monde magique ne saura jamais que vous existiez... Fin du jeu. ")
        exit(0)
    else:
        print("Erreur veuillez saisir une valeur valide")
        exit(1)

#4
def rencontrer_hagrid(personnage):
    print("Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.' \n","Voulez-vous suivre Hagrid ? \n 1. Oui \n 2. Non "))
    votre_choix=int(input())
    print(votre_choix)
    if votre_choix != 1 or 2:
        print("Error")
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui! ")
        exit(0)
#5
def acheter_fourniture:
    load_fichier(poudelardd/data/inventaire.json)
    print("Bienvenue sur le Chemin de Traverse ! ")


