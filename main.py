# Zé parti pour se mettre sur la tronche

from gears.Weapon import Weapon
from gears.Armor import Armor
from characters.character import Character

# Création des armures 

# Armure lourde de barbare

heavy_armor = Armor("Armure lourde de barbare", 15)

# Tunique de magicien

robe = Armor("Tunique de magicien", 5)

# Création des armes

# Hache de guerre

axe = Weapon("Hache de guerre", 10)

# Baguette magique

wand = Weapon("Baguette magique", 20)


# Création des personnages

# Barbare 

barbarian = Character("Conan", 100, axe, heavy_armor)

# Magicien

wizard = Character("Merlin", 80, wand, robe)