from characters.character import Character
from gears.Spell import Spell  # Classe Spells avec name, damage, mana

class Wizard(Character):
    def __init__(self, name:str, hp:int, Weapon:str, Armor:str, mana:int, spell:Spell):
        Character.__init__(self, name, hp, Weapon, Armor)
        self.mana = mana
        self.spell = spell  # un sort unique

    def attack(self, target:str):
        print(f"\n{self.name}! Mana: {self.mana}")

        if self.mana >= self.spell.mana_cost:
            print(f"{self.name} casts {self.spell.name} on {target.name}!")
            damage = (self.spell.damage *(100 - target.Armor.defense))/100
            damage = max(damage, 0)
            target.hp -= damage
            self.mana -= self.spell.mana_cost
            print(f"{target.name} takes {damage} damage! ({target.hp} HP left)")
        else:
            self.punch(target)

    def punch(self, target:str):
        # Attaque de secours si plus de mana
        print(f"{self.name} has no mana and punches {target.name}!")
        damage = 2 - target.armor.defense  # petits dégâts
        damage = max(damage, 0)
        target.hp -= damage
        print(f"{target.name} takes {damage} damage. ({target.hp} HP left)")