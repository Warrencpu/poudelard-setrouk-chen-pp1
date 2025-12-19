from poudelardd.chapitres.chapitre_1 import lancer_chapitre1
from poudelardd.univers.personnage import repartition_maisons
from poudelardd.utilis.input_utils import demander_choix, load_fichier


def rencontrer_amis(joueur):
    input("Vous montez à bord du Poudlard Express. Le train démarre lentement en  direction du Nord...  ")
    input("Un garçon roux entre dans votre compartiment, l’air amical. ")
    input("Salut ! Moi c'est ron Weasley. Tu veux bien qu'on s'assoie ensemble ?")
    choixRon = demander_choix("Que répondez-vous ?",["Bien sur, assieds-toi !", "Désolé , je préfère voyager seul.e."])
    if choixRon == 2 :
        joueur['Attributs']['Ambition'] += 1
    elif choixRon == 1  :
        joueur['Attributs']['Loyauté'] += 1
    input("Bonjour, je m'apelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie'?")
    choixHer = demander_choix("Que repondez-vous ?",["Oui, j'adore apprendre de nouvelles choses !", "Euh... non, je préfère les aventures aux bouquins."])
    if choixHer == 1 :
        joueur['Attributs']['Intelligence'] += 1
    elif choixHer == 2  :
        joueur['Attributs']['Courage'] += 1
    input("Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choixDra = demander_choix("Comment réagissez-vous?",["Je lui serre la main poliment.","Je l'ignore complètement.","Je lui réponds avec arrogance."])
    if choixDra == 1 :
        joueur['Attributs']['Ambition'] += 1
    elif choixDra == 2 :
        joueur['Attributs']['Loyauté'] += 1
    elif choixDra == 3 :
        joueur['Attributs']['Courage'] += 1
    input("Le train continue sa route. Le chateau de Poudlard se profile à l'horizon...")
    input("Tes choix semblent déjà en dire long sur ta personalité !")
    input("Tes attributs mis à joue : {}".format(joueur['Attributs']))

def mot_de_bienvenue():
    input("Bienvenue à Poudlard un endroit où la magie nest pas seulement dans les sorts mais aussi dans les rencontres les découvertes et parfois dans les imprévus qui transforment une journée ordinaire en souvenir inoubliable\nChaque année apporte son lot de défis et de surprises et cest ce qui fait de cette école un lieu unique Ici on apprend autant de ses réussites que de ses erreurs et il ny a aucune honte à trébucher tant quon se relève avec la volonté de continuer\nSouvenezvous que la curiosité ouvre des portes que le courage se trouve souvent là où on lattend le moins et que même la plus petite lumière peut éclairer un long chemin Si vous vous perdez dans les couloirs ou dans vos pensées respirez et avancez pas à pas quelquun finira toujours par vous tendre la main\nJe vous souhaite à tous une année pleine de magie de rires et de découvertes Que Poudlard soit pour vous un refuge un défi et une aventure")

def ceremonie_repartition(joueur):
    input("La cérémonie de répartition commence dans la Grande salle...")
    input("Le Choixpeau magique t'observe longuement avant de poser ses questions: ")
    questions = [
    (
        "Tu vois un ami en danger. Que fais-tu ?",
        ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de laide", "Je reste calme et jobserve"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Quel trait te décrit le mieux ?",
        ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Face à un défi difficile, tu...",
        ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    )]
    maisons , gagnant =repartition_maisons(joueur, questions)
    print("Résumé des scores : ")
    for a,b in maisons:
        print("{} : {} points". format(a,b))
    input("Le Choipeau s'exclame : {} !!".format(gagnant))
    input("Tu rejoints les éléves de {} sous les acclamations ! ".format(gagnant))
    return gagnant

def installation_salle_commune(joueur):
    dico = load_fichier("maisons.json")
    print(dico["attrib"])