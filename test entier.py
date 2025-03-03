# Initialiser une liste vide pour stocker les 10 entiers
entiers = []

# Demander à l'utilisateur de saisir 10 entiers
print("Veuillez entrer 10 entiers")
for i in range(10):
    nombre = int(input(f"Entrez l'entier numéro {i + 1}: "))
    entiers.append(nombre)

# Calculer la somme manuellement en utilisant une boucle
somme = 0
for nombre in entiers:
    somme += nombre

# Trouver le plus petit nombre en utilisant une boucle
minimum = entiers[0]
for nombre in entiers:
    if nombre < minimum:
        minimum = nombre

# Calculer la moyenne
moyenne = somme / len(entiers)

# Afficher les résultats

print("Somme des 10 entiers :", somme)
print("Plus petit entier :", minimum)
print("Moyenne des entiers :", moyenne)
