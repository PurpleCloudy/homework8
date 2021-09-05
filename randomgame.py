import random 

output = ''

print('print start')
output += 'print start\n'

user_input = input()
    # with open('new_f', 'w+') as rand:
    #     # write_data = txt
    #     rand.write(txt)
    #     print(txt)
# print(write_data)

def game():
    random_number = random.randint(1,100)
    print('I create a random number, try to guess it')
    output += 'I create a random number, try to guess it\n'
    progress = True
    while progress == True:
        guess = int(input())
        if guess > random_number:
            print ('your guess > then my guess on', guess - random_number)
            output += f'your guess > then my guess on {guess - random_number}\n'
        if guess < random_number:
            #print('your number < then my guess on', random_number - guess)
            output += 'I create a random number, try to guess it\n'
        else: 
            progress = False
    return str()
game()

with open('D:/python/new_f', 'w') as f:
    pass

#я пробовал сделать весь вывод из консоли в файл, и получилось, но он не принимает инпуты
