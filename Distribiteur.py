# Demander à l'utilisateur la somme souhaitée
somme_demandee = int(input("Entrez la somme souhaitée en euros : "))

# Liste des valeurs de pièces et de billets disponibles
valeurs = [20, 10, 5, 2, 1]

# Initialiser un dictionnaire pour stocker le nombre de chaque pièce/billet à distribuer
pieces_a_distribuer = {}

# Calculer les pièces/billets à distribuer pour chaque valeur
for valeur in valeurs:
    nombre_de_pieces = somme_demandee // valeur
    if nombre_de_pieces > 0:
        pieces_a_distribuer[valeur] = nombre_de_pieces
        somme_demandee %= valeur

# Afficher les pièces/billets à distribuer
print("Vous recevrez :")
for valeur, nombre_de_pieces in pieces_a_distribuer.items():
    if valeur >= 10:
        print(f"{nombre_de_pieces} billets de {valeur} euros")
    else:
        print(f"{nombre_de_pieces} pièces de {valeur} euro(s)")

