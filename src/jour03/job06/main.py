import matplotlib.pyplot as plt

# Ouvrir le fichier texte en mode lecture
with open("../job01/data.txt", "r") as f:
    # Initialiser un dictionnaire pour stocker le nombre d'occurrences de chaque lettre
    letter_counts = {}
    # Parcourir chaque ligne du fichier
    for line in f:
        # Séparer la ligne en mots
        words = line.split()
        # Parcourir chaque mot de la ligne
        for word in words:
            # Obtenir la première lettre du mot (en minuscule)
            first_letter = word[0].lower()
            # Si la lettre est déjà présente dans le dictionnaire, ajouter 1 au compteur
            if first_letter in letter_counts:
                letter_counts[first_letter] += 1
            # Sinon, ajouter la lettre au dictionnaire avec un compteur initialisé à 1
            else:
                letter_counts[first_letter] = 1

# Calculer le nombre total de mots dans le fichier
total_words = sum(letter_counts.values())

# Calculer le pourcentage de présence de chaque lettre en début de mot
percentages = [count/total_words*100 for count in letter_counts.values()]

# Générer un histogramme représentant le pourcentage de présence de chaque lettre en début de mot
plt.bar(letter_counts.keys(), percentages)
plt.xlabel("Lettre")
plt.ylabel("Pourcentage de présence")
plt.title("Histogramme des lettres en début de mot dans le fichier 'data.txt'")
plt.show()
