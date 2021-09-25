time = 0
class Attacks:
    def choosing(name):
        if name == 'barbarian':
            print('barbarian attacks!!!')
        if name == 'mage':
            print('mage attacks!!!')
class Barbarian(Attacks):
    def name_choosing(users_input):
        name = users_input
        print('name of your barbarian -', name)
    def __init__(self,name):
        self.name = name
class Mage(Attacks):
    def name_choosing(users_input):
        name = users_input
        print('name of your mage -', name)
    def __init__(self,name):
        self.name = name
barbarian = Barbarian
mage = Mage
barbarian.name_choosing(input('print your barbarians name '))
mage.name_choosing(input('print your mages name '))
while time == 0:
    print('Who you wants to attack enemies?')
    user_input = input()
    Attacks.choosing(user_input)

