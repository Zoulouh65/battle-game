# Classe de base pour les personnages

class Character:
    def __init__(self, name, hp, weapon, armor):
        self.name = name        # Nom du personnage
        self.hp = hp            # Santé du personnage
        self.weapon = weapon    