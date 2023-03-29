# Demander à l'utilisateur de renseigner un nombre entier
taille = int(input("Entrez la taille des mots à chercher : "))

# Ouvrir le fichier "data.txt"
with open("../job01/data.txt", "r") as fichier:
    contenu = fichier.read()

# Séparer le contenu du fichier en mots
mots = contenu.split()

# Initialiser le compteur de mots de la taille recherchée
nb_mots_taille = 0

# Parcourir les mots et compter ceux de la taille recherchée
for mot in mots:
    if len(mot) == taille:
        nb_mots_taille += 1

# Afficher le résultat
print(f"Il y a {nb_mots_taille} mots de taille {taille} dans le fichier.")
