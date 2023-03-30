# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
# programme devra calculer x^n, où n est le nombre fourni par l’utilisateur, sans utiliser de
# fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach
# ni ... boucle. Seulement de la récursivité.
def puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = puissance(x, n / 2)
        return y * y
    else:
        return x * puissance(x, n - 1)


x = int(input("Entrez un nombre : "))
n = int(input("Entrez la puissance : "))

resultat = puissance(x, n)
print("Le résultat est : ", resultat)
