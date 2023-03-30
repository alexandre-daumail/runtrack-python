import re


def compare_chains(chaine1, chaine2):
    chaine2 = chaine2.replace("*", ".+")
    return bool(re.match("^" + chaine2 + "$", chaine1))


chaine1 = input("Entrez la première chaîne : ").lower()
chaine2 = input("Entrez la deuxième chaîne : ").lower()

if compare_chains(chaine1, chaine2):
    print("1")
else:
    print("0")
