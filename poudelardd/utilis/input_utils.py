#1
def demander_texte(messages):
    valide= False
    while valide == False:
        dmd = input(messages)
        if dmd.strip() !="":
            valide = True
    return dmd


def demander_nombre(message,val_min=None,val_max=None):
    valide = False
    while valide == False :
        n = input(message)
        v = True
        for i in n :
            i = ord(i)
            if ord('a')< i <ord('z') or ord('A') < i < ord('Z'):
                v = False
            elif val_max is not None and val_min is not None:
                if  ord(n) < val_min or  ord(n)> val_max :
                    v = False
        if v == True :
            valide = True
        return ord(n)





def demander_choix(messages,options):
    valide = False
    while valide == False:
        print(messages)
        for i in range(len(options)):
            print(i+1,".",options[i])
        if demander_nombre("Votre choix :",0,len(options)):
            valide = True
        return valide

#4
import json

def load_fichier(chemin_fichier):
    with open (chemin_fichier,"r",encoding='utf-8') as f:
        dico = json.load(f)
    return dico


demander_nombre("caca",0,10)