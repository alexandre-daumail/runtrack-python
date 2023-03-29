import random

# Chargement des statistiques
with open("../job01/data.txt", "r") as f:
    word_lengths = {}
    first_letters = {}
    letter_counts = {chr(i): {} for i in range(ord('a'), ord('z') + 1)}
    letter_totals = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    total_letters = 0
    for line in f:
        line = line.strip()
        for i in range(len(line) - 1):
            current_letter = line[i].lower()
            next_letter = line[i + 1].lower()
            if next_letter.isalpha():
                if current_letter.isalpha() and next_letter.isalpha() and next_letter in letter_counts[current_letter]:
                    letter_counts[current_letter][next_letter] += 1
                else:
                    if current_letter.isalpha() and next_letter.isalpha():
                        if next_letter in letter_counts[current_letter]:
                            letter_counts[current_letter][next_letter] += 1
                        else:
                            letter_counts[current_letter][next_letter] = 1
                letter_totals[current_letter] += 1
                total_letters += 1
        length = len(line)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1
        first_letter = line[0].lower()
        if first_letter in first_letters:
            first_letters[first_letter] += 1
        else:
            first_letters[first_letter] = 1


# Fonction pour générer un nouveau mot
def generate_word():
    # Choisir une longueur de mot au hasard en utilisant les statistiques de longueur de mot
    lengths = list(word_lengths.keys())
    weights = [word_lengths[length] for length in lengths]
    length = random.choices(lengths, weights=weights)[0]
    # Choisir une première lettre au hasard en utilisant les statistiques de première lettre
    letters = list(first_letters.keys())
    weights = [first_letters[letter] for letter in letters]
    first_letter = random.choices(letters, weights=weights)[0]
    # Construire le reste du mot en utilisant les statistiques d'enchaînement de lettres
    word = first_letter
    current_letter = first_letter
    for i in range(length - 1):
        counts = letter_counts[current_letter]
        letters = list(counts.keys())
        weights = [counts[letter] / letter_totals[current_letter] * 100 for letter in letters]
        next_letter = random.choices(letters, weights=weights)[0]
        word += next_letter
        current_letter = next_letter
    return word


# Générer 10 nouveaux mots et les afficher
for i in range(10):
    print(generate_word())
