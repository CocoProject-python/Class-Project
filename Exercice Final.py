# Ruette Corenin
# Date : 07/11/2024
# Version 1.0

# Initialisation ordinateur
ordinateur = []

# Style python


# Creation du menu a interaction

print("Ajout d'un ordinateur (1)")
print("Supprimer ordinateur (2) ")
print("Voir la liste des ordinateurs (3) ")
print("Retour au menu (4) ")
print("Quitter le programme (5) ")

# Demande utilisateur info des pc

menu = int(input("Veuillez renseigner votre choix : "))

if menu == 1:
    ordinateuradd = {}

    ordinateuradd["Adresse Mac"] = input("Entrez son adresse mac : ")
    ordinateuradd["Adresse Ip"] = input("Entrez son adresse ip : ")
    ordinateuradd["Nom"] = input("Entrez son nom : ")

    ordinateur.append(ordinateuradd)

    str.split(ordinateuradd["Adresse Ip"])

    print(ordinateuradd["Adresse Ip"])


