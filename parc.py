class Parc:
    
    def __init__(self):
        self.voitures = []
    
    def ajouter_voiture(self, voiture):
        self.voitures.append(voiture)
    
    def supprimer_voiture(self, matricule):
        for v in self.voitures:
            if v.matricule == matricule:
                self.voitures.remove(v)
                break
    
    def lister_voitures(self):
        for v in self.voitures:
            v.afficher_informations()
            print("---")