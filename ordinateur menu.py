# Ruette Corentin
# Date : 07/11/2024
# Version 1.0

# programme noté par mr truffley gestion parc info

# Initialisation de la liste des ordinateurs
ordinateurs = []

# Boucle principale pour le menu
while True:
    print("Menu :")
    print("1. Ajouter un ordinateur")
    print("2. Supprimer un ordinateur")
    print("3. Voir la liste des ordinateurs")
    print("4. Quitter le programme")
    
    # Demande à l'utilisateur de choisir une option
    choix = input("Choisissez une option (1-4) : ")

    if choix == '1':  # Ajouter un ordinateur
        # Demander le nom, l'adresse MAC et l'adresse IP
        nom = input("Entrez le nom de l'ordinateur : ")
        adresse_mac = input("Entrez l'adresse MAC de l'ordinateur : ")
        adresse_ip_str = input("Entrez l'adresse IP de l'ordinateur  : ")
        
        # Découpage de l'adresse IP en 4 parties
        ip_parts = adresse_ip_str.split('.')
        adresse_ip = (int(ip_parts[0]), int(ip_parts[1]), int(ip_parts[2]), int(ip_parts[3]))
        
        # Création d'un dictionnaire pour l'ordinateur
        ordinateur = {
            "nom": nom,
            "adresse_mac": adresse_mac,
            "adresse_ip": adresse_ip
        }
        
        # Ajouter l'ordinateur à la liste
        ordinateurs.append(ordinateur)
        print("Ordinateur ajouté avec succès.")

    elif choix == '2':  # Supprimer un ordinateur
        # Demander le nom de l'ordinateur à supprimer
        nom = input("Entrez le nom de l'ordinateur à supprimer : ")
        trouve = False
        
        # Chercher l'ordinateur dans la liste et obtenir son index
        for i in range(len(ordinateurs)):
            if ordinateurs[i]["nom"] == nom:
                # Supprimer l'ordinateur en utilisant `del`
                del ordinateurs[i]
                print(f"Ordinateur {nom} supprimé avec succès.")
                trouve = True
                break
        
        # Si l'ordinateur n'est pas trouvé
        if not trouve:
            print(f"Aucun ordinateur trouvé avec le nom {nom}.")

    elif choix == '3':  # Voir la liste des ordinateurs
        if len(ordinateurs) == 0:
            print("Aucun ordinateur dans la liste.")
        else:
            # Afficher tous les ordinateurs de la liste
            for ordinateur in ordinateurs:
                adresse_ip = ordinateur['adresse_ip']
                # Affichage de l'adresse IP sans utiliser `join`
                print(f"Nom: {ordinateur['nom']}, Adresse MAC: {ordinateur['adresse_mac']}, Adresse IP: {adresse_ip[0]}.{adresse_ip[1]}.{adresse_ip[2]}.{adresse_ip[3]}")

    elif choix == '4':  # Quitter le programme
        print("Au revoir")
        break  # Sortie de la boucle et fin du programme

    else:
        print("Choix invalide, veuiller réessayer.")
