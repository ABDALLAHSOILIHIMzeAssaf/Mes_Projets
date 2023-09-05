import re
import random

def evaluer_complexite(mot_de_passe):
    longueur = len(mot_de_passe)
    force = 0

    # Vérifier la longueur minimale
    if longueur >= 8:
        force += 1

    # Vérifier l'utilisation de lettres majuscules et minuscules
    if re.search(r'[A-Z]', mot_de_passe) and re.search(r'[a-z]', mot_de_passe):
        force += 1

    # Vérifier l'utilisation de chiffres
    if re.search(r'\d', mot_de_passe):
        force += 1

    # Vérifier l'utilisation de caractères spéciaux
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', mot_de_passe):
        force += 1

    return force

def generer_suggestion():
    suggestions = [
        "Utilisez une combinaison de lettres majuscules et minuscules.",
        "Ajoutez des chiffres pour améliorer la complexité.",
        "Incluez des caractères spéciaux pour renforcer la sécurité.",
        "Choisissez un mot de passe plus long pour augmenter la robustesse."
    ]
    return random.choice(suggestions)

mot_de_passe = input("Entrez un mot de passe ou un code à chiffre : ")
force_mot_de_passe = evaluer_complexite(mot_de_passe)

if force_mot_de_passe == 0:
    print("La force du mot de passe est très faible.")
    suggestion = generer_suggestion()
    print("Suggestion :", suggestion)
elif force_mot_de_passe == 1:
    print("La force du mot de passe est faible.")
    suggestion = generer_suggestion()
    print("Suggestion :", suggestion)
elif force_mot_de_passe == 2:
    print("La force du mot de passe est moyenne.")
elif force_mot_de_passe == 3:
    print("La force du mot de passe est forte.")
else:
    print("La force du mot de passe est très forte.")

