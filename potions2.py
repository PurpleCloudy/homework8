from random import randint
import random
class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
    def __str__(self):
        return f'this potion named {self.name}'
    def __add__(self, other):
        new_name = self.name + other.name
        new_quality = (self.quality + other.quality) // 2
        return Potion(new_name, new_quality)
    def __sub__(self, other):
        new_quality = self.quality - other.quality
        if new_quality <= 0:
            print('health -10, potion exploded')
        return Potion(self.name, new_quality)

class Mana_Potion(Potion):
    def drinking(self):
        print(f'you drinked mana potion, mana + {quality}')

class Health_Potion(Potion):
    def drinking(self):
        print(f'you drinked health potion, health + {quality}')

class Mixed_Potion(Potion):
    def drinking(self):
        print(f'you drinked health potion, health and mana + {quality}')
game = True
potions = {}
while game:
    potion_name = [mana_potion, health_potion, super_potion]
    if potion_name == 'exit':
        game = False
    potion_quality = randint(1, 100)
    if potion_name == mana_potion:
        mana_potion = Mana_Potion('mana',randint(1,100) )
    if potion_name == health_potion:
        health_potion = Health_Potion('health',randint(1,100) )
    if potion_name == health_potion:
        super_potion = Mixed_Potion('health and mana',randint(1,100) )
    potions[potion_name] = 
    if len(potions) >= 2:
        action = input(f'Add(+) or subtract(-) your potions?').lower()
        potion1 = potions.popitem()[1]
        potion2 = potions.popitem()[1]
        if action == '+':
            mixed_potion = potion1 + potion2
        else:
            mixed_potion = potion1 - potion2
