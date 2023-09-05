import random

nombreMystere = random.randint(1,10)
essais = 0
essaisMax = 3

while essais != essaisMax:
    entree = input("Veuillez saisir un nombre compris entre 1 et 10\n")
    essais = essais + 1
    if entree.isdigit():
        nombre = int(entree)
        if nombre == nombreMystere:
           print("Vous avez gagné")
           break
        else:
            if essais == essaisMax:
                print("vous avez perdu")
            else:
                if nombre < nombreMystere:
                    print("Le nombre mystère est plus grand")
                else:
                    print("le nombre mystère est plus petit")
                    if nombre == nombreMystere:
                        print("C'est bien ça")
                    elif essais == essaisMax:
                        print("Le nombre mystere était: ",nombreMystere)

