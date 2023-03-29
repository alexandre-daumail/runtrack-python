class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print(f"Le client {self.nom} {self.prenom} possède les livres suivants :")
        for livre in self.collection:
            print(livre.titre)

    def louer(self, bibliotheque, livre_titre):
        livre = bibliotheque.catalogue.get(livre_titre)
        if livre and livre.quantite > 0:
            bibliotheque.catalogue[livre_titre].quantite -= 1
            self.collection.append(livre)
            print(f"{self.nom} {self.prenom} a loué le livre {livre_titre}.")
        else:
            print(f"Désolé, le livre {livre_titre} n'est pas disponible en ce moment.")

    def rendreLivres(self, bibliotheque):
        for livre in self.collection:
            if livre.titre in bibliotheque.catalogue:
                bibliotheque.catalogue[livre.titre].quantite += 1
            else:
                bibliotheque.catalogue[livre.titre] = livre
        self.collection = []


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def ecrireLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        print(f"{self.nom} {self.prenom} a écrit le livre {titre}.")
        return livre

    def inventaire(self):
        print(f"L'oeuvre de {self.nom} {self.prenom} comprend les livres suivants :")
        for livre in self.oeuvre:
            print(livre.titre)


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


class Bibliotheque:

    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        if titre in auteur.oeuvre:
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
            print(f"{quantite} exemplaire(s) du livre '{titre}' ont été ajouté(s) au catalogue.")
        else:
            print(f"Le livre '{titre}' n'existe pas dans l'oeuvre de l'auteur.")

    def inventaire(self):
        print("Inventaire de la bibliothèque :")
        for titre, quantite in self.catalogue.items():
            print(f"- {quantite} exemplaire(s) de '{titre}'")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            if titre in client.collection:
                client.collection[titre] += 1
            else:
                client.collection[titre] = 1
            self.catalogue[titre] -= 1
            print(f"Le livre '{titre}' a été ajouté à la collection du client '{client.nom}'.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible.")

    def rendreLivres(self, client):
        for titre, quantite in client.collection.items():
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
        client.collection = {}
        print(f"Les livres de '{client.nom}' ont été rendus et ajoutés au catalogue.")


# Ensuite, instanciez des auteurs, faites leurs écrire des livres, créer des bibliothèques,
# faites les acheter des livres, créez des clients, faites les louer des livres puis utilisez des
# fonctions d'affichage et montrez le résultat à votre examinateur.

# Instanciation des auteurs
auteur1 = Auteur("Hugo", "Victor")
auteur2 = Auteur("Gustave", "Flaubert")

# Création de livres
livre1 = auteur1.ecrireLivre("Les Misérables")
livre2 = auteur2.ecrireLivre("Madame Bovary")

# Création de bibliothèques
bibliotheque1 = Bibliotheque("Marseille")
bibliotheque2 = Bibliotheque("Aix")

# Achat de livres par les bibliothèques
bibliotheque1.acheterLivre(auteur1, "Les Misérables", 1500)
bibliotheque2.acheterLivre(auteur2, "Madame Bovary", 500)

# Instanciation de clients
client1 = Client("Doe", "John")
client2 = Client("Bob", "Landy")

# Location de livres par les clients
bibliotheque1.louer(client1, "Les Misérables")
bibliotheque2.louer(client2, "Les Misérables")
