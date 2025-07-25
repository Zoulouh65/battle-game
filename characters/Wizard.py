from characters.character import Character
from gears.Spells import Spells 

class Wizard(Character):
    def __init__(self, name, hp, weapon, armor, mana, spell):
        super().__init__(name, hp, weapon, armor)
        self.mana = mana
        self.spell = spell  # un sort

    def attack(self, target):
        print(f"\n{self.name} Mana: {self.mana}")

        if self.mana >= self.spell.mana:
            print(f"{self.name} lance {self.spell.name} sur {target.name} !")
            damage = self.spell.damage - target.armor.defense
            damage = max(damage, 0)
            target.hp -= damage
            self.mana -= self.spell.mana
            print(f"{target.name} subit {damage} dégâts ! ({target.hp} HP restants)")
        else:   
            self.punch(target)

    def punch(self, target):
        print(f"{self.name} plus de mana et frappe {target.name} à l'aide son sexe !")
        damage = 2 - target.armor.defense  # dégâts de pd 
        damage = max(damage, 0)
        target.hp -= damage
        print(f"{target.name} subit {damage} dégâts. ({target.hp} HP restants)") 
