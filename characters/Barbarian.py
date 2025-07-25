from characters.character import Character


class Barbarian(Character):
    def __init__(self, name, hp, Weapon, Armor):
        Character.__init__(name, hp, Weapon, Armor)
