from voiture import Voiture
from parc import Parc

parc = Parc(1, "123 Rue Principale", 3)

v1 = Voiture("ABC123", "Toyota", "Rouge")
v2 = Voiture("DEF456", "Honda", "Bleu")
v3 = Voiture("GHI789", "Ford", "Noir")

parc.entrerVoiture(v1)
parc.entrerVoiture(v2)
parc.entrerVoiture(v3)