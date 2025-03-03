var1 = int(input("Première valeur : "))
var2 = int(input("Deuxième valeur : "))
var3 = int(input("Troisième valeur : "))


nbEchange = 1

while(nbEchange !=0): # Tant qu'il y a eu des échanges
    nbEchange = 0 # Initialise à 0 le nb d'échange
    if var1 > var2: # est ce qu'il faut inverser
        temp = var1 # Alors stocker 
        var1 = var2 # Pour ensuite faire l'échange
        var2 = temp
        nbEchange += 1 # Incrémenter le nb echange

    if var2 > var3 : # est ce qu'il faut inverser
        temp = var2 # Alors stocker
        var2 = var3 # Pour ensuite faire l'échange
        var3 = temp
        nbEchange +=1 # Incrémenter le nb echange
    

print(var1, " ", var2, " ", var3)