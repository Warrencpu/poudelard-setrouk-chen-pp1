from poudelardd.chapitres.chapitre_1 import lancer_chapitre1
from poudelardd.utilis.input_utils import demander_choix


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


jouer = lancer_chapitre1()
rencontrer_amis(jouer)
print(jouer)
