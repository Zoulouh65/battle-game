from characters.character import Character


class Barbarian(Character):
    def __init__(self, name:str, hp:int, Weapon:str, Armor:str):
        Character.__init__(self,name, hp, Weapon, Armor)

    # attaquer un autre personnage
    def attack(self, target:str):
        for i in range(2) :
            damage = (self.Weapon.damage *(100 - target.Armor.defense))/100
            target.hp = target.hp - damage
            round(target.hp)
            print(self.name, "attack", target.name, "with", self.Weapon.name)
            if target.hp <= 0 :
                target.hp = 0
                print(f"{target.name} takes {damage} damage. {target.name} is dead. {target.hp} HP left")
                break 
            else:
                print(f"{target.name} takes {damage} damage. ({target.hp} HP left)")
    