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
