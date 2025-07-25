from characters.character import Character


class Wizard(Character):
    def __init__(self, name, hp, Weapon, Armor, Mana, Spells):
        Character.__init__(name, hp, Weapon, Armor, Mana, Spells)