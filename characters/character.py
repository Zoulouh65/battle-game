# classe de base pour tous les personnages
class Character:
    def init(self, name, hp, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor

# attaquer un autre personnage
    def attack(self, target):
        damage = self.weapon.damage - target.armor.defense
        if damage < 0:
            damage = 0

        target.hp = target.hp - damage
        
        print(self.name, "attaque", target.name, "avec", self.weapon.name)