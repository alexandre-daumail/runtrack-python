def est_valide(tableau, ligne, colonne, n):
    # Vérifie si une dame peut être placée sur la case (ligne, colonne)
    for i in range(ligne):
        if tableau[i][colonne] == 'X':
            return False
        if colonne-i >= 0 and tableau[ligne-i-1][colonne-i] == 'X':
            return False
        if colonne+i < n and tableau[ligne-i-1][colonne+i] == 'X':
            return False
    return True

def placer_dames(tableau, ligne, n):
    # Place les dames sur le plateau de manière récursive
    if ligne == n:
        return True
    for colonne in range(n):
        if est_valide(tableau, ligne, colonne, n):
            tableau[ligne][colonne] = 'X'
            if placer_dames(tableau, ligne+1, n):
                return True
            tableau[ligne][colonne] = 'O'
    return False

def afficher_plateau(tableau):
    # Affiche le plateau dans la console
    for ligne in tableau:
        print(' '.join(ligne))

n = int(input("Entrez le nombre de dames à placer : "))

# Initialisation du plateau de jeu
tableau = [['O' for i in range(n)] for j in range(n)]

# Placement des dames
placer_dames(tableau, 0, n)

# Affichage du plateau de jeu
afficher_plateau(tableau)
