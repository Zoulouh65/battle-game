# Zé parti pour se mettre sur la tronche

from characters.Wizard import Wizard
from gears.Weapon import Weapon
from gears.Armor import Armor
from gears.Spell import Spell
from characters.character import Character
from characters.Barbarian import Barbarian
from characters.Wizard import Wizard

# Création des armures 

# Armure lourde de barbare

heavy_armor = Armor("Armure lourde de barbare", 15)

# Tunique de magicien

robe = Armor("Tunique de magicien", 5)

# Création des armes

# Hache de guerre

axe = Weapon("Axe", 10)

# Baguette magique

wand = Weapon("Magic Wand", 2)

# Spells

fireball = Spell("Fireball",20,15)

# Création des personnages

# Barbare 

barbarian = Barbarian("Conan", 100, axe, heavy_armor)

# Magicien

wizard = Wizard("Merlin", 80, wand, robe, 100, fireball)

# Variable de départ

fight_beginning = 0

# Interface utilisateur
User_choice = str(input('Bienvenue dans ce RPG !\nVoulez-vous commencer le combat ?'))


while User_choice not in ['oui','non']:
    User_choice = str(input('S\'il vous plaît, choisissez entre oui et non >>>>>'))
    fight_beginning = 0


if User_choice == 'oui':
    fight_beginning = 1
    print("Début du combat !")
else:
    fight_beginning = 0
    print('Au revoir dans ce cas')


while (fight_beginning == 1) and (wizard.hp > 0) and (barbarian.hp > 0):

    if barbarian.hp <= 0:
        break

    barbarian.attack(wizard)
    print("Results : ")
    print(barbarian.name, barbarian.hp, "HP")
    print(wizard.name, wizard.hp, "HP")
    input("--------------------")

    if wizard.hp <= 0:
        break

    wizard.attack(barbarian)
    print("Results : ")
    print(wizard.name, wizard.hp, "HP")
    print(barbarian.name, barbarian.hp, "HP")
    input("--------------------")

    if barbarian.hp <= 0:
        print("Fin du combat le gagnant est Wizard")
    else:
        print("Fin du combat le gagnant est Barbarian")
