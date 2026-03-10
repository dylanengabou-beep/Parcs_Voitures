from voiture import Voiture
from parc import Parc

print("=== Test etape 4: entrerVoiture ===")
parc = Parc(1, "123 Rue Principale", 3)
v1 = Voiture("ABC123", "Toyota", "Rouge")
parc.entrerVoiture(v1)
