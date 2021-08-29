size = int(input())
pole = []
for i in range(size):
    pole = pole + [['_']*size]
x = 0
y = 0
progress = True
pole[x][y] = 'x'
for i in pole:
    print(' '.join(i))
while progress == True:
    user_input = input()
    if user_input == 'up': 
        pole[x][y] = '_'
        if x < 0:
           x = size - 1
        x -= 1
        pole[x][y] = 'x'
        for i in pole:
            print(' '.join(i))
    if user_input == 'down':
        pole[x][y] = '_'
        if x > size - 1:
            x = 0
        x += 1
        pole[x][y] = 'x'
        for i in pole:
            print(' '.join(i))
    if user_input == 'left': 
        pole[x][y] = '_'
        if y < 0:
           y = size - 1
        y -= 1
        pole[x][y] = 'x'
        for i in pole:
            print(' '.join(i))
    if user_input == 'right':
        pole[x][y] = '_'
        if y > size - 1:
            y = 0
        y += 1
        pole[x][y] = 'x'
        for i in pole:
            print(' '.join(i))
    if user_input == 'exit':
        progress = False
print('good bye')