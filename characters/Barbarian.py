from characters.character import Character


class Barbarian(Character):
    def __init__(self, name:str, hp:int, Weapon:str, Armor:str):
        Character.__init__(self,name, hp, Weapon, Armor)

    def attack(self, target):
        for i in range(0,1) :
            damage = (self.Weapon.damage) - target.Armor.defense
            if damage < 0:
                damage = 0
            i += 1

        target.hp = target.hp - damage

        print(self.name, "attack", target.name, "with", self.Weapon.name)