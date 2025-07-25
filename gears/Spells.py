# Définittion des spells

class Spells:
    def __init__(self, name:str, damage:int, mana_cost:int):
        self.name = name            # nom du spell
        self.damage = damage        # dégâts du spell
        self.mana_cost = mana_cost  # Coût en mana du spell
