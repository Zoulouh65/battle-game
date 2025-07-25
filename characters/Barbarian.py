from characters.character import Character


class Barbarian(Character):
    def __init__(self, name, hp, Weapon, Armor):
        Character.__init__(name, hp, Weapon, Armor)

    def attack(self, target):
        damage = 2*(self.Weapon.damage) - target.Armor.defense
        if damage < 0:
            damage = 0

        target.hp = target.hp - damage
        
        print(self.name, "attack", target.name, "with", self.Weapon.name)