# Demande à l'utilisateur de renseigner une chaîne de caractères
input_string = input("Entrez une chaîne de caractères : ")

# Ouvre le fichier "output.txt" en mode écriture
with open("output.txt", "w") as output_file:
    # Écrit la chaîne de caractères dans le fichier
    output_file.write(input_string)
    # Affiche un message pour confirmer l'écriture dans le fichier
    print("La chaîne de caractères a été écrite dans le fichier 'output.txt'.")
