class Parc:
    
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []
    
    def entrerVoiture(self, voiture):
        if len(self.listeVoitures) < self.capacite:
            for v in self.listeVoitures:
                if v.matricule == voiture.matricule:
                    print("Erreur: Cette voiture existe deja dans le parc")
                    return False
            self.listeVoitures.append(voiture)
            print("Voiture ajoutee au parc")
            return True
        else:
            print("Erreur: Parc plein")
            return False
    
    def sortirVoiture(self, matricule):
        for v in self.listeVoitures:
            if v.matricule == matricule:
                self.listeVoitures.remove(v)
                print("Voiture retiree du parc")
                print("Places libres: " + str(self.calculerNbrPlacesLibres()))
                return True
        print("Erreur: Voiture non trouvee")
        return False