from characters.character import Character
from gears.Spells import Spells  # Classe Spells avec name, damage, mana

class Wizard(Character):
    def __init__(self, name, hp, weapon, armor, mana, spell):
        super().__init__(name, hp, weapon, armor)
        self.mana = mana
        self.spell = spell  # un sort unique

    def attack(self, target):
        print(f"\n{self.name}! Mana: {self.mana}")

        if self.mana >= self.spell.mana:
            print(f"{self.name} casts {self.spell.name} on {target.name}!")
            damage = self.spell.damage - target.armor.defense
            damage = max(damage, 0)
            target.hp -= damage
            self.mana -= self.spell.mana
            print(f"{target.name} takes {damage} damage! ({target.hp} HP left)")
        else:
            self.punch(target)

    def punch(self, target):
        # Attaque de secours si plus de mana
        print(f"{self.name} has no mana and punches {target.name}!")
        damage = 2 - target.armor.defense  # petits dégâts
        damage = max(damage, 0)
        target.hp -= damage
        print(f"{target.name} takes {damage} damage. ({target.hp} HP left)")