"""
Classe Voiture pour la gestion d'un parc de voitures.
"""


class Voiture:
    """Classe représentant une voiture avec ses attributs."""
    
    def __init__(self, matricule, marque, couleur):
        """
        Initialise une voiture avec ses attributs.
        
        Args:
            matricule (str): Le matricule unique de la voiture
            marque (str): La marque de la voiture
            couleur (str): La couleur de la voiture
        """
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    
    def afficher_informations(self):
        """Affiche les informations de la voiture."""
        print(f"Matricule: {self.matricule}")
        print(f"Marque: {self.marque}")
        print(f"Couleur: {self.couleur}")
