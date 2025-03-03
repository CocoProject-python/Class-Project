# Ruette Corentin
# Date : 07/11/2024
# Version 1.0

from random import randint

#  cartes
valeurs_cartes = {
    "as": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "valet": 11,
    "dame": 12,
    "roi": 13
}

# Tirer une carte aléatoire
valeur_carte_tiree = randint(1, 13)

# Demander  à l'utilisateur
pronostic = input("Bonjour cher joueur, j’ai en ma possession une carte qui porte un chiffre entre 1 et 13. Le but est de deviner ce chiffre. Allez-y ! (Entrez as, 2, 3, ..., 10, valet, dame, roi) : ").lower()

# Vérifie si le pronostic est valide
if pronostic in valeurs_cartes:

    # Convertir le pronostic en valeur numérique
    valeur_pronostic = valeurs_cartes[pronostic]
    
    # Obtenir le nom de la carte tirée directement à partir du dictionnaire
    nom_carte_tiree = [nom for nom, val in valeurs_cartes.items() if val == valeur_carte_tiree][0]
    
    # Vérifier si le pronostic est correct
    if valeur_pronostic == valeur_carte_tiree:
        print(f"Bien joué ! La carte tirée était : {nom_carte_tiree}")
    else:
        print(f"Mince, essaye à nouveau. La carte tirée était : {nom_carte_tiree}")
else:
    print("Saisie incorrecte. Les valeurs valides sont as, 2, 3, ..., 10, valet, dame, roi.")
