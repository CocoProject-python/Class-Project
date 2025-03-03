# Ruette Corentin
# Date : 05/11/2024
# Version : 1.0 exercice


nbValeurs = 10
listeValeurs = []

nbElement = 10

for i in range(nbValeurs):
    print("Saisir entier " ,i, ":")
    listeValeurs.append(int(input()))


nbEchange = 1

while(nbEchange !=0): # Tant qu'il y a eu des échanges
    nbEchange = 0 # Initialise à 0 le nb d'échange

    for i in range (nbValeurs - 1):

        if listeValeurs[i] > listeValeurs[i+1]: # est ce qu'il faut inverser
            temp = listeValeurs[i] # Alors stocker 
            listeValeurs[i] = listeValeurs[i+1] # Pour ensuite faire l'échange
            listeValeurs[i+1] = temp
            nbEchange += 1 # Incrémenter le nb echange

for i in range (nbValeurs):
    print(listeValeurs[i])

print(listeValeurs[-1]) # Print le dernier chiffre
print(listeValeurs[-3:]) # Print les 3 derniere chiffre
print(listeValeurs[:]) # Print toute la liste
print(listeValeurs[1:3]) # Print le 2 et le 3

del listeValeurs[1] # Supprime la valeur 2 car liste1 = 2
print(listeValeurs) # Affiche tout sauf le deux

listeValeurs.reverse() # Va inverser la liste
print(listeValeurs) # affiche la liste de manière inverser

print(len(listeValeurs)) # Affiche que le 9 (i:9)
print(listeValeurs.count(4)) # Compte a l'envers et affiche le 1
print(listeValeurs.index(5)) # Index = va chercher et affichier le 5

for valeur in listeValeurs : 
    print(valeur) # va afficher les valeurs une par une en partant de 10


