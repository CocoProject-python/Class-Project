# Auteur Corentin Ruette
# Date 18/09/2024
# Version 1.0

# Programme Conversion mètres vers pieds et pouces

print("Ce programme convertit une taille donnée en mètres en une taille donnée en pieds et en pouces.")

# Demander la hauteur en mètres
metres = float(input("Saisir la hauteur en mètres : "))

# Convertir les mètres en pieds
metres_en_pieds = metres / 0.3048

# Obtenir la partie entière (pieds)
pieds = int(metres_en_pieds)

# Obtenir la partie restante (décimale) et la convertir en pouces
pouces = round((metres_en_pieds - pieds) * 12)

# Afficher le résultat
print(f"La hauteur est de {pieds} pieds et {pouces} pouces.")
