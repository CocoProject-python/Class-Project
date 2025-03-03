# Ruette Corentin
# Date : 07/11/2024
# Version 1.0

print("Formule Rapide (1)") # Affiche les formule au client
print("Formule Gourmande (2)")
print("Formule Prestige (3)")


dessert = ("oui")
fromage = ("oui") # variable qui va nous servire plus tars

oui = fromage and dessert # pareil

rapide = ("Formule Rapide") # Variable pour les menus
Gourmande = ("Formule Gourmande")
prestige = ("Formule Prestige")

interraction = int(input("Veuillez choisir entre 1 et 3 : ")) # demande au client de choisir

choix_menu = interraction




if interraction == 1 : # si 1 choisis alors print 

    print("Vous avez choisis la Formule Rapide")
    print("Dans cette formule vous avez ni fromage ni dessert")

else:
    print("") 

if interraction == 2 :  # si 2 choisis alors print et demande de supplément 

    print("Vous avez choisis la Formule Gourmande")
    fromage= input("Souhaiter vous du fromage : ")
    dessert = input("Souhaiter vous du dessert : ")
    if dessert == fromage:
        print("Désolé la formule n'est pas la bonne celle ci contient soit un fromage soit un dessert")
    else:
        print("")



if interraction == 3 : # si 3 choisi le client prend se qu'il veut

    print("Vous avez choisis la Formule Prestige")
    fromage= input("Souhaiter vous du fromage : ")
    dessert = input("Souhaiter vous du dessert : ")
    print("Pas de soucis bon appétit ! ")
else:
    print("")





