class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print(f"Bonjour, je m'appelle {self.nom} {self.prenom}.")
    
    def getNom(self):
        return self.nom
    
    def setNom(self, nouveauNom):
        self.nom = nouveauNom
    
    def getPrenom(self):
        return self.prenom
    
    def setPrenom(self, nouveauPrenom):
        self.prenom = nouveauPrenom

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
