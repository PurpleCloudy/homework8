from random import randint
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
        new_quality = self.quality - randint(1,1000)
        return Potion(self.name, new_quality)

class Mana_Potion:
    def __init__(self, quality):
        self.name = 'mana potion'
        self.quality = quality
    def drinking(self):
        print(f'you drinked mana potion, mana + {quality}')

class Health_Potion:
    def __init__(self, quality):
        self.name = 'health potion'
        self.quality = quality
    def drinking(self):
        print(f'you drinked health potion, health + {quality1}')

class Mixed_Potion:
    def __init__(self, quality):
        self.name = 'mixed potion'
        self.quality = quality
    def drinking(self):
        print(f'you drinked health potion, health and mana + {quality}')
quality = randint(1, 100)
quality1 = randint(1, 100)
mana = Mana_Potion(quality)
mana.drinking()
health = Health_Potion(quality)
health.drinking()
mixed = Mixed_Potion(quality)
mixed.drinking()
game = True
potions = {}
while game:
    potion_name = input('Enter your potion name: ')
    if potion_name == 'exit':
        game = False
    potion_quality = randint(1, 100)
    new_potion = Potion(potion_name, potion_quality)
    potions[potion_name] = new_potion
    if len(potions) >= 2:
        action = input(f'Add(+) or subtract(-) your potions?').lower()
        potion1 = potions.popitem()[1]
        potion2 = potions.popitem()[1]
        if action == '+':
            mixed_potion = potion1 + potion2
        else:
            mixed_potion = potion1 - potion2
