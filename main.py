# Zé parti pour se mettre sur la tronche

from characters.Wizard import Wizard
from gears.Weapon import Weapon
from gears.Armor import Armor
from gears.Spells import Spells
from characters.character import Character
# Création des armures 

# Armure lourde de barbare

heavy_armor = Armor("Armure lourde de barbare", 15)

# Tunique de magicien

robe = Armor("Tunique de magicien", 5)

# Création des armes

# Hache de guerre

axe = Weapon("Axe", 10)

# Baguette magique

wand = Weapon("Magic Wand", 20)


# Création des personnages

# Barbare 

barbarian = Character("Conan", 100, axe, heavy_armor)

# Magicien

wizard = Character("Merlin", 80, wand, robe)

# Variable de départ

fight_beginning = 0

# Interface utilisateur
User_choice = str(input('Bienvenue dans ce RPG !\nVoulez-vous commencer le combat ?'))

if User_choice == 'oui':
    fight_beginning = 1
    print("Début du combat !")
else:
    fight_beginning =0

while (fight_beginning == 1) and (wizard.hp > 0) and (barbarian.hp > 0):

    if barbarian.hp > 0 :
        barbarian.attack(wizard)
        print("Results : ")
        print(barbarian.name, barbarian.hp, "HP")
        print(wizard.name, wizard.hp, "HP")
        input("--------------------")
    else:
        break

    if wizard.hp > 0:
        wizard.attack(barbarian)
        print("Results : ")
        print(wizard.name, wizard.hp, "HP")
        print(barbarian.name, barbarian.hp, "HP")
        input("--------------------")
    else:
        break

print("Fin du combat")