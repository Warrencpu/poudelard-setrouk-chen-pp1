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


