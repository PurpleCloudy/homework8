import random
#рисовалка
def painting():
    for i in pole:
        print(' '.join(i))

#создание поля
size = int(input())
pole = []
for i in range(size):
    pole = pole + [['_']*size]
#х - номер списка сверху вниз
x = 0
#у - номер элемента в списке слева направо
y = 0
#
progress = True

#создание крестика в заданных координатах
pole[x][y] = 'x'
painting()

#список того, что прога может
command_list = ['up', 'down', 'left','right','exit']

def traps():
    for i in range(size*2):
        pole[random.randint(0,size-1)][random.randint(0,size-1)] = 'O'
        if pole [0][0] == 'O':
            pole[0][0] == '_'




 #подьем крестика
def up(x,y):      
    if pole[x-1][y] == 'O':
        print('you cant pass here')
    else:
        pole[x][y] = '_'
        if x < 0:
            x = size - 1
        x -= 1
        pole[x][y] = 'x'
    painting()
    return x

 #спуск крестика
def down(x,y):
    if pole[x+1][y] == 'O':
        print('you cant pass here')
    else:
        pole[x][y] = '_'
        if x >= size - 1:
            x = -1
        x += 1
        pole[x][y] = 'x'
    painting()
    return x

 #крестик влево
def left(x,y):
    if pole[x][y-1] == 'O':
        print('you cant pass here')
    else:
        pole[x][y] = '_'
        if y < 0:
            y = size - 1
        y -= 1
        pole[x][y] = 'x'
    painting()
    return y

#крестик вправо
def right(x,y):
    if pole[x][y+1] == 'O':
        print('you cant pass here')
    else:   
        pole[x][y] = '_'
        if y > size - 1:
            y = -1
        y += 1
        pole[x][y] = 'x'
    painting()
    return y

 #выход
def exit():
    progress = False

#сама собственно программа
traps()
while progress == True:
    user_input = input()
    if user_input == 'up':
        x = up(x,y)
    if user_input == 'down':
        x = down(x,y)
    if user_input == 'left':
        y = left(x,y)
    if user_input == 'right':
        y = right(x,y)
    if user_input == 'exit':
        exit()
print('good bye')
