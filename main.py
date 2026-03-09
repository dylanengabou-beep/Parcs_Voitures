from voiture import Voiture
from parc import Parc

# Créer quelques voitures
v1 = Voiture("ABC123", "Toyota", "Rouge")
v2 = Voiture("DEF456", "Honda", "Bleu")

# Créer un parc
parc = Parc()

# Ajouter les voitures au parc
parc.ajouter_voiture(v1)
parc.ajouter_voiture(v2)

# Lister les voitures
print("Voitures dans le parc :")
parc.lister_voitures()

# Supprimer une voiture
parc.supprimer_voiture("ABC123")

print("Après suppression :")
parc.lister_voitures()