prof1 = { "nom" : "lefranc" , "Prenom" : "Lucas" , "Date" : 1990 , "Matiere" : "Math"}
prof2 = { "nom" : "durant" , "Prenom" : "marvin" , "Date" : 2000 , "Matiere" : "eps"}
s1 = { "nom" : "Ruette" , "Prenom" : "Corentin", "Prof" : prof1}
s2 = { "nom" : "scofield" , "Prenom" : "Mickael", "Prof" : prof2}


if (prof1["nom"]) == (prof2["nom"]):
    print("Il sont le même prof")
else:
    print("Les élèves n'ont pas le même prof ! ")


if (prof1["Date"]) < (prof2["Date"]):
    print("L'élèves 1 a le prof le plus vieux")

if (prof1["Date"]) > (prof2["Date"]):
    print("L'élèves 2 a le prof le plus vieux")

notes_eleve_1 = []

print("Veuillez entrer 5 notes")
for i in range(5):
    nombre = float(input("Entrez les notes de l'élèves 1: "))
    notes_eleve_1.append(nombre)


notes_eleve_2 = []

print("Veuillez entrer 5 notes")
for i in range(5):
    nombre = float(input("Entrez les notes de l'élèves 2: "))
    notes_eleve_2.append(nombre)

# Calculer la somme manuellement en utilisant une boucle
somme = 0
for nombre in notes_eleve_1:
    somme += nombre


# Calculer la moyenne eleve 1
moyenne = somme / len(notes_eleve_1)

# Afficher les résultats

print("Moyenne de l'élève 1 et de :", moyenne , "/20")


# Calculer la somme manuellement en utilisant une boucle
somme = 0
for nombre in notes_eleve_2:
    somme += nombre


# Calculer la moyenne eleve 2
moyenne = somme / len(notes_eleve_2)

# Afficher les résultats

print("Moyenne de l'élève 2 et de :", moyenne , "/20")

