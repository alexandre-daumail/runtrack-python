import matplotlib.pyplot as plt

# Ouverture du fichier
with open('../job01/data.txt', 'r') as file:
    text = file.read().lower()

# Comptage des occurrences de chaque lettre
counts = {}
for letter in text:
    if letter.isalpha():
        counts[letter] = counts.get(letter, 0) + 1

# Calcul du pourcentage d'apparition de chaque lettre
total = sum(counts.values())
percentages = {letter: count/total*100 for letter, count in counts.items()}

# Affichage de l'histogramme
plt.bar(percentages.keys(), percentages.values())
plt.title("Pourcentage d'apparition de chaque lettre")
plt.xlabel("Lettres")
plt.ylabel("Pourcentage")
plt.show()
