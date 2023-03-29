import re
import xml.etree.ElementTree as et

# Ouvre le fichier "domains.xml"
tree = et.parse('domains.xml')
root = tree.getroot()

# Initialise un dictionnaire pour stocker le nombre d'extensions de domaines
extensions_count = {}

# Parcourt tous les éléments "domain" dans le fichier
for domain in root.findall('.//domain'):
    print(domain)
    # Récupère l'extension de domaine (la partie après le dernier point)
    extension = domain.text.split('.')[-1]
    # Ajoute 1 au compteur pour cette extension de domaine
    if extension in extensions_count:
        extensions_count[extension] += 1
    else:
        extensions_count[extension] = 1

# Affiche le nombre d'extensions de domaines trouvées
print("Nombre d'extensions de domaines trouvées :")
for extension, count in extensions_count.items():

    print(f"{extension}: {count}")

# Ouvre le fichier "data.txt"
with open("data.txt", "r") as input_file:
    # Lit le contenu du fichier
    content = input_file.read()
    # Supprime les caractères spéciaux (tout ce qui n'est pas une lettre ou un chiffre)
    content = re.sub(r"[^\w\s]", "", content)
    # Compte le nombre de mots (en utilisant l'espace comme séparateur)
    words = content.split()
    words_count = len(words)

# Affiche le nombre de mots trouvés
print(f"Nombre de mots trouvés dans le fichier 'data.txt' : {words_count}")
