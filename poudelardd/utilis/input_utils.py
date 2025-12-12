import json
#1
def demander_texte(messages):
    valide = False
    while valide == False:
        dmd = input(messages)
        if dmd.strip() != "" :
            valide = True
    return dmd.strip()
#2
def demander_nombre(message,val_min=None,val_max=None):
    valide = true
    while valide == True:
        m = demander_texte(input(message))
        for i in m :
            if i is int or i == "-" :
                if m >= val_min and m <= val_max:
                    print(message , n)
                    valide = False
    return m
#3
def demander_choix(messages,options):
    correct = False
    while correct == False:
        print(messages)
        for i in range(len(options)):
            print(i + 1 ,".", options[i])
        if demander_nombre("Votre choix :",0,len(options)):
            correct = True
        return choix

#4

def load_fichier(chemin_fichier):
    with open (chemin_fichier,"r",encoding='utf-8') as f:
        dico = json.load(f)
    return dico


#5
def recevoir_lettre():
    lettre=int(input("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... « Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! » Souhaitez-vous accepter cette invitation et partir pour Poudlard ? 1. Oui, bien sûr ! 2. Non, je préfère rester avec l’oncle Vernon... "))
    if lettre == 1:
       print("Votre choix:", lettre)
    else:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » Le monde magique ne saura jamais que vous existiez... Fin du jeu. ")
        exit(0)


