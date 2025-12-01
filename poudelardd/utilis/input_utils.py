#1
def demander_texte(messages):
    valide= False
    while valide == False:
        dmd = input(messages)
        if dmd.strip() !="":
            valide = True
#2
def demander_nombre(message,val_min,val_max):
    valide=true
    while valide==true:
        n = input("Niveau de courage (1-10) : ", val_min, val_max)
        if n>val_max or n<val_min:
            valide=false
            print("Veuillez entrer un nombre entre",val_min,"et",val_max)
    return
#3
def demander_choix(messages,options):
    olala = False
    while olala == False:
        print(messages)
        for i in range(len(options)):
            print(i+1.".",options[i])
        if demander_nombre("Votre choix :",0,len(options)):
            olala= True
        return choix







