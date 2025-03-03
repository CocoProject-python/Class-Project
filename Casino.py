# Ruette Corentin
# Date : 07/11/2024
# Version 1.0
import random
from random import randint


roulette = randint(0, 12)

print(roulette)

pair = {
    "2": 2,
    "4": 4,
    "6": 6,
    "8": 8,
    "10": 10,
    "12": 12,
}

impair = {
    "1": 1,
    "3": 3,
    "5": 5,
    "7": 7,
    "9": 9,
    "11": 11,
}

argent_joueur = 10
gain_roulette = 10 * 13
gain_pair = 10 * 2

print(""" Bonjour chère joueur bienvenue au casino de queneau voici les règles
     ---Si vous parier sur le numéro sortant vous gagner 13 fois votre mise ---
    --- Si vous choisiez de parier sur la parité d'un numéro vous gagner deux fois votre mise ---
    --- Si vous perdez , vous perdez vos gains --- 
      """)  # J'ai ajouter des petite règle c'était pas demander mais sa aide le "joueur"

# Pour rappel le joueur a seulement 10 €

pari = input(" Veuillez choisir un nombre entre 0 et 12 ou pair ou impair : ")


if  pair and impair:
    print("Bien joué !")
    print("Vous avez gagné", gain_pair, "€")

if pari == roulette:
    print("Bien joué !")
    print("Vous avez gagné", gain_roulette, "€")
     


     



    

















