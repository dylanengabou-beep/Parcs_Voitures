from voiture import Voiture
from parc import Parc

print("=== Test etape 6: calculerNbrPlacesLibres ===")
parc = Parc(1, "123 Rue Principale", 3)
v1 = Voiture("ABC123", "Toyota", "Rouge")
v2 = Voiture("DEF456", "Honda", "Bleu")
parc.entrerVoiture(v1)
parc.entrerVoiture(v2)
print("Places libres: " + str(parc.calculerNbrPlacesLibres()))
