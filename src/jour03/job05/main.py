import matplotlib.pyplot as plt

# Ouvrir le fichier texte en mode lecture
with open("../job01/data.txt", "r") as f:
    # Initialiser un dictionnaire pour stocker le nombre de mots de chaque taille
    word_counts = {}
    # Parcourir chaque ligne du fichier
    for line in f:
        # Séparer la ligne en mots
        words = line.split()
        # Parcourir chaque mot de la ligne
        for word in words:
            # Obtenir la taille du mot
            length = len(word)
            # Si la taille est déjà présente dans le dictionnaire, ajouter 1 au compteur
            if length in word_counts:
                word_counts[length] += 1
            # Sinon, ajouter la taille au dictionnaire avec un compteur initialisé à 1
            else:
                word_counts[length] = 1

# Calculer le nombre total de mots dans le fichier
total_words = sum(word_counts.values())

# Calculer le pourcentage d'apparition de chaque taille de mot
percentages = [count/total_words*100 for count in word_counts.values()]

# Générer un histogramme représentant le pourcentage d'apparition de chaque taille de mot
plt.bar(word_counts.keys(), percentages)
plt.xlabel("Taille des mots")
plt.ylabel("Pourcentage d'apparition")
plt.title("Histogramme des tailles de mots dans le fichier 'data.txt'")
plt.show()
