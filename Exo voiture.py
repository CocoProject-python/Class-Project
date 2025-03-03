# Liste pour stocker les voitures
listeVoitures = []

# Demander à l'utilisateur d'entrer les informations de 12 voitures
print("Veuillez entrer 12 voitures")
for i in range(2):
    voiture = {}
    voiture["matricule"] = input("Entrez son matricule : ")
    voiture["marque"] = input("Entrez sa marque : ")
    voiture["modele"] = input("Entrez son modèle : ")
    voiture["prix"] = float(input("Entrez son prix : "))  # Convertir en float pour comparer les prix

    listeVoitures.append(voiture)

# Trouver la voiture qui coûte le plus cher
maximum = listeVoitures[0]
for voiture in listeVoitures:
    if voiture["prix"] > maximum["prix"]:
        maximum = voiture

# Afficher la voiture la plus chère
print("La voiture la plus chère :")

print("Marque :", maximum["marque"])


