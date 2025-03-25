from livre import Livre

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def rechercher_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                return livre
            else:
                return None

    def emprunter_livre(self, titre):
        livre = self.rechercher_par_titre(titre)
        if livre is None:
            print(f"Le livre '{titre}' est introuvable.")
            return
        elif livre.disponible:
            livre.emprunter()
            print(f"Le livre '{titre}' a été emprunté.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible.")

    def retourner_livre(self, titre):
        livre = self.rechercher_par_titre(titre)
        if livre is None:
            print(f"Le livre '{titre}' n'appartient pas a la la bibliotheque {self.nom}; nous ne pouvons donc pas le retourner.")
            return
        elif livre.disponible:
            print(f"Le livre '{titre}' est deja dans les rayons. Il provient surement d'une autre bibliotheque.")
        else:
            livre.retourner()
            print(f"Le livre '{titre}' a été retourné.")

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Disponible: {'Oui' if livre.disponible else 'Non'}")



bibliotheque = Bibliotheque("GLOBALLINK")  

bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Monsieur K"))
bibliotheque.ajouter_livre(Livre("L'Alchimiste", "Paulo Coelho"))

bibliotheque.afficher_livres()

bibliotheque.emprunter_livre("Le Petit Prince")

bibliotheque.emprunter_livre("Le Petit Prince")

bibliotheque.afficher_livres()

bibliotheque.retourner_livre("Le Petit Prince")

bibliotheque.afficher_livres()

bibliotheque.retourner_livre("Le Petit Prince")

bibliotheque.afficher_livres()

bibliotheque.retourner_livre("L'Oeil de l'ours")

bibliotheque.afficher_livres()