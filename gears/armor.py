# Définitions des armures

class Armor:
    def __init__(self, name, defense):
        self.name = name        # Nom de l'armure
        self.defense = defense  # Nombre de point de vie bonus


# Armure lourde de barbare

heavy_armor = Armor("Armure lourde de barbare", 15)

# Tunique de magicien

robe = Armor("Tunique de magicien", 5)