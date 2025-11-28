def demander_nombre(message,val_min,val_max):
    valide=true
    while valide==true:
        n = input("Niveau de courage (1-10) : ", val_min, val_max)
        if n>val_max or n<val_min:
            valide=false
            print("Veuillez entrer un nombre entre",val_min,"et",val_max)











