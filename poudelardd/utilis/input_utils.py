#1
def demander_texte(messages):
    valide= False
    while valide == False:
        dmd = input(messages)
        if dmd.strip() !="":
            valide = True
    return dmd

def nb_existe(nb):
    contient_lettre = False
    for carac in nb:
        if carac not in  '0123456789':
            contient_lettre = True
    return contient_lettre

def demander_nombre(message,val_min=None,val_max=None):
    saisie = False
    while saisie == False :
        nb = demander_texte(message)
        if nb_existe(nb) == False or nb[0] == '-' and len(nb) > 1 and nb_existe(nb[1:]) == False:
            nb = int(nb)
            if val_min is not None or val_max is not None   :
                if nb >= val_min and nb <= val_max:
                    saisie = True
    return nb


def demander_choix(messages,options):
    print(messages)
    for i in range(len(options)):
        print(i+1,".",options[i])
    choix = False
    while choix == False:
        choix = demander_nombre('votre choix' , 1,i+1)
    return choix

#4
import json

def load_fichier(chemin_fichier):
    with open (chemin_fichier,"r",encoding='utf-8') as f:
        dico = json.load(f)
    return dico

