pole = []
x = 0
progress = True
size = int(input())
for i in range(size):
    pole.append('_')
pole[x] = 'x'
while progress == True:
    users_input = input()
    if users_input == 'right':
        if x > size - 1:
            x = 0
        pole[x+1] = 'x'
        pole[x] = '_'
        x += 1
    if users_input == 'left':
        if x < 0:
            x = size - 1
        pole[x-1] = 'x'
        pole[x] = '_'
        x -= 1
    print(pole)