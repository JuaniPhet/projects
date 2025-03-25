class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        else:return False

    def retourner(self):
        self.disponible = True

# livre1 = Livre("Le Petit Prince", "Monsieur K")

# print(livre1.titre)  # Affiche "Le Petit Prince"
# print(livre1.auteur)  # Affiche "Monsieur K"
# livre1.emprunter()
# print(livre1.disponible)  # Affiche False
# livre1.retourner()
# print(livre1.disponible)  # Affiche True
