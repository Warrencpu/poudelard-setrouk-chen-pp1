#1
def demander_texte(messages):
    valide= False
    while valide == False:
        dmd = input(messages)
        if dmd.strip() !="":
            valide = True
#2
def demander_nombre(message,val_min=None,val_max=None):
    valide=true
    while valide==True:
        n = input(("Niveau de courage (1-10) : "),message)
        if n=> val_min and n =< val_max:
            print("Niveau de courage (1-10) : ", n)
            valide = True
        else
            print("Veuillez saisir une valeur valide")
            valide= False
        return n
#3
def demander_choix(messages,options):
    olala = False
    while olala == False:
        print(messages)
        for i in range(len(options)):
            print(i+1,".",options[i])
        if demander_nombre("Votre choix :",0,len(options)):
            olala= True
        return choix

#4
import json

def load_fichier(chemin_fichier):
    with open (chemin_fichier,"r",encoding='utf-8') as f:
        dico = json.load(f)
    return dico





