import json
from poudelardd.univers.maison import repartition_maisons, afficher_maison_gagnante
from poudelardd.utilis.input_utils import *
from poudelardd.univers.personnage import *


def rencontrer_amis(joueur):
    input("Vous montez à bord du Poudlard Express. Le train démarre lentement en  direction du Nord...  ")
    input("Un garçon roux entre dans votre compartiment, l’air amical. ")
    input("Salut ! Moi c'est Ron Weasley. Tu veux bien qu'on s'assoie ensemble ?")
    choixRon = demander_choix("Que répondez-vous ?",["Bien sur, assieds-toi !", "Désolé , je préfère voyager seul.e."])
    if choixRon == 2 :
        joueur['Attributs']['Ambition'] += 1
        input("Il rebrousse chemin la tête basse")
    elif choixRon == 1  :
        joueur['Attributs']['Loyauté'] += 1
        input("il prend place à coté de vous avec un grand sourire")
    input("Bonjour, je m'apelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie'?")
    choixHer = demander_choix("Que repondez-vous ?",["Oui, j'adore apprendre de nouvelles choses !", "Euh... non, je préfère les aventures aux bouquins."])
    if choixHer == 1 :
        joueur['Attributs']['Intelligence'] += 1
        input("Je suis sûre que nous allons bien nous entendre !")
    elif choixHer == 2  :
        joueur['Attributs']['Courage'] += 1
        input("Elle vous regarde, deçue avant de partir")
    input("Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choixDra = demander_choix("Comment réagissez-vous?",["Je lui serre la main poliment.","Je l'ignore complètement.","Je lui réponds avec arrogance."])
    if choixDra == 1 :
        joueur['Attributs']['Ambition'] += 1
        input("Tu fait le bon choix, crois moi")
    elif choixDra == 2 :
        joueur['Attributs']['Loyauté'] += 1
        input("Il te lance un regard noir avant de rebrousser chemin")
    elif choixDra == 3 :
        joueur['Attributs']['Courage'] += 1
        input("Tu fera moins le.a malin.e quand je t'aurais battu.e")
    input("Le train continue sa route. Le chateau de Poudlard se profile à l'horizon...")
    input("Tes choix semblent déjà en dire long sur ta personalité !")
    input("Tes attributs mis à jour : {}".format(joueur['Attributs']))

def mot_de_bienvenue():
    input("Bienvenue à Poudlard un endroit où la magie nest pas seulement dans les sorts mais aussi dans les rencontres les découvertes et parfois dans les imprévus qui transforment une journée ordinaire en souvenir inoubliable")
    input("Chaque année apporte son lot de défis et de surprises et cest ce qui fait de cette école un lieu unique")
    input("Ici on apprend autant de ses réussites que de ses erreurs et il ny a aucune honte à trébucher tant quon se relève avec la volonté de continuer")
    input("Souvenez vous que la curiosité ouvre des portes que le courage se trouve souvent là où on lattend le moins et que même la plus petite lumière peut éclairer un long chemin")
    input("Si vous vous perdez dans les couloirs ou dans vos pensées respirez et avancez pas à pas quelquun finira toujours par vous tendre la main")
    input("Je vous souhaite à tous une année pleine de magie de rires et de découvertes Que Poudlard soit pour vous un refuge un défi et une aventure")

def ceremonie_repartition(joueur):
    input("La cérémonie de répartition commence dans la Grande salle...")
    input("Le Choixpeau magique t'observe longuement avant de poser ses questions: ")
    questions = [
    (
        "Tu vois un ami en danger. Que fais-tu ?",
        ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l'aide", "Je reste calme et j'observe"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Quel trait te décrit le mieux ?",
        ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Face à un défi difficile, tu...",
        ["Fonce sans hésiter", "Cherche la meilleure stratégie", "Compte sur tes amis", "Analyse le problème"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    )]
    house =repartition_maisons(joueur, questions)
    gagnant = afficher_maison_gagnante(house)
    print("Résumé des scores : ")
    for a,b in house.items():
        print("{} : {} points". format(a,b))
    input("Le Choipeau s'exclame : {} !!".format(gagnant))
    input("Tu rejoints les éléves de {} sous les acclamations ! ".format(gagnant))
    joueur["maison_j"] = gagnant
    return gagnant

def installation_salle_commune(joueur):
    dico = load_fichier("../data/maisons.json")
    print(dico[joueur["maison_j"]])


def lancer_chapitre_2(joueur):
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    print("Vous avez fini le chapitre 2 (˶ᵔ ᵕ ᵔ˶)")
