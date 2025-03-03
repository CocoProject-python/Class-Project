# determiner le nombre de plis d'une feuille de papier standard
# pour atteindre la distance Terre-Lune
# Auteur : Ruette Corenti

DISTANCE_TERRE_LUNE = 384e6
EPAISSEUR_FEUILLE = 1e-4

hauteur_atteinte = EPAISSEUR_FEUILLE
nombre_plis = 0


DEMANDE = 42

# tant que la distance Terre_Lune n'est pas comblée
while DEMANDE == 42:

        demande = int(input("A votre avis combien de plis faut t'il pour atteindre la lune ? : "))

        if demande < 42:
            print("c'est plus !")
        else: 
            print("")

        if demande > 42:
            print("C'est moins")

        else:
            print("")

        if demande == 42:
            print("Bien joué")
            break
        else :
             print("")
             
        

while hauteur_atteinte < DISTANCE_TERRE_LUNE:
        # plier la feuille en 2
        hauteur_atteinte = hauteur_atteinte * 2
        # le nombre de plis est incrémenté
        nombre_plis = nombre_plis + 1
print(f"Il faut plier {nombre_plis} fois une feuille de papier pour" "atteindre la lune")








