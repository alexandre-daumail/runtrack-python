import matplotlib.pyplot as plt

# Ouvrir le fichier texte en mode lecture
with open("../job01/data.txt", "r") as f:
    # Initialiser un dictionnaire pour stocker le nombre d'occurrences de chaque lettre suivante pour chaque lettre
    # de l'alphabet
    letter_counts = {chr(i): {} for i in range(ord('a'), ord('z')+1)}
    # Initialiser un dictionnaire pour stocker le nombre total de lettres pour chaque lettre de l'alphabet
    letter_totals = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    # Initialiser un compteur pour le nombre total de lettres dans le fichier
    total_letters = 0
    # Parcourir chaque ligne du fichier
    for line in f:
        # Supprimer les espaces de début et de fin de la ligne
        line = line.strip()
        # Parcourir chaque caractère de la ligne
        for i in range(len(line)-1):
            # Obtenir la lettre actuelle et la lettre suivante (en minuscule)
            current_letter = line[i].lower()
            next_letter = line[i+1].lower()
            # Si la lettre suivante est une lettre de l'alphabet,
            # ajouter 1 au compteur correspondant dans le dictionnaire
            if next_letter.isalpha():
                if next_letter in letter_counts[current_letter]:
                    letter_counts[current_letter][next_letter] += 1
                else:
                    letter_counts[current_letter][next_letter] = 1
                # Ajouter 1 au compteur total pour la lettre actuelle et pour le nombre total de lettres
                letter_totals[current_letter] += 1
                total_letters += 1

# Calculer le pourcentage d'apparition de chaque lettre suivante pour chaque lettre de l'alphabet
percentages = {
    letter: {
        next_letter:
            count/letter_totals[letter]*100
            for next_letter, count in counts.items()} for letter, counts in letter_counts.items()
}

# Générer un graphique de courbes superposées représentant le pourcentage
# d'apparition de chaque lettre suivante pour chaque lettre de l'alphabet
for letter in percentages:
    plt.plot(list(percentages[letter].keys()), list(percentages[letter].values()), label=letter)
plt.xlabel("Lettre suivante")
plt.ylabel("Pourcentage d'apparition")
plt.title("Graphique de courbes superposées des lettres suivantes dans le fichier 'data.txt'")
plt.legend()
plt.show()
