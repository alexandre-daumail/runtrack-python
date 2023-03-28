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
