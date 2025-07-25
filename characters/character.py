# classe de base pour tous les personnages
class Character:
    def __init__(self, name, hp, Weapon, Armor):
        self.name = name
        self.hp = hp
        self.Weapon = Weapon
        self.Armor = Armor

# attaquer un autre personnage
    def attack(self, target):
        damage = self.Weapon.damage - target.Armor.defense
        if damage < 0:
            damage = 0

        target.hp = target.hp - damage
        
        print(self.name, "attack", target.name, "with", self.Weapon.name)

class Barbarian(Character):
    def __init__(self, name, hp, Weapon, Armor):
        Character.__init__(name, hp, Weapon, Armor)
    