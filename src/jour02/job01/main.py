import sys
sys.path.append('src\jour02')

from job0.personne import Personne

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
    
    def print(self):
        print(self.titre)


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []
    
    def listerOeuvre(self):
        print(f"Livres écrits par {self.nom} {self.prenom}:")
        for livre in self.oeuvre:
            livre.print()
    
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre

# Instanciation de personnes avec des valeurs de construction différentes
personne1 = Personne("Doe", "John")
personne2 = Personne("Nom1", "Prénom1")
personne3 = Personne("LastName", "FIrstname")

# Appel de la méthode "SePresenter()" pour chaque personne
personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()

# Utilisation des accesseurs pour obtenir les valeurs des attributs
print(personne1.getNom())  # affiche "Dupont"
print(personne2.getPrenom())  # affiche "Bob"

# Utilisation des mutateurs pour changer les valeurs des attributs
personne1.setNom("Da Vinci")
personne2.setPrenom("Bradley")

# Appel de la méthode "SePresenter()" après modification des attributs
personne1.SePresenter()  
personne2.SePresenter() 

# Instantiation of an author
author = Auteur("Tolkien", "J.R.R.")

# Creating some books for the author
book1 = author.ecrireUnLivre("Le Seigneur des Anneaux : La Communauté de l'Anneau")
book2 = author.ecrireUnLivre("Le Silmarillion")

# Displaying the books written by the author
author.listerOeuvre()
